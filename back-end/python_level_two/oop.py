from math import pi


class A:
    pass


class B:
    pass


class AB(A, B):
    pass


ab = AB()

print(AB.mro())  # method resolution order


# multiple inheritance

class MA(object):
    def __init__(self, a):
        self.a = a
        print(f"MA: {a},dict: {self.__dict__}")


class MB(MA):
    def __init__(self, b, **kw):
        self.b = b
        print(f"before super MB:{kw}, dict: {self.__dict__}")
        super().__init__(**kw)
        print(f"after super MB:{kw}, dict: {self.__dict__}")


class MC(MA):
    def __init__(self, c, **kw):
        self.c = c
        print(f"before super MC:{kw},dict: {self.__dict__}")
        super().__init__(**kw)
        print(f"after super MC:{kw},dict: {self.__dict__}")


class MD(MB, MC):
    def __init__(self, a, b, c, d):
        super().__init__(a=a, b=b, c=c)
        self.d = d


print(MD.mro())
md = MD(1, 2, 3, 4)

# inheritance class casting examples


class Animal(object):
    def eat(self):
        print("Animal eating")


class Dog(Animal):
    def eat(self):
        print("Dog eating")


dog = Animal()
dog.eat()

dog.__class__ = Dog
dog.eat()


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def __repr__(self):
        return "Circle"


class CirclePlus(Circle):
    def diameter(self):
        return self.radius * 2

    def circumference(self):
        return self.radius * 2 * pi

    def __repr__(self):
        return "CirclePlus"


c = Circle(10)
print(c.radius)
print(c.area())
print(repr(c))

c.__class__ = CirclePlus
print(c.diameter())
print(c.circumference())
print(repr(c))

# Class attribute


class CC():
    pip = 3.14

    def area(self):
        print(CC.pip)


cc = CC()
cc.area()
