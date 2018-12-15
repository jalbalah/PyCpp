
from pdb import set_trace as st

class Transpile:
    
    def __new__(cls, line):
        """ return tuple of .h and .cpp strings to write to file """
        cpp = ''

        indent_stack = []
        line.append('END')
        for c in range(0, len(line)):
            line[c] = line[c].replace("'", '"')
            line[c] = line[c].rstrip()
            if line[c].strip() == '':
                line[c] = ''
            else:
                indent = cls.get_num_indent(line[c])
                if indent and (not indent_stack or indent > indent_stack[-1]):
                    indent_stack.append(indent)
                    line[c] = (indent_stack[-1] - 4) * ' ' + '{\n' + line[c]
                elif indent_stack and indent < indent_stack[-1]:
                    while indent_stack and indent < indent_stack[-1]:
                        line[c - 1] += '\n' + (indent_stack[-1] - 4) * ' ' + '}'
                        del indent_stack[-1]
        line[-1] = line[-1].replace('END', '')

        line = '\n'.join(line).split('\n')

        class_name = ''
        libs_to_add = set({})
        in_class = [False, -1]
        private_members = []
        for c in range(0, len(line)):
            lstrip = line[c].strip().replace(' ', '')
            if lstrip.startswith('class'):
                in_class[0] = True
                in_class[1] = cls.get_num_indent(line[c])
                class_name = line[c][line[c].find('class ') + 6:-1]
                line[c] = 'class {}'.format(class_name)
            elif lstrip.startswith('def__init__'):
                args = cls.get_args(line, c)
                line[c] = \
                    line[c][0:line[c].find('def')] \
                    + class_name \
                    + '(' + ','.join(['auto ' + str(x) for x in args]) + ')'
                if 'self' in line[c + 2]:
                    c += 2
                    while 'self' in line[c]:
                        line[c] = line[c].replace('self.', 'this->')
                        i = line[c].find('->') + 2
                        i2 = line[c].find('=') + 1
                        private_members.append((line[c][i:line[c].find(' ', i)],
                                                line[c][i2::]))
                        c += 1
            elif lstrip.startswith('def'):
                args = cls.get_args(line, c)
                func_name = line[c][line[c].find('def ') + 4:line[c].find('(')]
                line[c] = \
                    line[c][0:line[c].find('def')] \
                    + func_name \
                    + '(' + ','.join([str(x) for x in args]) + ')'
            elif lstrip.startswith('if__name__=="__main__":'):
                line[c] = 'int main()'

            if in_class[0] and '}' in line[c]:
                if cls.get_num_indent(line[c]) == in_class[1]:
                    in_class[0] = False
                    line[c] += ';'
                    if private_members:
                        pvt = 'private:\n'
                    for mbr in private_members:
                        typ, libs_to_add = cls.get_type(mbr[1], libs_to_add)
                        pvt += '    {} {};\n'.format(typ,  mbr[0]);
                    if private_members:
                        line[c] = pvt + line[c]

            if 'print(' in lstrip:
                line[c] = line[c].replace('print(', 'std::cout << ')
                line[c] = line[c][0:line[c].rfind(')')] + " << std::endl;"
                libs_to_add.add('iostream')

            if line[c] and line[c][-1] != ';' and ')' != line[c].strip()[-1]:
                if not ('{' in line[c] or '}' in line[c]
                        or 'def' in line[c] or 'class' in line[c]):
                    line[c] += ';'
        for lib in libs_to_add:
            line.insert(0, '#include<{}>'.format(lib))

        cpp = '\n'.join(filter(None, line))
        print(cpp)
        return cpp

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
