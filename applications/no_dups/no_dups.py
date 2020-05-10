# cache = {}


# def no_dups(s):
#     for word in s.split(" "):
#         if word not in cache:
#             cache[word] = word

#         return cache[word]

# Below is my unfinished version, below is solution
# documented by me

def no_dups(s):
    words = s.split()  # split the words, it is a list

    seen = {}  # words we have seen
    result = []  # return to show the words without duplicates

    for w in words:  # for each word in the list
        if w not in seen:  # if we haven't seen it yet
            result.append(w)  # add it to the result
            seen[w] = True  # set this to true so we won't append it again
    # returns them as a string rather a list with each string in it
    return " ".join(result)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
