

def word_count(s):
    words = {}
    # split the words at a space line break
    # words = [word for word in s.split(" ")]
    # print("words", words)
    if s == "":
        return words
    else:
        for word in s.split(" "):
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        return words
    # ignore special characters
    # make it lowercase
    # loop through and add count words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
