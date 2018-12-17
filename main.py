

from Transpile import Transpile

import os

if __name__ == '__main__':
    source_files = {'Transpile.py', 'main.py'}
    py_files = list(filter(None, ['' if (not x.endswith('.py') or x in source_files)
                                  else x for x in os.listdir(os.getcwd())]))

    # convert all non-source .py files to .cpp
    for pyf in py_files:
        with open(pyf) as rf:
            tupl = Transpile(rf.readlines())  # rf.read().split('\n')
        with open(pyf.replace('.py', '_out.cpp'), 'w') as wf:
            wf.write(tupl)

    build_cmd = 'g++ code_out.cpp -o code_out -g -O0'
    print(build_cmd)
    os.system(build_cmd)
