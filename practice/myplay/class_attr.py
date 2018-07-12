


class Person(object):
    def __init__(self):
        self.name = 'laowang'
        self.age = 18
        print(self)


if __name__ == '__main__':
    a = Person()
    
    print(dir(a))