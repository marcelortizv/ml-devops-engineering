# Exploratory Data Analysis

For a good EDA you need intuition and creativity, so it is not possible
to define a complete recipe. However, some things to look at are:

* Understand what each feature means
* Univariate analysis to verify that our expectation on that feature matches reality
* Bivariate analysis where we look for correlations
* Anomaly detection
* Missing values handling


## Execute and Track an EDA in jupyter

Even though the EDA is an interactive step, we want to make it reproducible and 
to track it. A simple strategy to accomplish this is:

* Write an MLflow component that installs Jupyter and all the libraries that we need,
and execute the EDA as a notebook from within this component
* Embed plots and comments into the Jupyter notebook itself
* Track inputs and outputs of the notebook with your artifact tracking, in our case
Weights & Biases
  
Tracking a notebook in W&B is as simple as adding the save_code=True option when
creating the run:

````python
run = wandb.init(
  project="my_exercise",
  save_code=True
)

import pandas_profiling
import pandas as pd

df = pd.read_parquet("genres_mod.parquet")
profile = pandas_profiling.ProfileReport(df)
profile.to_widgets()
````

## Pre-processing is limited in scope

All pre-processing that is needed on both the offline, and the online data MUST GO 
in the inference pipeline.

Example of operations that should typically NOT be part of this pre-processing
step:
* Categorical encoding
* Missing Value imputation when the feature could be also missing in production
* Dimensionality reduction

### Feature Store

A tool to achieve dev/prod symmetry. It provides a centralized implementation
of the features and it serves them at training and at inference time.

![feature_store](https://video.udacity-data.com/topher/2021/June/60b8953c_feature-store/feature-store.png)

# Data Validation

We perform data validation in order to verify that our assumptions about 
the data are correct and stay correct even for new datasets. This latter 
point is not guaranteed. Indeed, the data can change for many reasons:

* Bugs are introduced upstream (for example in ETL pipelines)
* Changes in the source of the data are not communicated properly and produce
  unexpected changes in the input data
* The world changes and the distribution of the input data changes

## Deterministic Tests
A data test is deterministic when it verifies attributes of the data 
that can be measured without uncertainty. Some examples are:
* Number of columns in a dataset
* Length of the dataset
* Distinct values in a categorical variable
* Legal range for a numerical variable (for example, length > 0)
* Location for a geographic model

## Non-Deterministic Tests
It is non-deterministic when it involves measuring a quantity with
intrinsic uncertainty (random variable). It uses statistical hypothesis.
Some examples are:
* Mean and std dev of columns
* Correlations between columns, and columns with target
* Distribution of values within a column
* Outliers
