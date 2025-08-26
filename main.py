def get_book_text(book_title):
    with open(f'books/{book_title}.txt', 'r', encoding="utf-8") as file:
        return file.read()


def count_words(book_title):
    text = get_book_text(book_title)
    words = text.split()
    return len(words)


def main():
    book_text = get_book_text("frankenstein")

    word_count = count_words("frankenstein")
    print(f"Word count: {word_count}")


if __name__ == "__main__":
    main()
