# Strings

my_string = "abcdefg"

print(my_string[::3])  # third parameter indicates step out

print(my_string.upper())

x = 5
# print(f'{my_string} {x}') Python3
print("Item One: {}".format(my_string))

# List


def print_list(l, *args):
    print_str = "list "
    for item in args:
        print_str += f"{item}"
    print(f"{print_str}: {l}")


l = [1, 2, 3, 4]
print_list(l, "length: ", len(l))
l.append(5)
print_list(l, "appended list 5")
l.extend([6, 7])
print_list(l, "extended list [6,7]")
l.insert(0, -1)
print_list(l, "insert -1 to 0 index")
item = l.pop(0)
print(f"popped item from 0 index: {item}")
print_list(l, "after popped")
l.reverse()
print_list(l, "after reversed")
l.sort()
print_list(l, "after sorted")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print_list(matrix, "rows first item", first_col)

# Dictionaries

"""
dict.get(key)
dict[key]

dict[key] = value

dict.keys(), dict.values(), dict.items()

dict.pop(key), dict.popitem()

del dict[key] for specific key or del dict to del all

dict.clear() clear dict

dict.update(another_dict)
"""

# Tuples (Immutable)

"""
 t = (1,2,3)

 t.count(value)
 t.index(value)
"""

# Set(Unordered collections of unique elements)

"""

x = set() {}

x.add(item)

for item in x: can not access via index

x.update(list, tuple, set)

x.remove(item) // raise an error unless item exists
x.discard(item) // not raise an error when item does not exists

x.union(another_set)
"""

# Functions

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Lambda expressions


def even_bool(num): return (True if num % 2 == 0 else False)

# filter (filter items out of sequence applying condition)


evens = filter(even_bool, my_list)

print(list(evens))


# map (Apply same func to each element of sequence)

n = [4, 3, 2, 1]


def exp_two(num): return(num**2)


evens_map = map(exp_two, n)

print(list(evens_map))

# reduce (Apples same operation to irems of a sequence and uses result of operation as first param of next operation returns item not list)

from functools import reduce

def multiply(x, y): return x * y


reduce_n = reduce(multiply, n)

print(reduce_n)
