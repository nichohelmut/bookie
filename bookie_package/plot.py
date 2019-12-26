from scipy.optimize import curve_fit
import pandas as pd
import seaborn as sns
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import matplotlib.style as style
import datetime

def line_plot(df_result, labels, predictions,feature_list,test_features):
    # Dates of training values
    months = df_result[:, feature_list.index('Month')]
    days = df_result[:, feature_list.index('Day')]
    years = df_result[:, feature_list.index('Year')]

    # List and then convert to datetime object
    dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]
    dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]

    # Dataframe with true values and dates
    true_data = pd.DataFrame(data = {'date': dates, 'actual': labels})

    # Dates of predictions
    months = test_features[:, feature_list.index('Month')]
    days = test_features[:, feature_list.index('Day')]
    years = test_features[:, feature_list.index('Year')]

    # Column of dates
    test_dates = [str(int(year)) + '-' + str(int(month)) + '-' + str(int(day)) for year, month, day in zip(years, months, days)]

    # Convert to datetime objects
    test_dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in test_dates]

    # Dataframe with predictions and dates
    predictions_data = pd.DataFrame(data = {'date': test_dates, 'prediction': predictions})

    return true_data, predictions_data
    