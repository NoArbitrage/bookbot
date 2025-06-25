from stats import count_words,count_chars, sorted_list_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    char_count = count_chars(book_text)
    sorted = sorted_list_dicts(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()