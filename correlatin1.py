import pandas as pd
df=pd.read.csv('rides.csv')
corr_coef=df['Ride Time'].corr(df['Ride Fare'])
print('Correlation coefficent:',corr_coef)
