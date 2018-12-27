
# defining a C++ object X
class X:

    x = 0

    def __init__(self):
        pass

    def __init__(self, a, b):
        print('Another initializer')

        # initialize object member variables
        self.a = a
        self.b = b + 1

        # array with type passed (i.e. int, float, string)
        self.arr = [int]

    def junk(self):
        a = [int]

class Test:

    x2 = X(1, 2.0)
    x3 = [str]

    def __init__(self):
        self.arr = [X]
        self.x4 = X()

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


        f = open('tests/test.txt', 'w')
        f.write('hello\nworld')
        
        f2 = open('tests/test.txt', 'r').readlines()
        print("\n", f2[0])

        s = "01234"
        s2 = s[0:3]
        print(s2[0])

        a = [int]
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        a2 = a[0:3]
        print(a2[0])


if __name__ == '__main__':
    t = Test()
    t.run_all_tests()
    t.x3.append("hello")
    t.x3.append("world")
