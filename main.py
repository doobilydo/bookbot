#! /usr/env/python3

def main():
    path_to_file = "books/frankenstein.txt"
    print(get_number_of_words(path_to_file))
    
    
    
# Return the number of words in the string.
def get_number_of_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    return (len(words))


# Run.
main()