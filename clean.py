import pandas as pd
#import and clean up
df = pd.read_csv('cleaned.csv')
df['Link'] = df['Link'].str.replace(' ', '')
df.to_csv('cleaned.csv')