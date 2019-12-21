from scipy.optimize import curve_fit
import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import matplotlib.style as style
import itertools
from sklearn.linear_model import LogisticRegression
import sys

def avg_goal_diff(df, avg_h_a_diff, a_h_team, a_h_goal_diff):
    df[avg_h_a_diff] = 0
    avg_per_team = {}
    all_teams = df[a_h_team].unique()
    for t in all_teams:
        df_team = df[df[a_h_team]==t].fillna(0)
        result = df_team['{}TGDIFF'.format(a_h_goal_diff)].rolling(10).mean()
        df_team[avg_h_a_diff] = result.shift(-9)
        avg_per_team[t] = df_team
    return avg_per_team

def avg_goals(df,h_or_a_avg, h_or_a_team, h_or_a_letter):
    df[h_or_a_avg] = 0
    avg_goals_team = {}
    all_teams = df[h_or_a_team].unique()
    for t in all_teams:
        df_team = df[df[h_or_a_team]==t].fillna(0)
        result = df_team['FT{}G'.format(h_or_a_letter)].rolling(10).mean()
        df_team[h_or_a_avg] = result.shift(-9)
        avg_goals_team[t] = df_team
    return avg_goals_team

def from_dict_value_to_df(d):
    """
    input = dictionary 
    output = dataframe as part of all the values from the dictionary
    """
    df = pd.DataFrame()
    for v in d.values():
        df = df.append(v)
    return df

def previous_data(df, h_or_a_team, column):
    d = dict()
    team_with_past_dict = dict()
    all_teams = df[h_or_a_team].unique()
    for team in all_teams:
        n_games = len(df[df[h_or_a_team]==team])
        team_with_past_dict[team] = df[df[h_or_a_team]==team]
        for i in range(1, n_games):
            d[i] = team_with_past_dict[team].assign(
                result=team_with_past_dict[team].groupby(h_or_a_team)[column].shift(-i)
            ).fillna({'{}_X'.format(column): 0})
            team_with_past_dict[team]['{}_{}'.format(column, i)] = d[i].result
    return team_with_past_dict