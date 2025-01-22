def main():
    with open("/home/casper/WORKSPACE/github.com/CasperD598/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(txt):
    words = txt.split()
    number = 0
    for word in words:
        number += 1
    return number

content = main()
word_number = count_words(content)
print(word_number)
