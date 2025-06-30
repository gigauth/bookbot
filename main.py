from stats import count_words, count_characters, sort_characters
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    book_text = get_book_text(path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    characters = count_characters(book_text)
    sorted_characters = sort_characters(characters)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
