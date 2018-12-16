

class X:

    def __init__(self):
        print("initializing, dude")

    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ == '__main__':
    x = X(1, 2.0)
    print(x.a)