"""
Run Customer Churn modelling and save artifacts
File: churn_library.py
Author: Marcelo
Date: May 31 2022
"""

# import libraries
import os
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import roc_curve, classification_report

import shap
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


os.environ['QT_QPA_PLATFORM'] = 'offscreen'


def import_data(file_path):
    """
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    """
    data = pd.read_csv(file_path)
    # Create churn variable
    data['Churn'] = data['Attrition_Flag'].apply(lambda val: 0 if val == "Existing Customer" else 1)

    return data


def perform_eda(dataframe):
    """
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    """
    columns = ['Churn', 'Customer_Age', 'Marital_Status', 'Total_Trans_Ct', 'correlation']
    for col in columns:
        # making plot
        plt.figure(figsize=(20, 10))

        if col == 'Churn':
            dataframe[col].hist()
        elif col == "Customer_Age":
            dataframe[col].hist()
        elif col == 'Marital_Status':
            dataframe[col].value_counts('normalize').plot(kind='bar')
        elif col == 'Total_Trans_Ct':
            sns.histplot(dataframe['Total_Trans_Ct'], stat='density', kde=True)
        elif col == 'correlation':
            sns.heatmap(dataframe.corr(), annot=False, cmap="Dark2_r", linewidths=2)
        # saving figures
        plt.savefig('images/eda/%s.jpg' % col)
        plt.close()


def encoder_helper(df, category_lst):
    """
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with cell 15 from the notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features

    output:
            df: pandas dataframe with new columns for
    """
    for category in category_lst:
        category_serie = []
        category_groups = df.groupby(category).mean()['Churn']
        # fill values
        for row in df[category]:
            category_serie.append(category_groups.loc[row])
        df[f'{category}_Churn'] = category_serie
    return df


def perform_feature_engineering(df, category_lst):
    """
    input:
              df: pandas dataframe
              category_lst: list of columns that contain categorical features

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    """
    # apply encoder_helper
    df_encoded = encoder_helper(df, category_lst)

    keep_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book',
                 'Total_Relationship_Count', 'Months_Inactive_12_mon',
                 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
                 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
                 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
                 'Gender_Churn', 'Education_Level_Churn', 'Marital_Status_Churn',
                 'Income_Category_Churn', 'Card_Category_Churn'
                 ]

    y_df = df_encoded['Churn']
    x_df = df_encoded[keep_cols]

    # making split
    X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test


def classification_report_image(y_train,
                                y_test,
                                y_train_preds_lr,
                                y_train_preds_rf,
                                y_test_preds_lr,
                                y_test_preds_rf):
    """
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    """
    report_data = {
        'Logistic_Regression': ('Train Data LR', y_train, y_train_preds_lr,
                                'Test Data LR', y_test, y_test_preds_lr),
        'Random_Forest': ('Train Data RF', y_train, y_train_preds_rf,
                          'Test Data RF', y_test, y_test_preds_rf)
    }
    for key, classification_data in report_data.items():
        plt.rc('figure', figsize=(20, 10))
        plt.text(0.01, 1.25, str(classification_data[0]))
        plt.text(0.01, 0.05, str(classification_report(classification_data[1], classification_data[2])))
        plt.text(0.01, 0.6, str(classification_data[3]))
        plt.text(0.01, 0.7, str(classification_report(classification_data[4], classification_data[5])))
        plt.axis("off")
        plt.savefig("images/results/%s.jpg" % key)
        plt.close()

        # Plot the ROC curve
        fpr, tpr, _ = roc_curve(classification_data[4], classification_data[5])
        plt.figure(figsize=(20, 10))
        plt.plot(fpr, tpr)
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        plt.savefig("images/results/roc_curve_%s.jpg" % key)
        plt.close()


def feature_importance_plot(model, X_data, output_pth):
    """
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    """
    feature_importance = model.best_estimator_.feature_importances_
    indices = np.argsort(feature_importance)[::-1]
    names = [X_data.columns[i] for i in indices]

    plt.figure(figsize=(20, 5))
    plt.title("Feature Importance")
    plt.ylabel("Importance")
    plt.bar(range(X_data.shape[1]), feature_importance[indices])
    plt.xticks(range(X_data.shape[1]), names, rotation=90)
    plt.savefig("images/%s/Feature_Importance.jpg" % output_pth)
    plt.close()


def train_models(X_train, X_test, y_train, y_test):
    """
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    """
    rf = RandomForestClassifier(random_state=42)
    lr = LogisticRegression(solver='lbfgs', max_iter=3000)

    param_grid = {
        'n_estimators': [200, 500],
        'max_features': ['auto', 'sqrt'],
        'max_depth': [4, 5, 100],
        'criterion': ['gini', 'entropy']
    }

    # train random forest classifier
    cv_rfc = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
    cv_rfc.fit(X_train, y_train)

    # train logistic regression
    lr.fit(X_train, y_train)

    # make predictions
    y_train_preds_rf = cv_rfc.best_estimator_.predict(X_train)
    y_test_preds_rf = cv_rfc.best_estimator_.predict(X_test)

    y_train_preds_lr = lr.predict(X_train)
    y_test_preds_lr = lr.predict(X_test)

    # make classification reports
    classification_report_image(y_train,
                                 y_test,
                                 y_train_preds_lr,
                                 y_train_preds_rf,
                                 y_test_preds_lr,
                                 y_test_preds_rf)
    # make feature importance plots
    feature_importance_plot(cv_rfc, X_test, "results")

    # save the models
    joblib.dump(cv_rfc.best_estimator_, "models/rfc_model.pkl")
    joblib.dump(lr, "models/logistic_model.pkl")


if __name__ == '__main__':
    data = import_data('data/bank_data.csv')
    print('Performing EDA')
    perform_eda(data)
    category_list = ["Gender",
                     "Education_Level",
                     "Marital_Status",
                     "Income_Category",
                     "Card_Category"]
    X_train_, X_test_, y_train_, y_test_ = perform_feature_engineering(data, category_list)

    print('Training models')
    train_models(X_train_, X_test_, y_train_, y_test_)
