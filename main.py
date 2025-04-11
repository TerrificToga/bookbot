from stats import number_of_words, character_count, sorted_characters
import sys
import os

def get_book_text(path):
    with open(path) as p:
        book = p.read()
    return book


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print("Not a valid path")
        sys.exit(1)
    book_to_analyze = sys.argv[1]
    book_text = get_book_text(book_to_analyze)
    answer = number_of_words(book_text)
    character = character_count(book_text)
    sorted_list = sorted_characters(character)
    print("============BOOKBOT============")
    print(f"Analyzing book found at {book_to_analyze}")
    print("----------- Word Count ----------")
    print("Found " + str(answer) + " total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()    
