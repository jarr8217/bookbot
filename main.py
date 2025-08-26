from stats import get_num_words


def get_book_text(book_title):
    with open(f'books/{book_title}.txt', 'r', encoding="utf-8") as file:
        return file.read()


def main():
    book_text = get_book_text("frankenstein")
    num_words = get_num_words("frankenstein")
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
