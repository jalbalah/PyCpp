

class Cat:
    # this variable is shared between classes
    num_cats = 0

    def __init__(self):
        self.name = ''

        # increment shared variable
        num_cats = num_cats + 1


    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    c1 = Cat()
    c1.set_name('Pursippany')
    c2 = Cat()
    c2.set_name('MeowMeow')
    print(c1.name + ' says the number of cats is: ' + c1.num_cats)
    print(c2.name + ' says the number of cats is: ' + c2.num_cats)
