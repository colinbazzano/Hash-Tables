import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()  # split the words
following = {}  # keeps track of all the words that can follow a word

prev = None

for w in words:  # for each word
    if prev is not None:
        # make an empty list for the first entries
        if prev not in following:
            following[prev] = []

        # add word to the list of those that are following
        following[prev].append(w)

    prev = w

# Words that we can start a sentence with

# We'll get clever and look for words where either the first letter is a
# capital, or the second is following a quote


def is_good_start(x): return x[0].isupper() or len(x) > 1 and x[1].isupper()


start_words = [w for w in following.keys() if is_good_start(w)]


# print a number of paragraphs
for _ in range(5):
    # choose starting word
    w = random.choice(start_words)

    stopped = False
    stop_punct = ".!?"  # stop on any of these

    while not stopped:
        print(w, end=" ")

        if w[-1] is stop_punct or len(w) > 1 and w[-2] in stop_punct:
            stopped = True
        else:
            # follow to the next word in chain
            next_words = following[w]
            w = random.choice(next_words)

    print("\n")
