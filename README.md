
# PyCpp

![Transpiling](https://github.com/jalbalah/PyCpp/blob/master/pics/transpile.PNG)

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
To run the executable:
```bash
./yourcode/test
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

strings:  
`./lessons/lesson6`

reading and writing files:  
`./lessons/lesson7`

## Tips
PyCpp is easier if you understand two things:
1. declare variables as often as possible
2. name variables descriptively and use class members/functions for scope to avoid name conflicts

(2) will help with (1), which is a limitation of PyCpp.
Note: Declaring a variable, underneath, may leverage 
C++11/14 "auto" to compile while deducing type, and 
declaring a variable also defines the type of a list
or class, for example.   
