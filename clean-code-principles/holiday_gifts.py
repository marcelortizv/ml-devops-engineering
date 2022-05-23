"""
A module to hold the compute_total_price function

Author: Marcelo
Date: May 21, 2022
"""

import time
import numpy as np


def compute_total_price(pth):
    """
    Take gift costs less than 25 calculate total price with tax
    :param pth: (str) path of the gifts_costs.txt
    :return: (float) total_price under 25 dollars + tax
    """

    with open(pth) as file_path:
        gift_costs = file_path.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    start = time.time()
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    print(total_price)
    print('Duration: {} seconds'.format(time.time() - start))

    return total_price


if __name__ == '__main__':
    TOTAL_PRICE_RESULT = compute_total_price('gift_costs.txt')
