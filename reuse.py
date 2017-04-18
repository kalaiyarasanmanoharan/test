

def func1():
    print "hello world"

def func2(arg1='San Francisco', arg2='Scottsdale', arg3='Sanjose'):
    print arg1,arg2,arg3

class MyClass(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

class NewClass(Myclass):
    def product(self):
        return self.x * self.y
