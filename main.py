from stats import count_words
from stats import count_characters
from stats import sort_characters_by_frequency
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_char_count = sort_characters_by_frequency(char_count)

    print(f"Found {word_count} total words.")
    print("Character frequencies (sorted):")
    for char, freq in sorted_char_count:
        print(f"  {char}: {freq}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()