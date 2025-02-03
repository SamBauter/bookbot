import sys
from collections import Counter
import string

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    print(f"---Begin report of {path_to_file} ---")
    print(f"{count_words(file_contents)} found in the document")
    char_count_dict = count_chars(file_contents)
    filtered_char_count_dict = {char:count for char,count in char_count_dict.items() if char in list(string.ascii_lowercase) }
    for char,count in filtered_char_count_dict.items():
        print(f"The '{char}' character was found {count} times")

def count_chars(book_string):
    book_string_lower = book_string.lower()
    return dict(Counter(book_string_lower))


def count_words(book_string):
    return len(book_string.split())

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("books/frankenstein.txt")
