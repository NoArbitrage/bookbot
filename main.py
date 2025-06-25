from stats import count_words,count_chars, sorted_list_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        char_count = count_chars(book_text)
        sorted = sorted_list_dicts(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        count_words(book_text)
        print("--------- Character Count -------")
        for item in sorted:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
main()