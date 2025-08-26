def get_book_text(book_title):
    with open(f'books/{book_title}.txt', 'r', encoding="utf-8") as file:
        return file.read()


def main():
    book_title = input(
        "Enter the book title (e.g., 'frankenstein'): ").strip().lower()
    book_text = get_book_text(book_title)
    print(book_text)


if __name__ == "__main__":
    main()
