import sys
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)
    print(count_words(file_contents))


def count_words(book_string):
    return len(book_string.split())

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("books/frankenstein.txt")
