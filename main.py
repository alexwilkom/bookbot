def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    print_report(book_path, number_words, chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    chars = {}
    for char in text:
        char = char.lower()
        if not char in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    print("\n")
    for key, value in chars.items():
        if not key.isalpha():
            continue
        print(f"The '{key}' character was found {value} times")
    print("\n")
    print("--- End report ---")
    
main()