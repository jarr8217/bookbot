from utils import get_book_text


def get_num_words(book_title):
    text = get_book_text(book_title)
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def get_sorted_char_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def get_num(d):
        return d["num"]
    char_list.sort(key=get_num, reverse=True)
    return char_list
