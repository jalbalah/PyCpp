

from Transpile import Transpile

import os

if __name__ == '__main__':
    source_files = {'Transpile.py', 'main.py'}
    py_files = list(filter(None, ['' if (not x.endswith('.py') or x in source_files)
                                  else x for x in os.listdir(os.getcwd())]))


    for pyf in py_files:
        with open(pyf) as rf:
            tupl = Transpile(rf.readlines())
        with open(pyf.replace('.py', '.cpp'), 'w') as wf:
            wf.write(tupl)

    for f in py_files:
        build_cmd = 'g++ {} -o {}'.format(f.replace('.py', '.cpp'), f.replace('.py', ''))
        print(build_cmd)
        # os.system(build_cmd)
