
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
        self.a = [int]

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

        self.run_loop_test()
        self.run_vector_test()
        self.run_find_test()
        self.run_substring_test()

    def run_vector_test(self):
        a = [int]
        a.append(0)
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        a2 = a[0:3]
        print(a2[0], '= 0')

        b = [float]
        b.append(1)
        b.append(2)
        b.append(3)
        b.append(4)
        b2 = b[0:3]
        i0 = len(b2)
        b3 = b2[1:i0]
        print(b2[0], '= 1')
        print(b3[0], '= 2')
        print(len(b2), '= 3')

        a3 = [float]
        a3.append(0)
        a3.append(1)
        a3.append(2)
        a3.append(3)
        a4 = a3[0:1]
        i4 = len(a4)
        print(a4[i4], '= 0')

    def run_loop_test(self):
        c4 = 3
        while c4 > 0:
            print('c4:', c4)
            c4 -= 1

    def run_find_test(self):
        s3 = '0123456'
        i1 = s3.find('34')
        i2 = i1 + 1
        print(i2)
        i3 = s3.find('5')
        i4 = len(s3)
        s4 = s3[i3:i4]
        print(s4)

    def run_substring_test(self):
        s = "01234"
        s2 = s[0:3]
        print(s2[0], '= 0')

        s5 = '01234567'
        s6 = s5[0:6]
        s7 = s6[0:5]
        s8 = s7[0:4]
        print(s8, '= 0123')

if __name__ == '__main__':
    t = Test()
    t.run_all_tests()
    t.x3.append("hello")
    t.x3.append("world")
    print(t.x4.x)
