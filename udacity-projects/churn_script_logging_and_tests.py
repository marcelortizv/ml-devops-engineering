"""
Module for test the correct performance of churn_library.py
Author: Marcelo
Date: May 31 2022
"""

import os
import logging
import sys
import glob

import pytest
import joblib

import churn_library as cls

logging.basicConfig(
    filename='./logs/churn_library.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

@pytest.fixture(name='dataframe_raw')
def get_dataframe_raw():
    """
    dataframe raw fixture
    :return: initial dataframe
    """
    try:
        dataframe_raw = cls.import_data('data/bank_data.csv')
        logging.info('Raw dataframe fixture creation: SUCCESS')
    except FileNotFoundError as err:
        logging.info('The raw dataframe was not found')
        raise err

    return dataframe_raw

def test_import(import_data):
    """
    test data import - this example is completed for you to assist with the other test functions
    """
    try:
        df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")

    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't appear to have rows and columns")
        raise err


def test_eda(dataframe_raw):
    """
    test perform eda function
	"""
    try:
        cls.perform_eda(dataframe_raw)
        logging.info('Testing perform_eda: SUCCESS')

        for image in ['Churn', 'correlation', 'Customer_Age', 'Marital_Status', 'Total_Trans_Ct']:
            with open('images/edad/%s.jpg' % image, 'r'):
                logging.info('Opening %s image: SUCCESS' % image)
    except FileNotFoundError as err:
        logging.error('Testing EDA generated missing images')
        raise err


def test_encoder_helper(encoder_helper):
    """
    test encoder helper
    """



def test_perform_feature_engineering(perform_feature_engineering):
    """
	test perform_feature_engineering
	"""


def test_train_models(train_models):
    """
	test train_models
	"""


if __name__ == "__main__":
    pass
