

# a dog has properties and functions (things you can do with it)
class Dog:

    def __init__(self):

        # define name property
        self.name = ''
        self.weight = 0

    def set_name(self, new_name):
        self.name = new_name

    def set_size(self, weight):
        self.weight = weight

    def get_name(self):
        print('My name is ' + self.name)

    def get_weight(self):
        print('I weight' + self.weight)

if __name__ == '__main__':
    x = Dog()
    x.set_name('john')
    x.set_size(40)
    x.get_name()
    x.get_weight()
