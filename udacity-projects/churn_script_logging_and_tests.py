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


@pytest.fixture(name='dataframe_encoded')
def get_dataframe_encoded(dataframe_raw):
    """
    encoded dataframe fixture
    :param dataframe_raw:
    :return: dataframe encoded
    """
    try:
        category_list = ["Gender",
                         "Education_Level",
                         "Marital_Status",
                         "Income_Category",
                         "Card_Category"]
        df_encoded = cls.encoder_helper(dataframe_raw, category_list)
        logging.info('Encoded dataframe fixture creation: SUCCESS')
    except KeyError as err:
        logging.error('Fail to encode a column')
        raise err
    return df_encoded


@pytest.fixture(name='dataframe_split')
def make_feature_engineering(dataframe_encoded):
    """
    dataframe splitting fixture
    :param dataframe_encoded:
    :return: 4 datasets from the splitting process in train and test
    """
    try:
        category_list = ["Gender",
                         "Education_Level",
                         "Marital_Status",
                         "Income_Category",
                         "Card_Category"]
        X_train, X_test, y_train, y_test = cls.perform_feature_engineering(dataframe_encoded, category_list)
        logging.info('Feature Engineering feature: SUCCESS')
    except BaseException as err:
        logging.error('Mismatch in feature engineering fixture')
        raise err
    return X_train, X_test, y_train, y_test


def test_import(dataframe_raw):
    """
    test data import - this example is completed for you to assist with the other test functions
    """
    try:
        assert dataframe_raw.shape[0] > 0
        assert dataframe_raw.shape[1] > 0
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


def test_encoder_helper(dataframe_encoded):
    """
    test encoder helper
    """
    try:
        assert dataframe_encoded.shape[0] > 0
        assert dataframe_encoded.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing encoder_helper: The dataframe doesn't appear to have rows and columns")
        raise err
    try:
        column_list = ["Gender",
                       "Education_Level",
                       "Marital_Status",
                       "Income_Category",
                       "Card_Category"]
        for column in column_list:
            assert column in dataframe_encoded
    except AssertionError as err:
        logging.error("The dataframe doesn't have the right encoded columns")
        raise err
    logging.info("Testing encoder_helper: SUCCESS")
    return dataframe_encoded


def test_perform_feature_engineering(dataframe_split):
    """
    test perform_feature_engineering
    """
    try:
        X_train = dataframe_split[0]
        X_test = dataframe_split[1]
        y_train = dataframe_split[2]
        y_test = dataframe_split[3]
        assert len(X_train) == len(y_train)
        assert len(X_test) == len(y_test)
        logging.info("Testing feature_engineering process and length of files: SUCCESS")

    except AssertionError as err:
        logging.error("Testing feature_engineering: Dataframe split length mismatch")
        raise err
    return dataframe_split


def test_train_models(dataframe_split):
    """
    test train_models
    """
    cls.train_models(dataframe_split[0], dataframe_split[1], dataframe_split[2], dataframe_split[3])
    try:
        joblib.load('models/rfc_model.pkl')
        joblib.load('models/logistic_model.pkl')
        logging.info("Testing testing_models. Models were created: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing train_models: The models were not created")
        raise err
    for image in ["Logistic_Regression", "Random_Forest", "Feature_Importance"]:
        try:
            with open("images/results/%s.jpg" % image, 'r'):
                logging.info("Testing testing_models (report generation): SUCCESS")
        except FileNotFoundError as err:
            logging.error("Testing testing_models (report generation): The images were not found")
            raise err


if __name__ == "__main__":
    for directory in ["logs", "images/eda", "images/results", "./models"]:
        files = glob.glob("%s/*" % directory)
        for file in files:
            os.remove(file)
    sys.exit(pytest.main(["-s"]))
