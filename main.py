def main():
    book_path = "/home/casper/WORKSPACE/github.com/CasperD598/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict = get_num_apperance(text)
    print(f"{num_words} words found in the document")
    print(dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_apperance(text):
    Apperance_dict = {}
    text = text.lower()
    for character in text:
        if character in Apperance_dict:
            Apperance_dict[character] += 1
        else:
            Apperance_dict[character] = 1
    return Apperance_dict

main()