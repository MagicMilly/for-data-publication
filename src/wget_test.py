import pandas as pd 
import wget

test_url = 'https://de.cyverse.org/dl/d/1828EE4A-1B6B-4127-B1BF-6BDF3D9D42E9/clemson_rh_2014.csv'

clemson_rh_2014 = wget.download(test_url)
df = pd.read_csv('clemson_rh_2014.csv')
print(type(df))
print(df.head())
