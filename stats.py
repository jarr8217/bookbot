from main import get_book_text


def get_num_words(book_title):
    text = get_book_text(book_title)
    words = text.split()
    return len(words)
