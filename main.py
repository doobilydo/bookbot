#! /usr/env/python3

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    #print(get_number_of_words(text))
    print(num_of_words(text))
    
    
# Return text from a file.
def get_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# Return the number of words in the string.
def get_number_of_words(contents):
    words = contents.split()
    return (len(words))

# Return the count per unique word.
def num_of_words(contents):
    words = contents.split()
    num_words = {}

    for word in words:
        w = word.lower()
        if w not in num_words:
            num_words[w] = 1
        else:
            num_words[w] += 1
    
    return num_words



# Run.
main()