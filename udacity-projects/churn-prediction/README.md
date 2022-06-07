# Predict Customer Churn with Clean Code

## Project Introduction
In this project, you will identify credit card customers that are most likely to churn. 
The completed project will include a Python package 
for a machine learning project that follows coding (PEP8) and engineering best practices 
for implementing software (modular, documented, and tested). The package will also have 
the flexibility of being run interactively or from the command-line interface (CLI).

This project will give you practice using your skills for testing, logging, and best 
coding practices. 

One common question that Data Scientists need to deal is:
How do we identify (and later intervene with) customers who are likely to churn?

## Project Description
The churn_notebook.ipynb was already provided, which is a file containing the 
solution to identify credit card customers that are most likely to churn, 
but without implementing the engineering and software best practices.

My goal is to refactor the given churn_notebook.ipynb file following the 
best coding practices generating these files:

churn_library.py
churn_script_logging_and_tests.py
README.md

## Files and data description
`churn_library.py`: run the pipeline for training models and generate artifacts 

`churn_script_logging_and_tests.py` rin the tests for de training pipeline

`README.md`: instructions

* data
    * bank_data.csv
* images
    * eda
        * churn_distribution.png
        * customer_age_distribution.png
        * heatmap.png
        * marital_status_distribution.png
        * total_transaction_distribution.png
    * results
        * feature_importance.png
        * logistics_results.png
        * rf_results.png
        * roc_curve_result.png
* logs
    * churn_library.log
* models
    * logistic_model.pkl
    * rfc_model.pkl
* churn_library.py
* churn_notebook.ipynb
* churn_script_logging_and_tests.py
* README.md

## Running Files

First, you need to install the requirements:

`pip install -r requirements_py3.8.txt`

Second, you should run in terminal console

`python churn_library.py`

After the models were trained and artifacts generate, you can run the tests

`python churn_script_logging_and_test.py`
