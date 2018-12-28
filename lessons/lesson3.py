

# a dog has properties and functions (things you can do with it)
class Dog:

    def __init__(self):

        # define name property
        self.name = ''
        self.weight = 0
        self.nicknames = [str]
        self.favorite_numbers = [int]

    def get_name(self):
        print('My name is ' + self.name)

    def get_weight(self):
        print('I weigh: ' + self.weight)

if __name__ == '__main__':
    d = Dog()
    d.name = 'john'
    d.weight = 40
    d.nicknames.append('funnybones')
    d.nicknames.append('ripcurrent')
    d.nicknames.append('bowman')
    d.favorite_numbers.append(7)
    d.favorite_numbers.append(23)

    d.get_name()
    d.get_weight()
    for fav_num in d.favorite_numbers:
        print(fav_num)
    for nickname in d.nicknames:
        print(nickname)
