

from pdb import set_trace as st



class Transpile:

    

    def __new__(cls, lines):

        """ return tuple of .h and .cpp strings to write to file """

        h = ''

        cpp = ''



        indent_stack = []

        for line in lines:

            indent = cls.get_num_indent(line)

            spacer = indent * ' '

            # print(indent)

            print(line)

            if indent and (not indent_stack or indent > indent_stack[-1]):

                indent_stack.append(indent)

                line = spacer + '{\n' + line

            elif indent_stack and indent < indent_stack[-1]:

                line = line + '\n' + spacer + '}'

                del indent_stack[-1]

            else:

                pass

                # print(indent)

                # print(indent_stack)

                # st()



        h = '\n'.join(lines)



        """

        class_name = ''

        for line in lines:

            if line.strip() == '':

                pass

            elif line.strip().startswith('class') and line.strip().endswith(':'):

                class_name = 'class {}'.format(line[line.find('class ') + 6:-1])

                h += '{}\n'.format(class_name)

                h += '{\n}\n'

            elif line.startswith

        """

        return [h, cpp]



    @staticmethod

    def get_num_indent(line):

        for i in range(8, -1, -4):

            indent = ' ' * (i + 1)

            if line.startswith(indent):

                return i + 1

        return 0  # no indent
