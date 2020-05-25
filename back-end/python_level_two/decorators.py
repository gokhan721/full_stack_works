"""
s = "GLOBAL VARIABLE!"

def func():
    mylocal = 10
    print(locals()) # local variablesables
    print(globals()) # global variables

func()
"""

"""
def hello(name = "Bambam"):
    print(f"hello() {name}")


    def greet():
        return "This string is inside greet()"


    def welcome():
        return "This string is inside welcome()"

    if name == "Bambam":
        return greet
    else:
        return welcome

x = hello()

print(x())
"""

# func decorators


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION NEEDS OF A DECORATOR")

# @new_decorator => func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()

# class decorators


class decorator:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print(f"Decorating {self.f.__name__}")
        self.f()


@decorator
def foo():
    print("inside foo()")


foo()


# memoization

def memoize(f):
    memo = {}

    def helper(x):
        print(f"x: {x}")
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib = fib(50)

print(fib)


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7))
