from stats import words_counter

def get_book_text(txt_book_file):
    with open(txt_book_file, encoding = "utf-8") as file:
        txt_book_contents = file.read()
    return txt_book_contents

def main():
    text_content = get_book_text(r"/home/sytna/Bookbot/books/frankenstein.txt")

    print(words_counter(text_content))

main()
