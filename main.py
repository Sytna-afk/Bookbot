from stats import words_counter
from stats import character_counter
from stats import listing_dictionary
from stats import sort_list_dictionary
import sys

def get_book_text(txt_book_file):
    with open(txt_book_file, encoding = "utf-8") as file:
        txt_book_contents = file.read()
    return txt_book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1] #/home/sytna/Bookbot/books/frankenstein.txt
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}")
    text_content = get_book_text(path_to_book)
    #text_content is string variable with formated book text

    character_number = character_counter(text_content)
    #character_number is a dictionary with number of each character in book's text

    words_number = words_counter(text_content)
    #words_number is a f-string with number of words contained in string with book's text
    print(f"----------- Word Count ----------\n{words_number}")

    listed_dictionary = listing_dictionary(character_number)
    #listed_dictionary is a list of dictionaries. refer to character_number

    sorted_dictionary_list = sort_list_dictionary(listed_dictionary)
    # sorted_dictionary_list is a sorted list of dictionaries

    print("--------- Character Count -------")

    for index in sorted_dictionary_list:
        if index['char'].isalpha():
            print(f"{index['char']}: {index['num']}")

    print("============= END ===============")

main()
