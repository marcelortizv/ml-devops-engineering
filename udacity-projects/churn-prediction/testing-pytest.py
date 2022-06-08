import os
import logging
import pytest
#import churn_library_solution as cls
from churn_library import import_data


@pytest.fixture
def logger():
    logging.basicConfig(
        filename='./logs/churn_library_test.log',
        level=logging.INFO,
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s')


def test_import(logger):
    """
    test data import - this example is completed for you to assist with the other test functions
    """
    try:
        df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import data: The file wasn't found")
        raise err
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err