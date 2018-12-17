
from pdb import set_trace as st

class Transpile:
    
    def __new__(cls, line):
        """ return tuple of .h and .cpp strings to write to file """
        cpp = ''
        line = Transpile.get_indented(line)

        class_name = ['']
        libs_to_add = set({})
        in_class = [False, -1]
        in_class_done = True
        private_members = []

        for c in range(0, len(line)):
            lstrip = line[c].strip().replace(' ', '')
            if lstrip.startswith('//'):
                pass
            else:
                if lstrip.startswith('class'):
                    in_class[0] = True
                    in_class_done = False
                    in_class[1] = Transpile.get_num_indent(line[c])
                    cn = line[c][line[c].find('class ') + 6::].replace(":", "")
                    class_name.append(cn)
                    line[c] = 'class {}'.format(class_name[-1])
                elif lstrip.startswith('def__init__'):
                    args = Transpile.get_args(line, c)
                    line[c] = \
                        line[c][0:line[c].find('def')] \
                        + class_name[-1] \
                        + '(' + ', '.join(['auto ' + str(x) for x in args]) + ')'
                    c += 2
                    c2 = c
                    while '}' not in line[c2] and c2 < len(line):
                        if 'self.' in line[c2]:
                            line[c2] = line[c2].replace('self.', 'this->')
                            i = line[c2].find('->') + 2
                            i2 = line[c2].find('=') + 1
                            private_members.append((line[c2][i:line[c2].find(' ', i)],
                                                    line[c2][i2::]))
                        c2 += 1
                elif lstrip.startswith('def'):
                    args = Transpile.get_args(line, c)
                    func_name = line[c][line[c].find('def ') + 4:line[c].find('(')]
                    line[c] = \
                        line[c][0:line[c].find('def')] \
                        + func_name \
                        + '(' + ','.join([str(x) for x in args]) + ')'
                elif lstrip.startswith('if__name__=="__main__":'):
                    line[c] = 'int main()'
                elif lstrip.startswith('print('):
                    libs_to_add.add('iostream')
                    i = line[c].find('print(') + 6
                    i2 = line[c].find(')', i)
                    args = line[c][i:i2].replace(',', '<< " " << ')
                    line[c] = line[c][0:i] + args + line[c][i2::]
                    line[c] = line[c].replace('print(', 'std::cout << ')
                    line[c] = line[c][0:line[c].rfind(')')] + " << std::endl;"


                elif line[c].strip().endswith(']'):
                    typ = line[c][line[c].find('[') + 1:line[c].find(']')]
                    line[c] = line[c][0:line[c].find('[') + 1] + line[c][line[c].find(']')::]
                    line[c] = line[c].replace('[]', 'std::vector<{}>()'.format(typ))
                elif lstrip.startswith('for') and 'range' in lstrip:
                    i = line[c].find(' in ') + 4
                    var = line[c][line[c].find('for') + 3:i - 4].replace('(', '').strip()
                    rnge = line[c][i:line[c].find(':')]
                    rnge = [x.strip() for x in rnge[rnge.find('(') + 1:rnge.find(')')].split(',')]
                    if len(rnge) == 2:
                        op = '++' if rnge[0] < rnge[1] else '--'
                        line[c] = line[c][0:line[c].find('f')] + \
                            'for(auto {} = {}; {} != {}; {}{})'.format(var, rnge[0], var, rnge[1], op, var)
                    elif len(rnge) == 3:
                        line[c] = line[c][0:line[c].find('f')] + \
                                  'for(auto {} = {}; {} != {}; {} += {})'.format(var, rnge[0], var, rnge[1], var, rnge[2])
                elif lstrip.startswith('for'):
                    i = line[c].find(':')
                    i2 = line[c].rfind(' ', 0)
                    obj = line[c][i2:i].replace(':', '').strip()
                    forlp = 'for(auto it = {}.begin(); it != {}.end(); ++it)'.format(obj, obj)
                    line[c] = line[c][0:line[c].find('f')] + forlp
                    line[c + 1] = line[c + 1] + '\n    ' + line[c + 1].replace('{', 'auto i = *it;')
                    # st()
                elif lstrip.startswith('if') and line[c].strip().endswith(':'):
                    i = line[c].find('if') + 2
                    line[c] = line[c][0:i] + '(' + line[c][i + 1:-1] + ')'

                if in_class[0]:
                    if '{' in line[c] and not in_class_done:
                        line[c] += '\npublic:'
                        in_class_done = True
                    elif '}' in line[c]:
                        if Transpile.get_num_indent(line[c]) == in_class[1]:
                            in_class[0] = False
                            line[c] += ';'
                            if private_members:
                                pvt = '\n'
                            for mbr in private_members:
                                typ, libs_to_add = Transpile.get_type(mbr[1], libs_to_add)
                                pvt += '    {} {};\n'.format(typ,  mbr[0]);
                            if private_members:
                                line[c] = pvt + line[c]

                line = cls.add_semicolon(line, c)
                line = cls.instantiation(line, c, class_name)

        for lib in libs_to_add:
            line.insert(0, '#include<{}>'.format(lib))

        cpp = '\n'.join(filter(None, line))
        print(cpp)
        return cpp

    @staticmethod
    def get_indented(line):
        indent_stack = []
        line.append('END')
        for c in range(0, len(line)):
            line[c] = line[c].replace("'", '"').replace('#', '//').replace('append', 'push_back') \
                .replace('pass', ';')
            line[c] = line[c].rstrip()
            if line[c].strip() == '':
                line[c] = ''
            else:
                indent = Transpile.get_num_indent(line[c])
                if indent and (not indent_stack or indent > indent_stack[-1]):
                    indent_stack.append(indent)
                    line[c] = (indent_stack[-1] - 4) * ' ' + '{\n' + line[c]
                elif indent_stack and indent < indent_stack[-1]:
                    while indent_stack and indent < indent_stack[-1]:
                        line[c - 1] += '\n' + (indent_stack[-1] - 4) * ' ' + '}'
                        del indent_stack[-1]
        line[-1] = line[-1].replace('END', '')
        line = '\n'.join(line).split('\n')
        return line

    @staticmethod
    def add_semicolon(line, c):
        if line[c] and line[c][-1] != ';' and (')' != line[c].strip()[-1] or ('=' in line[c] or '.' in line[c]) and not ';' in line[c]):
            if not ('{' in line[c] or '}' in line[c]
                    or 'def' in line[c] or 'class' in line[c]):
                line[c] += ';'
        return line

    @staticmethod
    def instantiation(line, c, class_name):
        for clas in class_name[1::]:
            if clas in line[c] and '=' in line[c]:
                i = len(line[c]) - len(line[c].lstrip())
                stack_init = line[c].lstrip()
                var_name = stack_init[0:stack_init.find(' ')]
                args = stack_init[stack_init.find('('):stack_init.find(')') + 1].strip()
                line[c] = i * ' ' + clas + ' ' + var_name + args + ';'
        return line

    @staticmethod
    def get_num_indent(line):
        for i in range(4 * 8, -1, -4):
            indent = ' ' * i
            if line.startswith(indent):
                return i
        return 0  # no indent

    @staticmethod
    def get_args(line, c):
        return [x.strip() for x in
                line[c].strip()[line[c].strip().find(','):-1][0:-1].split(',')[1::]]

    @staticmethod
    def get_type(x, libs_to_add):
        # st()
        if x.strip()[0] == '[' and x.strip()[-1] == ']':
            libs_to_add.add('vector')
            return ['std::vector<{}>'.format(x[x.find('[') + 1:x.find(']')]), libs_to_add]
        try:
            int(x)
            if '.' in x:
                return ['float', libs_to_add]
            else:
                return ['int', libs_to_add]
        except ValueError:
            return ['float', libs_to_add]
        except Exception:
            libs_to_add.add('string')
            return ['std::string', libs_to_add]
