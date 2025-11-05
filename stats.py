def words_counter(string_content):
    splitted_book_contents = string_content.split()
    words_num = len(splited_book_contents)
    return f"Found {words_num} total words"