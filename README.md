### Table of Contents

1. [Installation](#installation)
2. [Instructions](#instructions)
2. [Project Motivation](#motivation)
3. [File Description](#files)
4. [Medium Blog Post](#medium)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*. Additionly please install: python3 install pydot

## Instructions <a name ="instructions"></a>
1. Run load_and_clean.ipynb
2. Run home_team_prediction.ipynb and away_team_prediction.ipynb
3. Run result.ipynb

## Project Motivation<a name="motivation"></a>

This is the final Udacity Nanodegree project. 

Football betting has been around since the invention of football in the 19th century. It is present in commercials, as team sponsors or in betting shops around the corner (at least in Germany). Nevertheless, I think I have a solid understanding of the actual football trends, great overview of Europes biggest leagues and know most names of the players of my favourite teams (Borussia Dortmund and Hertha Berlin), I never tried to bet money on the outcome of a game or any other game related event. I always missed solid proof, that my gut feeling might be correct.

The questions I will target:

1. How to predict the number of goals correctly for any given team.

2. Is it possible to predict the outcome of a game correctly from predicted numbers of goals of each team at least 50% of all times?

## File Descriptions <a name="files"></a>

1. D1.csv: contains match related data from all football matches from the actual German Bundesliga season
2. D1_last.csv: contains match related data from all football matches from the last German Bundesliga season
3. D2.csv: contains match related data from all football matches from the last German second Bundesliga season
All files downloaded from: https://www.football-data.co.uk/germanym.php
4. df_both_seasons_essentials: pickle file with results from load_and_clean.ipynb; contains clean and merged data from D1.csv, D1_last.csv and D2.csv
5. df_both_seasons_home.xlsx: goal prediction from home teams
6. df_both_seasons_away.xlsx: goal prediction from away teams
 
## Medium Blog Post<a name="medium">
Please find here the medium blog post: 
https://medium.com/@nicholasutikal/predict-football-results-with-random-forest-c3e6f6e2ee58?

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Udacity courses for some of code ideas, and to football-data.co.uk for the data. You can find the Licensing for the data and other descriptive information at the football-data.co.uk link available [here](https://www.football-data.co.uk/germanym.php). Otherwise, feel free to use the code here as you would like!

References
1. https://www.football-data.co.uk/germanym.php
2. https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling/
3. https://www.sciencedirect.com/science/article/pii/S2210832717301485?via%3Dihub
4. https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74
5. https://arxiv.org/pdf/1710.02824.pdf
6. https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
7. https://towardsdatascience.com/improving-random-forest-in-python-part-1-893916666cd