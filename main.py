def get_book_text(book_title):
    with open(f'books/{book_title}.txt', 'r', encoding="utf-8") as file:
        return file.read()


def main():
    book_text = get_book_text("frankenstein")
    print(book_text)


if __name__ == "__main__":
    main()
