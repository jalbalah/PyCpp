
# defining a C++ object X
class X:

    x = 0

    def __init__(self, a, b):
        print('Another initializer')

        # initialize object member variables
        self.a = a
        self.b = b + 1

        # array with type passed (i.e. int, float, string)
        self.arr = [int]

class Test:
    def __init__(self):
        pass
    def run_all_tests(self):
        # instantiating C++ objects
        x1 = X(1, 2.0)
        print(x1.a, "\n")

        # range loop
        for i in range(10, 0, -1):
            print(i)
        print('liftoff!', '\n')

        for i in range(0, 10000):
            x1.arr.append(i)

        # iterator to loop through container
        for i in x1.arr:
            if i > 9995:
                print(i)

if __name__ == '__main__':
    t = Test()
    t.run_all_tests()
