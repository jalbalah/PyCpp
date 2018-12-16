

class X:

    def __init__(self):
        print('Default initializer')

    def __init__(self, a, b):
        print('Another initializer')
        self.a = a
        self.b = b

if __name__ == '__main__':
    x0 = X()
    x1 = X(1, 2.0)
    print(x1.a)