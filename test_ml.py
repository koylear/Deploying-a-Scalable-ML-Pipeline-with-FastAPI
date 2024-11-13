import pytest
# TODO: add necessary import
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.model import train_model
from train_model import train, test, data, X_train, y_train
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_size(): #test_one():
    """
    Ensure datasets are correct size for testing
    """
    file_path = './data/census.csv'
    dataset = pd.read_csv(file_path)
    train, test = train_test_split(dataset, test_size = 0.2)
    assert len(test) >= 2000


# TODO: implement the second test. Change the function name and input as needed
def test_columns(): #test_two():
    """
    Ensure all columns are present
    """
    file_path = './data/census.csv'
    dataset = pd.read_csv(file_path)

    col_names = {
        'age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    }

    assert set(dataset.columns) == col_names


# TODO: implement the third test. Change the function name and input as needed
def test_rf_model(): #test_three():
    """
    Ensure ccorrect algorithm is being used
    """
    rfmodel = train_model(X_train, y_train)
    assert type(rfmodel) == type(RandomForestClassifier())
