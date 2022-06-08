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

from pathlib import Path
import churn_library as cls

@pytest.fixture
def logger():
    logging.basicConfig(
        filename='./logs/churn_library.log',
        level=logging.INFO,
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s')


def test_import(logger):
    """
    test data import - this example is completed for you to assist with the other test functions
    """
    try:
        dataframe_raw = cls.import_data('data/bank_data.csv')
        logging.info('Raw dataframe fixture creation: SUCCESS')
    except FileNotFoundError as err:
        logging.info('The raw dataframe was not found')
        raise err

    try:
        assert dataframe_raw.shape[0] > 0
        assert dataframe_raw.shape[1] > 0
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't appear to have rows and columns")
        raise err


def test_eda(logger):
    """
    test perform eda function
    """
    try:
        dataframe_raw = cls.import_data('data/bank_data.csv')
        cls.perform_eda(dataframe_raw)
        logging.info('Testing perform_eda: SUCCESS')

        for image in ['Churn', 'correlation', 'Customer_Age', 'Marital_Status', 'Total_Trans_Ct']:
            path_img = 'images/eda/%s.jpg' % image
            with open(path_img, 'r'):
                img = Path(path_img)
                assert img.exists()
                logging.info('Opening %s image: SUCCESS' % image)
    except FileNotFoundError as err:
        logging.error('Testing EDA generated missing images')
        raise err


def test_encoder_helper(logger):
    """
    test encoder helper
    """
    dataframe_raw = cls.import_data('data/bank_data.csv')
    category_list = ["Gender",
                     "Education_Level",
                     "Marital_Status",
                     "Income_Category",
                     "Card_Category"]
    dataframe_encoded = cls.encoder_helper(dataframe_raw, category_list)
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


def test_perform_feature_engineering(logger):
    """
    test perform_feature_engineering
    """
    data = cls.import_data('data/bank_data.csv')
    category_list = ["Gender",
                     "Education_Level",
                     "Marital_Status",
                     "Income_Category",
                     "Card_Category"]
    X_train, X_test, y_train, y_test = cls.perform_feature_engineering(data, category_list)
    try:
        assert len(X_train) == len(y_train)
        assert len(X_test) == len(y_test)
        logging.info("Testing feature_engineering process and length of files: SUCCESS")

    except AssertionError as err:
        logging.error("Testing feature_engineering: Dataframe split length mismatch")
        raise err


def test_train_models(logger):
    """
    test train_models
    """
    data = cls.import_data('data/bank_data.csv')
    category_list = ["Gender",
                     "Education_Level",
                     "Marital_Status",
                     "Income_Category",
                     "Card_Category"]
    X_train, X_test, y_train, y_test = cls.perform_feature_engineering(data, category_list)
    cls.train_models(X_train, X_test, y_train, y_test)
    try:
        joblib.load('models/rfc_model.pkl')
        joblib.load('models/logistic_model.pkl')
        rfc_model = Path('models/rfc_model.pkl')
        lr_model = Path('models/logistic_model.pkl')
        assert rfc_model.exists()
        assert lr_model.exists()
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
    # for directory in ["logs", "images/eda", "images/results", "./models"]:
    #     files = glob.glob("%s/*" % directory)
    #     for file in files:
    #         os.remove(file)
    # sys.exit(pytest.main(["-s"]))
    test_import(logger)
    test_eda(logger)
    test_encoder_helper(logger)
    test_perform_feature_engineering(logger)
    test_train_models(logger)