
PyCpp converts template code that is modeled 
after python syntax into C++ code by mapping directly.

Low level C++ instructions tranpiled and compiled, by only coding in a 
limited capability python environment. 

Quick Start

First, download:
- g++ compiler suite (cygwin, mingw, etc.)
- python

See lessons for example code that is tested to compile
and run. To do the same:
```bash
python build.py
``` 

Lessons:

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

To speed up developement, see in `build.py`:
```bash
# comment out to skip compiling lessons
transpile_and_compile('lessons')
```
