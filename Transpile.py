
from pdb import set_trace as st
from time import time


class Transpile:
    
    def __new__(cls, line):
        """ return tuple of .h and .cpp strings to write to file """
        cpp = ''
        line = Transpile.get_indented(line)

        class_name = []
        libs_to_add = set({})
        in_class = [False, -1]
        in_class_done = True
        entered_constructor = False
        private_members = []
        static_members = []
        write_files = []

        for c in range(0, len(line)):
            lstrip = line[c].lstrip().replace(' ', '')
            if '#' in lstrip:
                pass
            else:
                if lstrip.startswith('class'):
                    in_class[0] = True
                    in_class_done = False
                    in_class[1] = Transpile.get_num_indent(line[c])
                    entered_constructor = False
                    cn = line[c][line[c].find('class ') + 6::].replace(":", "")
                    class_name.append(cn)
                    line[c] = 'class {}'.format(class_name[-1])
                elif lstrip.startswith('def__init__'):
                    entered_constructor = True
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
                        line[c][0:line[c].find('def')] + \
                        func_name + \
                        '(' + ','.join(['auto ' + str(x) for x in args]) + ')'
                    return_type = 'void ' if '{' in line[c + 1] else ''
                    i = line[c].find(line[c].strip()[0])
                    line[c] = line[c][0:i] + return_type + line[c][i::]
                elif lstrip.startswith('if__name__=='):
                    line[c] = 'int main()'
                elif lstrip.startswith('print('):
                    libs_to_add.add('iostream')
                    i = line[c].find('print(') + 6
                    i2 = line[c].find(')', i)
                    args = line[c][i:i2].replace(',', '<< " " << ')
                    line[c] = line[c][0:i] + args + line[c][i2::]
                    line[c] = line[c].replace('print(', 'std::cout << ')
                    line[c] = line[c][0:line[c].rfind(')')] + " << std::endl;"
                elif line[c].strip().endswith(']') and not cls.between(line[c], ':', '[', ']'):
                    libs_to_add.add('vector')
                    typ = line[c][line[c].find('[') + 1:line[c].find(']')]
                    line[c] = line[c][0:line[c].find('[') + 1] + line[c][line[c].find(']')::]
                    line[c] = line[c].replace('[]', 'std::vector<{}>()'.format(typ))
                    if '=' in line[c] and not 'this->' in line[c] and ')' in line[c]:
                        # if entered_constructor:
                        line[c] = ' ' * cls.get_num_indent(line[c]) + 'auto ' + line[c].lstrip()
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
                    var_name = line[c].strip()
                    var_name = var_name[var_name.find(' ') + 1::]
                    var_name = var_name[0:var_name.find(' ')]
                    auto_line = 'auto {} = *it;'.format(var_name)
                    line[c] = line[c][0:line[c].find('f')] + forlp
                    line[c + 1] = line[c + 1] + '\n    ' + line[c + 1].replace('{', auto_line)
                elif lstrip.startswith('if') and line[c].strip().endswith(':'):
                    i = line[c].find('if') + 2
                    line[c] = line[c][0:i] + '(' + line[c][i + 1:-1] + ')'
                elif 'open(' in line[c]:
                    indent = ' ' * cls.get_num_indent(line[c])
                    ifstream = 'f{}'.format(cls.get_time())
                    i = line[c].find('open(') + 5
                    i2 = line[c].find(',', i)
                    fn = line[c][i:i2]
                    var_name = line[c][0:line[c].find('=')].strip()
                    ftype = line[c][i2 + 1:line[c].find(')', i2)].strip()[1:-1]
                    if ftype == 'r':
                        libs_to_add.add('string')
                        libs_to_add.add('fstream')
                        libs_to_add.add('iostream')
                        libs_to_add.add('vector')
                        indent = ' ' * cls.get_num_indent(line[c])
                        line2 = indent + 'std::ifstream file({});\n'.format(fn)
                        line2 += indent + 'std::vector<std::string> {};\n'.format(var_name)
                        line2 += indent + 'if(file.is_open()){\n'
                        line2 += indent + '    std::string line;\n'
                        line2 += indent + '    while (getline(file, line)) {\n'
                        line2 += indent + '        {}.push_back(line);\n'.format(var_name)
                        line2 += indent + '    }; file.close();\n'
                        line2 += indent + '}'
                        line[c] = line2
                    elif ftype == 'w':
                        libs_to_add.add('fstream')
                        indent = ' ' * cls.get_num_indent(line[c])
                        line[c] = indent + 'std::ofstream {}({});'.format(var_name, fn)
                        write_files.append(var_name)
                elif '.write(' in line[c]:
                    string_to_write = line[c][line[c].find('.write(') + 7:-1]
                    for var_wf in write_files:
                        if var_wf + '.write(' in line[c]:
                            indent = ' ' * cls.get_num_indent(line[c])
                            line[c] = indent + '{} << {};\n'.format(var_wf, string_to_write)
                            line[c] += indent + '{}.close();\n'.format(var_wf)
                elif 'while' in line[c]:
                    i = line[c].find('while') + 5
                    line[c] = line[c][0:i] + '(' + line[c][i::].strip()[0:-1] + ')'
                elif Transpile.between(line[c], ':', '[', ']'):
                    var_name = line[c].strip().replace('auto ', '')
                    var_name = var_name[0:var_name.find(' ')]  # .replace('X', 'auto ')
                    a = line[c][line[c].find('[') + 1:line[c].find(':')]
                    b = line[c][line[c].find(':') + 1:line[c].find(']')]
                    vector_or_string = line[c][line[c].find('=') + 1:line[c].find('[')].strip()
                    indent = ' ' * Transpile.get_num_indent(line[c])

                    c2 = c - 1
                    while not cls.found_type(line, c2, vector_or_string):
                        c2 -= 1

                    line_type = Transpile.get_assign_type(line[c2])

                    if line_type == 'std::string':
                        libs_to_add.add('string')
                        line_type = 'char'
                        vector = 'auto {} = {}.substr({}, {});'
                        line2 = indent + vector.format(var_name, vector_or_string, a, b)
                    else:
                        libs_to_add.add('vector')
                        vector = 'std::vector<{}> {}({}.begin() + {}, {}.begin() + {});'
                        line2 = indent + vector.format(
                            line_type, var_name, vector_or_string, a, vector_or_string, b)
                    line[c] = line2
                elif 'find(' in line[c]:
                    var_name = line[c].strip().replace('auto ', '')
                    var_name = var_name[0:var_name.find(' ')]  # .replace('X', 'auto ')
                    vector_or_string = line[c][line[c].find('=') + 1:line[c].find('.find(')].strip()
                    i = line[c].find('.find(') + 6
                    string_find = line[c][i:line[c].find(')', i)].replace('"', "'")
                    string_find = string_find.replace("'", '"')
                    indent = ' ' * Transpile.get_num_indent(line[c])

                    c2 = c - 1
                    while not cls.found_type(line, c2, vector_or_string):
                        c2 -= 1

                    line_type = Transpile.get_assign_type(line[c2])

                    if line_type == 'std::string':
                        find_str = 'int {} = {}.find({});'
                        line2 = indent + find_str.format(var_name, vector_or_string, string_find)
                    else:
                        libs_to_add.add('algorithm')
                        find_str = 'int {} = std::find({}.begin(), {}.end(), {}) - {}.begin();'
                        line2 = indent + find_str.format(
                            var_name, vector_or_string, vector_or_string, string_find, vector_or_string)
                    line[c] = line2
                elif '.join(' in line[c]:
                    libs_to_add.add('iterator')
                    libs_to_add.add('sstream')
                    libs_to_add.add('string')
                    indent = ' ' * cls.get_num_indent(line[c])
                    line[c] = line[c].replace("'", '"')
                    i = line[c].find('"')
                    i2 = line[c].find('"', i + 1) + 1
                    i3 = line[c].find('.join(') + 6
                    i4 = line[c].find(')', i3)
                    separator = line[c][i:i2]
                    vector = line[c][i3:i4]
                    var_name = line[c][0:line[c].find('=')].strip()
                    ostringstream = 'os{}'.format(cls.get_time())
                    line2 = indent + 'std::ostringstream {};\n'.format(ostringstream)
                    copy_string = 'std::copy({}.begin(), {}.end() - 1, \n' + \
                                  '          std::ostream_iterator<std::string>({}, {}));\n'
                    line2 += indent + copy_string.format(vector, vector, ostringstream, separator)
                    line2 += indent + '{} << *({}).rbegin();\n'.format(ostringstream, vector)
                    line2 += indent + 'std::string {} = {}.str();\n'.format(var_name, ostringstream)
                    line[c] = line2
                # bottom of elif
                elif '=' in line[c] and not 'this->' in line[c] and not 'self.' in line[c] \
                        and not 'auto' in line[c]:
                    found_class = False
                    for clas in class_name:
                        if clas in line[c]:
                            found_class = True
                    if not found_class:
                        line[c] = line[c] + ' POSSIBLE LOCAL DECLARATION'

                if in_class[0]:
                    if not entered_constructor:
                        if line[c] and not 'class' in line[c] and not '{' in line[c] and '=' in line[c]:
                            var = line[c].strip()
                            var = var.replace('auto ', '')
                            var = var[0:var.find(' ')]
                            assignment = line[c][line[c].find('=') + 1::].strip()
                            line[c] = ''
                            for clas in class_name:
                                if assignment.startswith('{}('.format(clas)):
                                    assignment = clas
                            private_members.append(('static ' + var, assignment))
                    if '{' in line[c] and not in_class_done:
                        line[c] += '\n' + ' ' * cls.get_num_indent(line[c]) + '    public:'
                        in_class_done = True
                    elif '}' in line[c]:
                        if Transpile.get_num_indent(line[c]) == in_class[1]:
                            in_class[0] = False
                            # static_members = []
                            line[c] += ';'
                            if private_members:
                                pvt = '\n'
                                for mbr in private_members:
                                    if mbr[1] not in class_name and 'vector' not in mbr[1]:
                                        typ, libs_to_add = Transpile.get_type(mbr[1], libs_to_add, class_name)
                                    else:
                                        typ = mbr[1].replace('<str>', '<string>')
                                        typ = typ.replace('<string>', '<std::string>')
                                        if 'string' in typ:
                                            libs_to_add.add('string')
                                    if 'static' in mbr[0]:
                                        typ = 'static ' + typ.replace('()', '')
                                        pvt += '    {} {};\n'.format(typ, mbr[0].replace('static ', ''))
                                        static_mem = typ.replace('static ', '')
                                        static_mem += ' {}::{}'.format(class_name[-1], mbr[0].replace('static ', ''))
                                        static_mem += ' = {}'.format(cls.get_default_initializer(typ.replace('static ', '')))
                                        static_members.append(static_mem)
                                    else:
                                        pvt += '    {} {};\n'.format(typ,  mbr[0]);
                                line[c] = pvt + line[c]
                            private_members = []
                line = cls.add_semicolon(line, c)
                line = cls.instantiation(line, c, class_name, entered_constructor)

        line.insert(0, '\n')
        for lib in libs_to_add:
            line.insert(0, '#include<{}>'.format(lib))

        # O(N) loops
        line = cls.get_replacements(line)
        line = cls.add_static_member_initializers(line, static_members)
        line = cls.add_auto_for_local_vars(line, class_name, private_members, static_members)
        line = cls.convert_char_to_string(line)
        line = cls.convert_len_to_size(line)

        cpp = '\n'.join(filter(None, line))
        return cpp

    @staticmethod
    def convert_len_to_size(line):
        for c in range(0, len(line)):
            if 'len(' in line[c]:
                i = line[c].find('len(')
                i2 = line[c].find(')', i) + 1
                line2 = line[c][0:i] + line[c][i:i2].replace('len', '') + '.size()' + line[c][i2::]
                line2 = line2.replace('len(', '(')
                line[c] = line2
        return line

    @staticmethod
    def convert_char_to_string(line):
        for c in range(0, len(line)):
            if Transpile.get_assign_type(line[c]) == 'std::string' \
                    and 'vector' not in line[c] and 'this->' not in line[c] and '.substr(' not in line[c]\
                    and (line[c].find('.') == -1 or not line[c].find('.') < line[c].find('=')):
                i = line[c].find('"')
                i2 = line[c].find('"', i + 1)
                line[c] = line[c][0:i] + '("' + line[c][i + 1:i2] + '");'
                line[c] = line[c].replace(' = ', '').replace('=', '').replace(' =', '').replace('= ', '')
                line[c] = line[c].replace('auto ', 'std::string ')
        return line

    @staticmethod
    def add_auto_for_local_vars(line, class_name, private_members, static_members):
        flag = ' POSSIBLE LOCAL DECLARATION'
        local_vars = []
        closing_braces = []  # what indents of scope are open
        for c in range(0, len(line)):
            if '{' in line[c]:
                indent = Transpile.get_num_indent(line[c])
                closing_braces.append(indent)
            elif '}' in line[c]:
                _ = closing_braces.pop()
                if local_vars:
                    local_vars2 = []
                    for i in range(0, len(local_vars)):
                        if closing_braces and local_vars[i][0] <= closing_braces[-1]:  # ?
                            local_vars2.append(local_vars[i])
                    local_vars = local_vars2

            if flag in line[c]:
                static_mem_found = False
                for static_mem in static_members:
                    i = static_mem.find('::') + 2
                    static_mem = static_mem[i:static_mem.find(' ', i)]
                    if static_mem in line[c]:
                        static_mem_found = True
                if not static_mem_found:
                    local_var_found = False
                    for local_var in local_vars:
                        indent = local_var[0]
                        local_var = local_var[1]
                        if indent <= Transpile.get_num_indent(line[c]):
                            if local_var + ' =' in line[c] or local_var + '=' in line[c] \
                                    or local_var + ' -=' in line[c] or local_var + ' +=' in line[c]:
                                local_var_found = True
                    if not local_var_found:
                        if line[c].find('.') == -1 or not line[c].find('.') < line[c].find('='):
                            line[c] = ' ' * Transpile.get_num_indent(line[c]) + 'auto ' + line[c].lstrip()
                            local_vars.append((Transpile.get_num_indent(line[c]),
                                               line[c][0:line[c].find('=')]
                                               .replace('auto ', '').replace('-', '').strip()))
                    elif 'i4' in line[c]:
                        st()
                line[c] = line[c].replace(flag, '')

        return line

    @staticmethod
    def add_static_member_initializers(line, static_members):
        for c in range(0, len(line)):
            if 'main' in line[c]:
                line[c] = '{};\n'.format(';\n'.join([x for x in static_members])) + line[c]
        return line

    @staticmethod
    def get_default_initializer(typ):
        if typ == 'int':
            return 0
        elif typ == 'float':
            return 0.0
        elif typ == 'string':
            return ''
        elif 'vector' in typ:
            return {}
        else:
            return typ + '()'

    @staticmethod
    def get_replacements(line):
        for c in range(0, len(line)):
            if '#' not in line[c] and '#' not in line[c]:
                line[c] = line[c] \
                    .replace('self.', 'this->').replace('>()];', '>();') \
                    .replace('append', 'push_back').replace('pass', ';') \
                    .replace('" +', '" <<').replace('"+', ' << ').replace('+"', ' << "').replace('+ "', '<< "') \
                    .replace(';;;', ';').replace(';;', ';').replace('"<<', '" <<').replace('<<"', '<< "') \
                    .replace('vector<str>', 'vector<std::string>')\
                    .replace(' str(', ' std::to_string(').replace('(str(', '(std::to_string(')
                if 'std::cout <<' in line[c]:
                    line[c] = line[c]\
                        .replace(', "', '<< "').replace('",', '" <<').replace(", '", "<< '").replace("' ,", "' <<")
            else:
                if '#include' not in line[c]:
                    line[c] = line[c].replace('#', '//')
            if 'std::find(' not in line[c]:
                line[c] = line[c].replace("'", '"')
        return line

    @staticmethod
    def get_indented(line):
        indent_stack = []
        line.append('END')
        for c in range(0, len(line)):
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
        not_in = lambda x: x not in line[c]
        yes_in = lambda x: not not_in(x)
        if line[c] and not_in('//') and not_in('if') and not_in('for') and not_in('class') and not_in('main'):
            if yes_in('=') or (not_in(';') and not_in('void')):
                if not ('{' in line[c] or '}' in line[c] and not_in('def') and not_in('class')):
                    if not_in('while('):
                        line[c] += ';'
        return line


    @staticmethod
    def instantiation(line, c, class_name, entered_constructor):
        if entered_constructor:
            for clas in class_name:
                if clas in line[c] and '=' in line[c]:
                    if line[c].strip().endswith(']'):
                        i = len(line[c]) - len(line[c].lstrip())
                        vector = line[c].lstrip()
                        var_name = vector[0:vector.find(' ')]
                        vector = vector[vector.find('[') + 1:vector.find(']')]
                        vector = 'vector<{}>();'.format(vector)
                        spacer = ' ' * Transpile.get_num_indent(line[c])
                        line[c] = '{}{} = {}'.format(spacer, var_name, vector)
                    else:
                        i = Transpile.get_num_indent(line[c])
                        stack_init = line[c].lstrip()
                        var_name = stack_init[0:stack_init.find(' ')]
                        args = stack_init[stack_init.find('('):stack_init.find(')') + 1].strip()
                        try:
                            args = '' if args.strip()[1] == ')' else args
                            if 'this->' in line[c]:
                                raise TypeError('')
                            line[c] = i * ' ' + clas + ' ' + var_name + args + ';'
                        except IndexError:
                            line[c] = i * ' ' + var_name + ' = ' + 'std::vector<{}>();'.format(clas)
                        except:
                            pass
            return line
        else:
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
    def get_type(x, libs_to_add=set(), class_name=['']):
        if x.strip()[0] == '[' and x.strip()[-1] == ']':
            libs_to_add.add('vector')
            typ = x[x.find('[') + 1:x.find(']')].strip()
            return ['std::vector<{}>'.format(typ), libs_to_add]
        try:
            int(x)
            if '.' in x:
                return ['float', libs_to_add]
            else:
                return ['int', libs_to_add]
        except ValueError:
            for clas in class_name[1::]:
                if clas + '(' in x:
                    return [clas, libs_to_add]
            if '""' in x or "''" in x:
                libs_to_add.add('string')
                return ['std::string', libs_to_add]
            for clas in class_name:
                if clas in x:
                    return [clas, libs_to_add]
            return ['float', libs_to_add]
        except Exception:
            libs_to_add.add('string')
            return ['std::string', libs_to_add]

    @staticmethod
    def between(s, btw, a, b):
        """ return True if btw between a and b """
        s = s.replace('::', '')  # ignore std::, etc.
        ai = s.rfind(a)
        bi = s.rfind(b)
        btwi = s.rfind(btw)
        return True if btwi < bi and btwi > ai else False

    @staticmethod
    def get_assign_type(line_c):
        if '.substr(' in line_c:
            return 'std::string'
        line_c = line_c[line_c.find('=') + 1:line_c.find(';')].strip()
        if not line_c.strip():
            return
        if 'vector<' in line_c:
            i = line_c.find('vector<') + 7
            return line_c[i:line_c.find('>')]
        if '"' == line_c.strip()[0] or "'" == line_c.strip()[0]:
            return 'std::string'
        elif '.' in line_c:
            return 'float'
        else:
            return 'int'

    @staticmethod
    def get_time():
        return str(int(1000 * time()))

    @staticmethod
    def found_type(line, c2, vector_or_string):
        return c2 < 0 or \
               ((vector_or_string + '=' in line[c2] or vector_or_string + ' =' in line[c2]
                 or ' ' + vector_or_string + '(' in line[c2])
                and 'cout' not in line[c2] and '.find' not in line[c2]
                and '.append' not in line[c2] and '.size' not in line[c2]
                and 'len(' not in line[c2] and '#' not in line[c2]
                and vector_or_string not in line[c2].replace(vector_or_string, '', 1))
