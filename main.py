def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = get_num_words(text)
    print(text[:1000])
    print(number_words)

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

main()