cache = {}


# def expensive_seq(x, y, z):
#     if x <= 0:
#         return y + z
#     if (x, y, z) not in cache:
#         cache[(x, y, z)] = expensive_seq(
#             x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
#     return cache[(x, y, z)]

# above is MY solution, below is the solution code from Lambda, documented by me
# Well, it seems very very similar, if not exactly the same as the solution code


def expensive_seq(x, y, z):
    if x <= 0:  # base case!
        return y + z  # we are returning the sum of y and z so we want to make sure we keep them up to date in the cache
    if (x, y, z) not in cache:  # if we don't have x,y,z in our cache
        # set the cache for each variable to the specified calculations
        cache[(x, y, z)] = expensive_seq(x - 1, y + 1, z) + \
            expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    # return the cache for each variable in a tuple
    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
