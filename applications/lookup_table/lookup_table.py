import math
import random

cache = {}


# def slowfun(x, y):

#     v = math.pow(x, y)
#     if v not in cache:
#         cache[v] = math.factorial(v)
#         v = cache[v]
#     elif v in cache:
#         v = cache[v]
#     v //= (x + y)
#     v %= 982451653

#     return v

# Above is my solution, below is the lambda solution
# Below adds x and y in the cache, not v. Much more performant as x and y are the numbers we want
# v is simply a variable for operations performed on the numbers


def slowfun(x, y):
    # use a tuple to check for x and y
    if (x, y) not in cache:
        v = math.pow(x, y)  # return x raised to the power of y
        v = math.factorial(v)  # returns factorial of v as an integer
        v //= (x + y)  # floor division of v and x plus y
        # update x and y in the cache to v modulo
        cache[(x, y)] = v % 982451653
    return cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
