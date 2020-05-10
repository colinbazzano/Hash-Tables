

# def word_count(s):
#     words = {}
#     # split the words at a space line break
#     # words = [word for word in s.split(" ")]
#     # print("words", words)
#     if s == "":
#         return words
#     else:
#         for word in s.split(" "):
#             if word not in words:
#                 words[word] = 1
#             else:
#                 words[word] += 1
#         return words
# ignore special characters
# make it lowercase
# loop through and add count words

# above is me, below is solution documented by me

def word_count(s):
    # make a tranformation of the letters we dont want
    tr = str.maketrans("", "", '":;,.-+=/\\|[]{}()*^&')
    # make everything lower case
    s = s.translate(tr).lower()

    words = s.split()  # split the words
    counts = {}  # store the count of each word

    for w in words:
        if w not in counts:
            counts[w] = 1  # if it's not there, set the count to 1
        else:  # it IS there
            counts[w] += 1  # add 1 to the count
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
