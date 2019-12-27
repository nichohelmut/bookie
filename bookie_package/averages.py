import pandas as pd
import sys

def avg_goal_diff(df, avg_h_a_diff, a_h_team, a_h_goal_letter):
    """
    input: 
        df = dataframe with all results
        avg_h_a_diff = name of the new column
        a_h_team = HomeTeam or AwayTeam
        a_h_goal_letter = 'H' for home or 'A' for away
    output: 
        avg_per_team = dictionary with with team as key and columns as values with new column H/ATGDIFF
    """
    df[avg_h_a_diff] = 0
    avg_per_team = {}
    all_teams = df[a_h_team].unique()
    for t in all_teams:
        df_team = df[df[a_h_team]==t].fillna(0)
        result = df_team['{}TGDIFF'.format(a_h_goal_letter)].rolling(10).mean()
        df_team[avg_h_a_diff] = result.shift(-9)
        avg_per_team[t] = df_team
    return avg_per_team

def avg_goals(df,h_or_a_avg, h_or_a_team, h_or_a_letter):
    """
    input: 
        df = dataframe with all results
        h_or_a_avg = name of the new column
        a_h_team = HomeTeam or AwayTeam
        a_h_goal_letter = 'H' for home or 'A' for away
    """
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
    """
    input: 
        df = dataframe with all results
        a_h_team = HomeTeam or AwayTeam
        column = column selected to get previous data from
    output:
        team_with_past_dict = dictionary with team as a key and columns as values with new 
                              columns with past value
    """
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
    