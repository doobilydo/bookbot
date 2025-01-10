#! /usr/env/python3

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text(path_to_file)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{get_number_of_words(text)} words found in the document")
    
    chars = num_of_characters(text)
    for key in chars:
        print(f"The '{key}' character was found {chars[key]}")

    print("--- End report ---")
    
    
# Return text from a file.
def get_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# Return the number of words in the string.
def get_number_of_words(contents):
    words = contents.split()
    return len(words)

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
# Return the count per unique character.
def num_of_characters(contents):
    words = contents.split()
    num_characters = {}

    for word in words:
        for letter in word:
            l = letter.lower()
            if l.isalpha():
                if l not in num_characters:
                    num_characters[l] = 1
                else:
                    num_characters[l] += 1
    
    return num_characters



# Run.
main()