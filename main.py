import sys
from collections import Counter

def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(count_words(file_contents))
    print(count_chars(file_contents))

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
