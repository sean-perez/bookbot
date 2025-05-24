
def get_num_words(words):
    return len(words.split())

def character_count(text):
    char_count = {}    
    lowercase_text = text.lower()
    char_set = set(lowercase_text)

    for char in char_set:
        char_count[char] = lowercase_text.count(char)
    return char_count

def most_common(chars_count):
    return [{key: value} for key, value in sorted(
        chars_count.items(), 
        key=lambda x: x[1], 
        reverse=True
    ) if key.isalpha()]
