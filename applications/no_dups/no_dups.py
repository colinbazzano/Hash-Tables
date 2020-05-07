cache = {}


def no_dups(s):
    for word in s.split(" "):
        if word not in cache:
            cache[word] = word

        return cache[word]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
