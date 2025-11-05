def words_counter(string_content):
    splitted_book_content = string_content.split()
    words_num = len(splitted_book_content)
    return f"Found {words_num} total words"


def character_counter(string_content):
    splitted_book_content = string_content.split()
    symbols_dict = {}
    for word in splitted_book_content:
        word = word.lower()
        for char in word:
            if char in symbols_dict:
                symbols_dict[char] += 1
            else:
                symbols_dict[char] = 1

    return symbols_dict


