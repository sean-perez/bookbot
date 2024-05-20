from collections import Counter

def main(path_to_file):


    def count_chars(file_contents):
        return dict(Counter(file_contents.lower()))


    def count_words(text):
        return len(text.split())


    def get_value(item):
        return item[1]


    def generate_report(path_to_file, word_count, sorted_chars):
        heading = f"--- Begin report of {path_to_file} ---"
        print(f"{heading}\n{word_count} words found in the document\n")

        for key, value in sorted_chars.items():
            print(f"The '{key}' character was found {value} times")

        print("--- End report ---")


    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    
    alpha_chars = {key: char_count[key] for key in char_count if key.isalpha()}
    sorted_chars = dict(sorted(alpha_chars.items(), key=get_value, reverse=True))

    generate_report(path_to_file, word_count, sorted_chars)


main("books/frankenstein.txt")