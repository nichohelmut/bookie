import pandas as pd
import numpy as np
import scipy 
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

def random_forrest(
    X_train, y_train,n_estimators=1000,random_state = 42, min_samples_split=2, max_leaf_nodes=None, max_features='auto', max_depth=None, bootstrap=True
    ):
    # making the RandomForestRegressor paramteres changable for hyperparameter optimization
    # as found here: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
    regr = RandomForestRegressor(
        n_estimators = n_estimators, 
        random_state = random_state, 
        min_samples_split=min_samples_split, 
        max_leaf_nodes=max_leaf_nodes,
        max_features=max_features,
        max_depth=max_depth,
        bootstrap=bootstrap
        )

    regr.fit(X_train, y_train)
    return regr

def random_search(X_train,y_train, n_estimators=1000, n_iter=10, cv=3):
    # creating the parameter grid with variables
    param_grid = {
        'n_estimators': np.linspace(10, n_estimators).astype(int),
        'max_depth': [None] + list(np.linspace(3, 20).astype(int)),
        'max_features': ['auto', 'sqrt', None] + list(np.arange(0.5, 1, 0.1)),
        'max_leaf_nodes': [None] + list(np.linspace(10, 50, 500).astype(int)),
        'min_samples_split': [2, 5, 10],
        'bootstrap': [True, False]
    }

    # RandomForestClassifier selected as estimator
    clf = RandomForestClassifier(random_state = 42)

    # create randomized search 
    # as described here: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
    rscv = RandomizedSearchCV(clf, param_grid, n_jobs = -1, cv = cv, 
                            n_iter = n_iter, verbose = 1, random_state=42)

    # refit 
    rscv.fit(X_train,y_train)
    return rscv

def performance_accuracy(y_test,X_test, regr):
    """
    input:
        y_test
        X_test
        regr = random forest regressor
    output:
        Mean Absolute Error(MAE)
        regr Accuracy
    """
    errors = abs(abs(np.round(regr.predict(X_test),0)) - y_test)
    accuracy = (errors==0).sum() / len(errors) * 100

    print('MAE:', round(np.mean(errors),2), 'Goals.')
    print('regr Accuracy:', round(accuracy, 2), '%.')    