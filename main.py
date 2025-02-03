import sys
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)


if __name__ == "__main__":
    main(sys.argv[1])
