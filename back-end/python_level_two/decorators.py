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
