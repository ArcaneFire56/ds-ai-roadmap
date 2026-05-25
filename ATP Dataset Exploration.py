import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2010.csv")

# print(df.count)                             # 1.How big is the dataset?
# print(df['surface'].value_counts())         # 2.Surfaces played on and value counts

# nadal_clay = df[(df['winner_name'] == 'Rafael Nadal') & (df['surface'] == 'Clay')]
# #print(nadal_clay)                           # 3.All matches Rafael Nadal won on clay

# print(df.groupby('surface')['w_ace'].mean()) #4

# print(df['winner_name'].value_counts().head()) #5

# print(df[(df['surface'] == 'Grass')]['winner_name'].value_counts().head(10))

# wins_2010 = df['winner_name'].value_counts()
# wins_2010.head()
# print(wins_2010.get('Rafael Nadal', 0))

# print(df.iloc[[0,10,20],[0,1,2]])

# print(df.loc[:,['winner_name','loser_name','surface']])
# print(df.loc[0:4,['winner_name','surface']])

# big_four = ['Rafael Nadal', 'Roger Federer', 'Novak Djokovic', 'Andy Murray']

# b4_wins = df[(df['winner_name'].isin(big_four))]
# print(b4_wins.loc[:,'winner_name'])

# long_matches = df[df['minutes'].between(180,240)]
# print(long_matches)


# nadal_rg = df[(df['tourney_name']=='Roland Garros') & ((df['winner_name'] == 'Rafael Nadal') | (df['loser_name'] == 'Rafael Nadal'))]
# print(nadal_rg[['winner_name','loser_name','score','minutes']])

# nonb4_wins = df[~(df['winner_name'].isin(
#     big_four
# ))]

# f_largest = df[df['round']=='F'].nlargest(5,'minutes')
# print(f_largest[[
#     'winner_name','loser_name','minutes'
# ]])

#################### 25/05/2026 ####################

groupby_surface = df.groupby('surface')['w_ace'].mean()
print(groupby_surface)

# groupby_winner_2010 = df.groupby('winner_name').size().sort_values(ascending=False)
# print(groupby_winner_2010.head(5))

# groupby_surface_agg = df.groupby('surface').agg(
#     avg_ace = ('w_ace', 'mean'),
#     median_length = ('minutes', 'median'),
#     matches = ('surface', 'size')
# )
# print(groupby_surface_agg)

# compare_hands = df.groupby(['surface','winner_hand'])['w_ace'].mean()
# print(compare_hands)

# pivot_surface_bestof = pd.pivot_table(
#     df,
#     values='minutes',
#     index='surface',
#     columns='best_of',
#     aggfunc='mean'
# )
# groupby_surface_reset = df.groupby('surface')['w_ace'].mean().reset_index()
# groupby_surface_reset.columns = ['Surface', 'Average Aces']
# print(groupby_surface_reset)

aces = df.groupby(['surface', 'winner_name'])['w_ace'].sum()
print(aces.groupby('surface').idxmax())

print(df.groupby('round')['minutes'].mean())
