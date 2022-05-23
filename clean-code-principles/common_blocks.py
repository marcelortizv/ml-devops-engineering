import time
import pandas as pd
import numpy as np


def find_recent_coding_books(recent_books_pth, coding_books_pth):
    with open(recent_books_pth) as f:
        recent_books = f.read().split('\n')

    with open(coding_books_pth) as f:
        coding_books = f.read().split('\n')

    recent_coding_books = set(recent_books).intersection(coding_books)
    return recent_coding_books


if __name__ == '__main__':
    recent_coding_books = find_recent_coding_books('books_published_last_two_years.txt',
                                                   'all_coding_books.txt')
    print(recent_coding_books)