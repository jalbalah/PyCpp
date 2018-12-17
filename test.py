
# defining a C++ object X
class X:

    def __init__(self, a, b):
        print('Another initializer')
        # initialize object member variables
        self.a = a
        self.b = b + 1
        # array with type passed (i.e. int, float, string)
        self.arr = [int]

if __name__ == '__main__':
    # instantiating C++ objects
    x1 = X(1, 2.0)
    print(x1.a)
    for i in range(0, 10):
        print(i)
    print('liftoff!')
