import pandas as pd 
import numpy as np
import pickle

df = pd.read_csv("ipl.csv")

df.drop(['mid','batsman','bowler','striker','non-striker'],inplace=True, axis='columns')

df.drop('venue', axis='columns', inplace = True)

faketeams = ['Deccan Chargers','Pune Warriors','Gujarat Lions','Rising Pune Supergiant','Kochi Tuskers Kerala','Rising Pune Supergiants']

df.drop(index = df[df['bat_team'].isin(faketeams)].index, inplace = True)
df.drop(df[df['bowl_team'].isin(faketeams)].index, inplace = True)

df.drop(df[df['overs']<=6.0].index, inplace = True)

df['year'] = df['date'].str.split('-').str[0]
df['year'] = df['year'].astype(int)

newdf = pd.get_dummies(data=df, columns=['bat_team','bowl_team'])


newdf.drop(['date'], axis='columns', inplace=True)

newdf = newdf[['year', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',
              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',
              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]

xtrain = newdf[newdf['year']<=2016]
xtest = newdf[newdf['year']>=2017]

xtrain.drop(['total'], axis='columns', inplace=True)
xtest.drop(['total'], axis = 'columns', inplace=True)

ytrain = newdf[newdf['year']<=2016]['total'].values
ytest = newdf[newdf['year']>=2017]['total'].values

xtrain.drop(['year'], axis='columns', inplace=True)

xtest.drop(['year'], axis='columns', inplace=True)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(xtrain,ytrain)

pickle.dump(lr, open('ipll.pkl','wb'))


