def main():
    book = "books/frankenstein.txt"
    text = read_book(book)
    #print(text)
    word_string = word_count(text)
    print(f"the book has {word_string} words")
    char_dict = char_count(text)
    char_list = dict_sort(char_dict)
    report = char_report(char_list)
    #print(char_list)
    print(report)

def dict_sort(word_dict):
    char_list = []
    sorted_dict = dict(sorted(word_dict.items()))
    for key,value in sorted_dict.items():
        new_dict = {}
        if key.isalpha():
            new_dict[key] = value
            char_list.append(new_dict)
    return char_list

def char_report(char_list):
    new_string = "\n \n"
    for item in char_list:
        for key,value in item.items():
            new_string += f"The letter {key} was used {value} times \n"
    return new_string

def word_count(string):
    count = string.split()
    return len(count)


def read_book(path):
    with open(path) as f:
        return f.read()

def char_count(book_path):
    characters = {}
    book_lower = book_path.lower()
    for letter in book_lower:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters

main()