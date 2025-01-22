def main():
    book_path = "/home/casper/WORKSPACE/github.com/CasperD598/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict = get_num_apperance(text)
    char_list = list(dict.items())
    char_list.sort(reverse=True, key=sort_on)
    alpha_list = only_alpha(char_list)
    
    print_report(alpha_list, book_path, num_words)

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

def sort_on(dict):
    return dict[1]

def only_alpha(listt):
    sorted_list = []
    for item in listt:
        if item[0].isalpha():
            sorted_list.append(item)
    return sorted_list

def print_report(list, path, num_words):
    print(f"--- Begin report of {path[53:]} ---")
    print(f"{num_words} words found in the document")
    for item in list:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")

main()