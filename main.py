from stats import get_num_words, count_characters, get_sorted_char_list
from utils import get_book_text
import sys


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    num_words = get_num_words(book_path)
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    book_text = get_book_text(book_path)
    char_counts = count_characters(book_text)
    sorted_char_list = get_sorted_char_list(char_counts)
    for entry in sorted_char_list:
        print(f'{entry['char']}: {entry['num']}')
    print('============= END ==============')


if __name__ == '__main__':
    main()
