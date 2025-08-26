from stats import get_num_words
from utils import get_book_text


def main():
    book_text = get_book_text("frankenstein")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
