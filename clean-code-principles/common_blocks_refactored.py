"""
Module for find_recent_coding_books function

Author: Marcelo
Date: April 2022
"""


def find_recent_coding_books(recent_books_pth, coding_books_pth):
    """
    Takes data from paths and retuns intersection containing
    recent_coding_boosk

    :param recent_books_pth: (str)
    :param coding_books_pth: (str)
    :return: recent_coding_books (set) books that are both paths
    """
    # open and read data form paths
    with open(recent_books_pth) as file_path_one:
        recent_books = file_path_one.read().split('\n')

    with open(coding_books_pth) as file_path_two:
        coding_books = file_path_two.read().split('\n')
    # finding intersection of paths to get recent coding books
    recent_coding_books = set(recent_books).intersection(coding_books)
    return recent_coding_books


if __name__ == '__main__':
    RECENT_CODING_BOOKS = find_recent_coding_books('books_published_last_two_years.txt',
                                                   'all_coding_books.txt')
    print(RECENT_CODING_BOOKS)
