from scipy.optimize import curve_fit
import pandas as pd
import seaborn as sns
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import matplotlib.style as style
import itertools
from sklearn.linear_model import LogisticRegression
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

def random_forrest(
    train_features, train_labels,n_estimators=1000,random_state = 42, min_samples_split=2, max_leaf_nodes=None, max_features='auto', max_depth=None, bootstrap=True
    ):
    # Instantiate model 
    rf = RandomForestRegressor(
        n_estimators = n_estimators, 
        random_state = random_state, 
        min_samples_split=min_samples_split, 
        max_leaf_nodes=max_leaf_nodes,
        max_features=max_features,
        max_depth=max_depth,
        bootstrap=bootstrap
        )

    # Train the model on training data
    rf.fit(train_features, train_labels)
    return rf

def random_search(train_features,train_labels, n_estimators=1000, n_iter=10, cv=3):
    # Hyperparameter grid
    param_grid = {
    'n_estimators': np.linspace(10, n_estimators).astype(int),
        'max_depth': [None] + list(np.linspace(3, 20).astype(int)),
        'max_features': ['auto', 'sqrt', None] + list(np.arange(0.5, 1, 0.1)),
        'max_leaf_nodes': [None] + list(np.linspace(10, 50, 500).astype(int)),
        'min_samples_split': [2, 5, 10],
        'bootstrap': [True, False]
    }

    # Estimator for use in random search
    estimator = RandomForestClassifier(random_state = 42)

    # Create the random search model
    rs = RandomizedSearchCV(estimator, param_grid, n_jobs = -1, cv = cv, 
                            n_iter = n_iter, verbose = 1, random_state=42)

    # Fit 
    rs.fit(train_features,train_labels)
    return rs
