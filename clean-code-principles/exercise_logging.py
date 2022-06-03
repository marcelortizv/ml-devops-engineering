"""
Logging exercise solution

author: Marcelo
date: May 31, 2021
"""

import logging

logging.basicConfig(
    filename='./results_exercise.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def sum_vals(first_val, second_val):
    '''
    Args:
        first_val: (int)
        second_val: (int)
    Return:
        first_val + second_val (int)
    '''
    try:
        logging.info("%s, %s", first_val, second_val)
        assert isinstance(first_val, int)
        assert isinstance(second_val, int)
        logging.info("SUCCESS: it looks like the values are ints")
        return first_val + second_val
    except AssertionError:
        logging.error("ERROR: it appears the values are not ints")


if __name__ == "__main__":
    sum_vals(4, 5)
    sum_vals('no', 'way')
