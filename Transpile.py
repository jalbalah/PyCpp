
from pdb import set_trace as st
from time import time


class Transpile:
    
    def __init__(self, line):
        """ return tuple of .h and .cpp strings to write to file """
        self.cpp = ''
        self.line = line
        self.line = self.get_indented()

        self.class_name = []
        self.libs_to_add = set({})
        self.in_class = [False, -1]
        self.in_class_done = True
        self.entered_constructor = False
        self.private_members = []
        self.static_members = []
        self.write_files = []

        for c in range(0, len(self.line)):
            lstrip = self.line[c].lstrip().replace(' ', '')
            if '#' in lstrip:
                pass
            else:
                if lstrip.startswith('class'):
                    # line_class()
                    self.in_class[0] = True
                    self.in_class_done = False
                    self.in_class[1] = self.get_num_indent(self.line[c])
                    self.entered_constructor = False
                    cn = self.line[c][self.line[c].find('class ') + 6::].replace(":", "")
                    self.class_name.append(cn)
                    self.line[c] = 'class {}'.format(self.class_name[-1])
                elif lstrip.startswith('def__init__'):
                    self.entered_constructor = True
                    args = self.get_args(c)
                    self.line[c] = \
                        self.line[c][0:self.line[c].find('def')] \
                        + self.class_name[-1] \
                        + '(' + ', '.join(['auto ' + str(x) for x in args]) + ')'
                    c += 2
                    c2 = c
                    while '}' not in self.line[c2] and c2 < len(self.line):
                        if 'self.' in self.line[c2]:
                            self.line[c2] = self.line[c2].replace('self.', 'this->')
                            i = self.line[c2].find('->') + 2
                            i2 = self.line[c2].find('=') + 1
                            self.private_members.append((self.line[c2][i:self.line[c2].find(' ', i)],
                                                    self.line[c2][i2::]))
                        c2 += 1
                elif lstrip.startswith('def'):
                    args = self.get_args(c)
                    func_name = self.line[c][self.line[c].find('def ') + 4:self.line[c].find('(')]
                    self.line[c] = \
                        self.line[c][0:self.line[c].find('def')] + \
                        func_name + \
                        '(' + ','.join(['auto ' + str(x) for x in args]) + ')'
                    return_type = 'void ' if '{' in self.line[c + 1] else ''
                    i = self.line[c].find(self.line[c].strip()[0])
                    self.line[c] = self.line[c][0:i] + return_type + self.line[c][i::]
                elif lstrip.startswith('if__name__=='):
                    self.line[c] = 'int main()'
                elif lstrip.startswith('print('):
                    self.libs_to_add.add('iostream')
                    i = self.line[c].find('print(') + 6
                    i2 = self.line[c].find(')', i)
                    args = self.line[c][i:i2].replace(',', '<< " " << ')
                    self.line[c] = self.line[c][0:i] + args + self.line[c][i2::]
                    self.line[c] = self.line[c].replace('print(', 'std::cout << ')
                    self.line[c] = self.line[c][0:self.line[c].rfind(')')] + " << std::endl;"
                elif self.line[c].strip().endswith(']') and not self.between(self.line[c], ':', '[', ']') \
                        and self.line[c][self.line[c].find('[') + 1:self.line[c].find(']')] in ('str', 'int', 'float'):
                    self.libs_to_add.add('vector')
                    typ = self.line[c][self.line[c].find('[') + 1:self.line[c].find(']')]
                    if typ == 'str' or typ == 'string':
                        self.libs_to_add.add('string')
                    self.line[c] = self.line[c][0:self.line[c].find('[') + 1] + self.line[c][self.line[c].find(']')::]
                    self.line[c] = self.line[c].replace('[]', 'std::vector<{}>()'.format(typ))
                    if '=' in self.line[c] and not 'this->' in self.line[c] and ')' in self.line[c]:
                        self.line[c] = ' ' * self.get_num_indent(self.line[c]) + 'auto ' + self.line[c].lstrip()
                elif lstrip.startswith('for') and 'range' in lstrip:
                    i = self.line[c].find(' in ') + 4
                    var = self.line[c][self.line[c].find('for') + 3:i - 4].replace('(', '').strip()
                    rnge = self.line[c][i:self.line[c].find(':')]
                    rnge = [x.strip() for x in rnge[rnge.find('(') + 1:rnge.find(')')].split(',')]
                    if len(rnge) == 2:
                        op = '++' if rnge[0] < rnge[1] else '--'
                        self.line[c] = self.line[c][0:self.line[c].find('f')] + \
                            'for(auto {} = {}; {} != {}; {}{})'.format(var, rnge[0], var, rnge[1], op, var)
                    elif len(rnge) == 3:
                        self.line[c] = self.line[c][0:self.line[c].find('f')] + \
                                  'for(auto {} = {}; {} != {}; {} += {})'.format(var, rnge[0], var, rnge[1], var, rnge[2])
                elif lstrip.startswith('for'):
                    i = self.line[c].find(':')
                    i2 = self.line[c].rfind(' ', 0)
                    obj = self.line[c][i2:i].replace(':', '').strip()
                    forlp = 'for(auto it = {}.begin(); it != {}.end(); ++it)'.format(obj, obj)
                    var_name = self.line[c].strip()
                    var_name = var_name[var_name.find(' ') + 1::]
                    var_name = var_name[0:var_name.find(' ')]
                    auto_line = 'auto {} = *it;'.format(var_name)
                    self.line[c] = self.line[c][0:self.line[c].find('f')] + forlp
                    self.line[c + 1] = self.line[c + 1] + '\n    ' + self.line[c + 1].replace('{', auto_line)
                elif lstrip.startswith('if') and self.line[c].strip().endswith(':'):
                    i = self.line[c].find('if') + 2
                    self.line[c] = self.line[c][0:i] + '(' + self.line[c][i + 1:-1] + ')'
                elif 'open(' in self.line[c]:
                    indent = ' ' * self.get_num_indent(self.line[c])
                    ifstream = 'f{}'.format(self.get_time())
                    i = self.line[c].find('open(') + 5
                    i2 = self.line[c].find(',', i)
                    fn = self.line[c][i:i2]
                    var_name = self.line[c][0:self.line[c].find('=')].strip()
                    ftype = self.line[c][i2 + 1:self.line[c].find(')', i2)].strip()[1:-1]
                    if ftype == 'r':
                        self.libs_to_add.add('string')
                        self.libs_to_add.add('fstream')
                        self.libs_to_add.add('iostream')
                        self.libs_to_add.add('vector')
                        indent = ' ' * self.get_num_indent(self.line[c])
                        line2 = indent + 'std::ifstream file({});\n'.format(fn)
                        line2 += indent + 'std::vector<std::string> {};\n'.format(var_name)
                        line2 += indent + 'if(file.is_open()){\n'
                        line2 += indent + '    std::string line;\n'
                        line2 += indent + '    while (getline(file, line)) {\n'
                        line2 += indent + '        {}.push_back(self.line);\n'.format(var_name)
                        line2 += indent + '    }; file.close();\n'
                        line2 += indent + '}'
                        self.line[c] = line2
                    elif ftype == 'w':
                        self.libs_to_add.add('fstream')
                        indent = ' ' * self.get_num_indent(self.line[c])
                        self.line[c] = indent + 'std::ofstream {}({});'.format(var_name, fn)
                        self.write_files.append(var_name)
                elif '.write(' in self.line[c]:
                    string_to_write = self.line[c][self.line[c].find('.write(') + 7:-1]
                    for var_wf in self.write_files:
                        if var_wf + '.write(' in self.line[c]:
                            indent = ' ' * self.get_num_indent(self.line[c])
                            self.line[c] = indent + '{} << {};\n'.format(var_wf, string_to_write)
                            self.line[c] += indent + '{}.close();\n'.format(var_wf)
                elif 'while' in self.line[c]:
                    i = self.line[c].find('while') + 5
                    self.line[c] = self.line[c][0:i] + '(' + self.line[c][i::].strip()[0:-1] + ')'
                elif self.between(self.line[c], ':', '[', ']'):
                    var_name = self.line[c].strip().replace('auto ', '')
                    var_name = var_name[0:var_name.find(' ')]  # .replace('X', 'auto ')
                    a = self.line[c][self.line[c].find('[') + 1:self.line[c].find(':')]
                    b = self.line[c][self.line[c].find(':') + 1:self.line[c].find(']')]
                    vector_or_string = self.line[c][self.line[c].find('=') + 1:self.line[c].find('[')].strip()
                    indent = ' ' * self.get_num_indent(self.line[c])

                    c2 = c - 1
                    while not self.found_type(c2, vector_or_string):
                        c2 -= 1
                    line_type = self.get_assign_type(self.line[c2])

                    if line_type == 'std::string':
                        self.libs_to_add.add('string')
                        line_type = 'char'
                        vector = 'auto {} = {}.substr({}, {});'
                        line2 = indent + vector.format(var_name, vector_or_string, a, b)
                    else:
                        self.libs_to_add.add('vector')
                        vector = 'std::vector<{}> {}({}.begin() + {}, {}.begin() + {});'
                        line2 = indent + vector.format(
                            line_type, var_name, vector_or_string, a, vector_or_string, b)
                    self.line[c] = line2
                elif 'find(' in self.line[c]:
                    var_name = self.line[c].strip().replace('auto ', '')
                    var_name = var_name[0:var_name.find(' ')]  # .replace('X', 'auto ')
                    vector_or_string = self.line[c][self.line[c].find('=') + 1:self.line[c].find('.find(')].strip()
                    i = self.line[c].find('.find(') + 6
                    string_find = self.line[c][i:self.line[c].find(')', i)].replace('"', "'")
                    string_find = string_find.replace("'", '"')
                    indent = ' ' * self.get_num_indent(self.line[c])

                    c2 = c - 1
                    while not self.found_type(c2, vector_or_string):
                        c2 -= 1

                    line_type = self.get_assign_type(self.line[c2])

                    if line_type == 'std::string':
                        self.libs_to_add.add('string')
                        find_str = 'int {} = {}.find({});'
                        line2 = indent + find_str.format(var_name, vector_or_string, string_find)
                    else:
                        self.libs_to_add.add('algorithm')
                        find_str = 'int {} = std::find({}.begin(), {}.end(), {}) - {}.begin();'
                        line2 = indent + find_str.format(
                            var_name, vector_or_string, vector_or_string, string_find, vector_or_string)
                    self.line[c] = line2
                elif '.join(' in self.line[c]:
                    self.libs_to_add.add('iterator')
                    self.libs_to_add.add('sstream')
                    self.libs_to_add.add('string')
                    indent = ' ' * self.get_num_indent(self.line[c])
                    self.line[c] = self.line[c].replace("'", '"')
                    i = self.line[c].find('"')
                    i2 = self.line[c].find('"', i + 1) + 1
                    i3 = self.line[c].find('.join(') + 6
                    i4 = self.line[c].find(')', i3)
                    separator = self.line[c][i:i2]
                    vector = self.line[c][i3:i4]
                    var_name = self.line[c][0:self.line[c].find('=')].strip()
                    ostringstream = 'os{}'.format(self.get_time())
                    line2 = indent + 'std::ostringstream {};\n'.format(ostringstream)
                    copy_string = indent + 'std::copy({}.begin(), {}.end() - 1, \n' + \
                                  '              std::ostream_iterator<decltype({}[0])>({}, {}));\n'
                    line2 += copy_string.format(vector, vector, vector, ostringstream, separator)
                    line2 += indent + '{} << *({}).rbegin();\n'.format(ostringstream, vector)
                    line2 += indent + 'std::string {} = {}.str();\n'.format(var_name, ostringstream)
                    self.line[c] = line2
                # bottom of elif
                elif '=' in self.line[c] and not 'this->' in self.line[c] and not 'self.' in self.line[c] \
                        and not 'auto' in self.line[c]:
                    found_class = False
                    for clas in self.class_name:
                        if clas in self.line[c]:
                            found_class = True
                    if not found_class:
                        self.line[c] = self.line[c] + ' POSSIBLE LOCAL DECLARATION'

                if self.in_class[0]:
                    if not self.entered_constructor:
                        if self.line[c] and not 'class' in self.line[c] and not '{' in self.line[c] and '=' in self.line[c]:
                            var = self.line[c].strip()
                            var = var.replace('auto ', '')
                            var = var[0:var.find(' ')]
                            assignment = self.line[c][self.line[c].find('=') + 1::].strip()
                            self.line[c] = ''
                            for clas in self.class_name:
                                if assignment.startswith('{}('.format(clas)):
                                    assignment = clas
                            self.private_members.append(('static ' + var, assignment))
                    if '{' in self.line[c] and not self.in_class_done:
                        self.line[c] += '\n' + ' ' * self.get_num_indent(self.line[c]) + '    public:'
                        self.in_class_done = True
                    elif '}' in self.line[c]:
                        if self.get_num_indent(self.line[c]) == self.in_class[1]:
                            self.in_class[0] = False
                            # self.static_members = []
                            self.line[c] += ';'
                            if self.private_members:
                                pvt = '\n'
                                for mbr in self.private_members:
                                    if mbr[1] not in self.class_name and 'vector' not in mbr[1]:
                                        typ, self.libs_to_add = self.get_type(mbr[1])
                                    else:
                                        typ = mbr[1].replace('<str>', '<string>')
                                        typ = typ.replace('<string>', '<std::string>')
                                        if 'string' in typ:
                                            self.libs_to_add.add('string')
                                    if 'static' in mbr[0]:
                                        typ = 'static ' + typ.replace('()', '')
                                        pvt += '    {} {};\n'.format(typ, mbr[0].replace('static ', ''))
                                        static_mem = typ.replace('static ', '')
                                        static_mem += ' {}::{}'.format(self.class_name[-1], mbr[0].replace('static ', ''))
                                        static_mem += ' = {}'.format(self.get_default_initializer(typ.replace('static ', '')))
                                        self.static_members.append(static_mem)
                                    else:
                                        pvt += '    {} {};\n'.format(typ,  mbr[0]);
                                self.line[c] = pvt + self.line[c]
                            self.private_members = []
                self.line = self.add_semicolon(c)
                self.line = self.instantiation(c)

        self.line.insert(0, '\n')
        for lib in self.libs_to_add:
            self.line.insert(0, '#include<{}>'.format(lib))

        # O(N) loops
        self.line = self.get_replacements()
        self.line = self.add_static_member_initializers()
        self.line = self.add_auto_for_local_vars()
        self.line = self.convert_char_to_string()
        self.line = self.convert_len_to_size()

        self.cpp = '\n'.join(filter(None, self.line))
        # return self.cpp
    
    # def line_class(self):
        
    def convert_len_to_size(self):
        for c in range(0, len(self.line)):
            if 'len(' in self.line[c]:
                i = self.line[c].find('len(')
                i2 = self.line[c].find(')', i) + 1
                line2 = self.line[c][0:i] + self.line[c][i:i2].replace('len', '') + '.size()' + self.line[c][i2::]
                line2 = line2.replace('len(', '(')
                self.line[c] = line2
        return self.line

    def convert_char_to_string(self):
        for c in range(0, len(self.line)):
            if self.get_assign_type(self.line[c]) == 'std::string' \
                    and 'vector' not in self.line[c] and 'this->' not in self.line[c] and '.substr(' not in self.line[c]\
                    and (self.line[c].find('.') == -1 or not self.line[c].find('.') < self.line[c].find('=')):
                i = self.line[c].find('"')
                i2 = self.line[c].find('"', i + 1)
                self.line[c] = self.line[c][0:i] + '("' + self.line[c][i + 1:i2] + '");'
                self.line[c] = self.line[c].replace(' = ', '').replace('=', '').replace(' =', '').replace('= ', '')
                self.line[c] = self.line[c].replace('auto ', 'std::string ')
        return self.line

    def add_auto_for_local_vars(self):
        flag = ' POSSIBLE LOCAL DECLARATION'
        local_vars = []
        closing_braces = []  # what indents of scope are open
        for c in range(0, len(self.line)):
            if '{' in self.line[c]:
                indent = self.get_num_indent(self.line[c])
                closing_braces.append(indent)
            elif '}' in self.line[c]:
                _ = closing_braces.pop()
                if local_vars:
                    local_vars2 = []
                    for i in range(0, len(local_vars)):
                        if closing_braces and local_vars[i][0] <= closing_braces[-1]:  # ?
                            local_vars2.append(local_vars[i])
                    local_vars = local_vars2

            if flag in self.line[c]:
                static_mem_found = False
                for static_mem in self.static_members:
                    i = static_mem.find('::') + 2
                    static_mem = static_mem[i:static_mem.find(' ', i)]
                    if static_mem in self.line[c]:
                        static_mem_found = True
                if not static_mem_found:
                    local_var_found = False
                    for local_var in local_vars:
                        indent = local_var[0]
                        local_var = local_var[1]
                        if indent <= self.get_num_indent(self.line[c]):
                            if self.line[c].strip().startswith(local_var + ' =') \
                                    or self.line[c].strip().startswith(local_var + '=') \
                                    or self.line[c].strip().startswith(local_var + ' -=')\
                                    or self.line[c].strip().startswith(local_var + ' +='):
                                local_var_found = True
                    if not local_var_found:
                        if self.line[c].find('.') == -1 or not self.line[c].find('.') < self.line[c].find('='):
                            self.line[c] = ' ' * self.get_num_indent(self.line[c]) + 'auto ' + self.line[c].lstrip()
                            local_vars.append((self.get_num_indent(self.line[c]),
                                               self.line[c][0:self.line[c].find('=')]
                                               .replace('auto ', '').replace('-', '').strip()))
                self.line[c] = self.line[c].replace(flag, '')
        return self.line

    def add_static_member_initializers(self):
        for c in range(0, len(self.line)):
            if 'main' in self.line[c]:
                self.line[c] = '{};\n'.format(';\n'.join([x for x in self.static_members])) + self.line[c]
        return self.line

    def get_default_initializer(self, typ):
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

    def get_replacements(self):
        for c in range(0, len(self.line)):
            if '#' not in self.line[c] and '#' not in self.line[c]:
                self.line[c] = self.line[c] \
                    .replace('self.', 'this->').replace('>()];', '>();') \
                    .replace('append', 'push_back').replace('pass', ';') \
                    .replace('" +', '" <<').replace('"+', ' << ').replace('+"', ' << "').replace('+ "', '<< "') \
                    .replace(';;;', ';').replace(';;', ';').replace('"<<', '" <<').replace('<<"', '<< "') \
                    .replace('vector<str>', 'vector<std::string>')\
                    .replace(' str(', ' std::to_string(').replace('(str(', '(std::to_string(')
                if 'std::cout <<' in self.line[c]:
                    self.line[c] = self.line[c]\
                        .replace(', "', '<< "').replace('",', '" <<').replace(", '", "<< '").replace("' ,", "' <<")
            else:
                if '#include' not in self.line[c]:
                    self.line[c] = self.line[c].replace('#', '//')
            if 'std::find(' not in self.line[c]:
                self.line[c] = self.line[c].replace("'", '"')
        return self.line

    def get_indented(self):
        indent_stack = []
        self.line.append('END')
        for c in range(0, len(self.line)):
            self.line[c] = self.line[c].rstrip()
            if self.line[c].strip() == '':
                self.line[c] = ''
            else:
                indent = self.get_num_indent(self.line[c])
                if indent and (not indent_stack or indent > indent_stack[-1]):
                    indent_stack.append(indent)
                    self.line[c] = (indent_stack[-1] - 4) * ' ' + '{\n' + self.line[c]
                elif indent_stack and indent < indent_stack[-1]:
                    while indent_stack and indent < indent_stack[-1]:
                        self.line[c - 1] += '\n' + (indent_stack[-1] - 4) * ' ' + '}'
                        del indent_stack[-1]
        self.line[-1] = self.line[-1].replace('END', '')
        line = '\n'.join(self.line).split('\n')
        return self.line

    def add_semicolon(self, c):
        not_in = lambda x: x not in self.line[c]
        yes_in = lambda x: not not_in(x)
        if self.line[c] and not_in('//') and not_in('if') and not_in('for') and not_in('class') and not_in('main'):
            if yes_in('=') or (not_in(';') and not_in('void')):
                if not ('{' in self.line[c] or '}' in self.line[c] and not_in('def') and not_in('class')):
                    if not_in('while('):
                        self.line[c] += ';'
        return self.line

    def instantiation(self, c):
        if self.entered_constructor:
            for clas in self.class_name:
                if clas in self.line[c] and '=' in self.line[c]:
                    if self.line[c].strip().endswith(']'):
                        i = len(self.line[c]) - len(self.line[c].lstrip())
                        vector = self.line[c].lstrip()
                        var_name = vector[0:vector.find(' ')]
                        vector = vector[vector.find('[') + 1:vector.find(']')]
                        vector = 'vector<{}>();'.format(vector)
                        spacer = ' ' * self.get_num_indent(self.line[c])
                        self.line[c] = '{}{} = {}'.format(spacer, var_name, vector)
                    else:
                        i = self.get_num_indent(self.line[c])
                        stack_init = self.line[c].lstrip()
                        var_name = stack_init[0:stack_init.find(' ')]
                        args = stack_init[stack_init.find('('):stack_init.find(')') + 1].strip()
                        try:
                            args = '' if args.strip()[1] == ')' else args
                            if 'this->' in self.line[c]:
                                raise TypeError('')
                            self.line[c] = i * ' ' + clas + ' ' + var_name + args + ';'
                        except IndexError:
                            self.line[c] = i * ' ' + var_name + ' = ' + 'std::vector<{}>();'.format(clas)
                        except:
                            pass
            return self.line
        else:
            return self.line

    def get_num_indent(self, line_c):
        for i in range(4 * 8, -1, -4):
            indent = ' ' * i
            if line_c.startswith(indent):
                return i
        return 0  # no indent

    def get_args(self, c):
        return [x.strip() for x in
                self.line[c].strip()[self.line[c].strip().find(','):-1][0:-1].split(',')[1::]]

    def get_type(self, x):
        if x.strip()[0] == '[' and x.strip()[-1] == ']':
            self.libs_to_add.add('vector')
            typ = x[x.find('[') + 1:x.find(']')].strip()
            return ['std::vector<{}>'.format(typ), self.libs_to_add]
        try:
            int(x)
            if '.' in x:
                return ['float', self.libs_to_add]
            else:
                return ['int', self.libs_to_add]
        except ValueError:
            for clas in self.class_name[1::]:
                if clas + '(' in x:
                    return [clas, self.libs_to_add]
            if '""' in x or "''" in x:
                self.libs_to_add.add('string')
                return ['std::string', self.libs_to_add]
            for clas in self.class_name:
                if clas in x:
                    return [clas, self.libs_to_add]
            return ['float', self.libs_to_add]
        except Exception:
            self.libs_to_add.add('string')
            return ['std::string', self.libs_to_add]

    def between(self, s, btw, a, b):
        """ return True if btw between a and b """
        s = s.replace('::', '')  # ignore std::, etc.
        ai = s.rfind(a)
        bi = s.rfind(b)
        btwi = s.rfind(btw)
        return True if btwi < bi and btwi > ai else False

    def get_assign_type(self, line_c):
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

    def get_time(self):
        return str(int(1000 * time()))

    def found_type(self, c2, vector_or_string):
        return c2 < 0 or \
               ((vector_or_string + '=' in self.line[c2] or vector_or_string + ' =' in self.line[c2]
                 or ' ' + vector_or_string + '(' in self.line[c2])
                and 'cout' not in self.line[c2] and '.find' not in self.line[c2]
                and '.append' not in self.line[c2] and '.size' not in self.line[c2]
                and 'len(' not in self.line[c2] and '#' not in self.line[c2]
                and vector_or_string + '[' not in self.line[c2][self.line[c2].find('=')::])
