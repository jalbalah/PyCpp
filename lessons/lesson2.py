
# this is called a class
class Square:
    def __init__(self):
        print('I am a square')

# this is another class
class Rectangle:
    def __init__(self, attitude):
        print('I am a ' + attitude + ' circle')

if __name__ == '__main__':
    # create a square object
    s = Square()

    # create a rectangle, and pass in an argument
    r = Rectangle('funny')
