

from Transpile import Transpile

import os
import argparse
from pdb import set_trace as st


def transpile(python_files):
    for pyf in python_files:
        with open(pyf) as rf:
            tupl = Transpile(rf.readlines()).cpp  # rf.read().split('\n')
        with open(pyf.replace('.py', '.cpp'), 'w') as wf:
            wf.write(tupl)


def compile(python_file):
    name = python_file.replace('.py', '')
    build_cmd = 'g++ {}.cpp -o {} -g -O4 -std=c++14'.format(name, name)
    print(build_cmd)
    os.system(build_cmd)


def transpile_and_compile(folder, do_compile=True):
    py_files = get_py_files(paren_path, folder)
    # py_files = ['lessons/lesson1.py', 'tests/run_tests.py']
    transpile(py_files)
    if do_compile:
        for py_file in py_files:
            compile(py_file)


def test_generate_large_codebase():
    test_code = 'tests/run_tests.py'
    large_code = 'tests/run_large_code_base.py'
    if not os.path.exists(large_code):
        code = 'class X:\n'
        code += '    def __init__(self):\n'
        code += '        self.s = ""\n'
        code += '        self.n = 0\n'
        code += '        self.f = 0.0\n'
        code += '\n'
        with open(large_code, 'w') as wf:
            wf.write('int main() {\n}\n')
        with open(large_code, 'a') as wf:
            for i in range(0, 10000):
                wf.write(code.replace('X', 'X{}'.format(i)))

if __name__ == '__main__':
    source_files = {'Transpile.py', 'build.py'}

    # convert each non-source .py file to a .cpp file
    directory = lambda folder: os.path.join(os.getcwd(), folder)
    paren_path = lambda x, folder: os.path.join(folder, x)
    get_py_files = lambda parent_path, folder: \
        list(filter(None, ['' if (not x.endswith('.py') or x in source_files)
                           else parent_path(x, folder) for x in os.listdir(directory(folder))]))

    parser = argparse.ArgumentParser()
    parser.add_argument('foldername', default='')
    args = parser.parse_args()
    if args.foldername == 'lty':
        # comment out to skip compiling lessons
        transpile_and_compile('lessons')

        # test_generate_large_codebase()
        # transpile_and_compile('tests', do_compile=False)
        transpile_and_compile('tests')

        transpile_and_compile('yourcode')
    else:
        transpile_and_compile(args.foldername)

