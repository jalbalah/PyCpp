
from pdb import set_trace as st

class Transpile:
    
    def __new__(cls, line):
        """ return tuple of .h and .cpp strings to write to file """
        h = ''
        cpp = ''

        indent_stack = []
        line.append('END')
        for c in range(0, len(line)):
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
        for c in range(0, len(line)):
            lstrip = line[c].strip().replace(' ', '')
            if lstrip.startswith('class'):
                class_name = line[c][line[c].find('class ') + 6:-1]
                line[c] = 'class {}'.format(class_name)
            elif lstrip.startswith('def__init__'):
                args = cls.get_args(line, c)
                line[c] = \
                    line[c][0:line[c].find('def')] \
                    + class_name \
                    + '(' + ','.join([str(x) for x in args]) + ')'
                if 'self' in line[c + 2]:
                    c += 2
                    while 'self' in line[c]:
                        line[c] = line[c].replace('self.', 'this->')
                        c += 1
            elif lstrip.startswith('def'):
                args = cls.get_args(line, c)
                func_name = line[c][line[c].find('def ') + 4:line[c].find('(')]
                line[c] = \
                    line[c][0:line[c].find('def')] \
                    + func_name \
                    + '(' + ','.join([str(x) for x in args]) + ')'


        h = '\n'.join(line)
        print(h)
        return [h, cpp]

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
