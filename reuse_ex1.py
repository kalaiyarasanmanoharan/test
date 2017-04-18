

def func1():
    print "hello world"

def func2(arg1='San Francisco', arg2='Scottsdale', arg3='Sanjose', arg4=None):
    if arg4 == None:
        print arg1, arg2, arg3
    else:
        print arg1, arg2, arg3, arg4

class MyClass(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

class NewClass(MyClass):
    def product(self):
        return self.x * self.y

def main():
    print "This is the __name__ value: {}".format(__name__)

if __name__ == "__main__":
    main()
    print "This module does something"
