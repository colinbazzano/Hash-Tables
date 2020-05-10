# taken from word count
def word_count(s):
    tr = str.maketrans("", "", '":;,.-+=/\|[]{}()*^&')
    s = s.translate(tr).lower()

    words = s.split()  # split the words
    counts = {}  # track the counts of words

    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

    return counts


# read in the file
with open("robin.txt") as f:
    d = f.read()

# get al the counts items

counts = list(word_count(d).items())

# figure out the longest word
max_len = 0
for c in counts:
    ln = len(c[0])  # length of first item
    if ln > max_len:
        max_len = ln  # if there's something longer set it to that

# sort everything based on count first, then alphabetical
counts.sort(key=lambda e: (-e[1], e[0]))

# print it all out
for c in counts:
    print(f"{c[0]:{max_len}}  ", end="")
    for _ in range(c[1]):
        print(f"#", end="")

    print()
