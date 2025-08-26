from stats import get_num_words
from utils import get_book_text
from stats import get_num_characters


def main():
    num_words = get_num_words("frankenstein")
    print(f"{num_words} words found in the document")

    num_characters = get_num_characters("frankenstein")
    print(f"{num_characters} characters found in the document")


if __name__ == "__main__":
    main()
