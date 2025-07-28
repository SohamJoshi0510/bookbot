from stats import get_word_count, get_char_count, sort_char_count
import sys

def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_count = sort_char_count(char_count)


    report = f'''
    ============ BOOKBOT ============
Analyzing book found at {path_to_book}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
'''
    print(report, end="")
    for element in sorted_char_count:
        if not element.get("name").isalpha():
            continue
        print(f"{element.get('name')}: {element.get('num')}")

main()