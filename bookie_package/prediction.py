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
