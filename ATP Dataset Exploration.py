import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2010.csv")

#print(df.count)                             # 1.How big is the dataset?
#print(df['surface'].value_counts())         # 2.Surfaces played on and value counts

nadal_clay = df[(df['winner_name'] == 'Rafael Nadal') & (df['surface'] == 'Clay')]
#print(nadal_clay)                           # 3.All matches Rafael Nadal won on clay

# print(df.groupby('surface')['w_ace'].mean()) #4

# print(df['winner_name'].value_counts().head()) #5

# print(df[(df['surface'] == 'Grass')]['winner_name'].value_counts().head(10))

wins_2010 = df['winner_name'].value_counts()
wins_2010.head()
print(wins_2010.get('Rafael Nadal', 0))