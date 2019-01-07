

class Cat:
    # this variable is shared between classes
    num_cats = 0

    def __init__(self, name):
        self.name = ''
        self.set_name(name)
        # increment shared variable
        num_cats = num_cats + 1

    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    c1 = Cat('Pursippany')
    print(c1.name, 'says the number of cats is:', c1.num_cats)
    c2 = Cat('MeowMeow')
    print(c2.name, 'says the number of cats is:', c2.num_cats)
