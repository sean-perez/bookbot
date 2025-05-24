
import sys

from stats import get_num_words, character_count, most_common

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()

    return file_contents

def main():
    text = get_book_text(book)
    num_words = get_num_words(text)
    char_count = character_count(text)
    results = most_common(char_count)
    return num_words, results
    

total_words, results = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for i in results:
    for k, v in i.items():
        print(f"{k}: {v}")
print("============= END ===============")