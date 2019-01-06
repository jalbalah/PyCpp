

class X:

    def __init__(self, name):
        self.name = ''
        self.set_name(name)

    def set_name(self, name):
        self.name = name

    def __str__(self):
        print(self.name)

if __name__ == '__main__':
    x = X('dan')
    x.__str__()
