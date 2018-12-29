
# PyCpp
PyCpp converts template code that is modeled 
after python syntax into C++ code by mapping directly.

Low level C++ instructions tranpiled and compiled, by coding in a 
limited capability python environment. 

## Quick Start

First, download:
- g++ compiler suite (cygwin, mingw, etc.)
- python

See "Learning PyCpp" for example code that is tested to compile
and run.

Put your scripts into the "yourcode" directory. 
Then run:
```bash
python build.py yourcode
``` 

For tests, run:
```bash
python build.py tests
```

Any `.py` files in the folder passed as an argument to 
`build.py` will transpile and compile.

## Learning PyCpp:

hello world:  
`./lessons/lesson1`

classes:  
`./lessons/lesson2`

class members:  
`./lessons/lesson3`

static class members:  
`./lessons/lesson4`

lists and loops:  
`./lessons/lesson5`

strings and vectors:  
`./lessons/lesson6`

reading and writing files:  
`./lessons/lesson7`
