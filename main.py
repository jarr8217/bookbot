from stats import get_num_words
from utils import get_book_text
from stats import count_characters


def main():
    num_words = get_num_words("frankenstein")
    print(f"{num_words} words found in the document")

    book_text = get_book_text("frankenstein")
    char_counts = count_characters(book_text)
    print(f"Character counts found in the document: {char_counts}")


if __name__ == "__main__":
    main()
