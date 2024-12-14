import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


column_names1 = ['userID', 'movieID', 'rating', 'timestamp']
df = pd.read_csv('ratings.csv', sep=',', names=column_names1)

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

column_names2 = ['movieID', 'title', 'genres']
movie_titles = pd.read_csv('movies.csv', sep=',', names=column_names2)

df = pd.merge(df, movie_titles, on='movieID')

ratings = df.dropna(subset=['rating']).groupby('title')['rating'].agg(['mean', 'count'])
ratings.columns = ['avg_rating', 'num_of_ratings']
ratings = ratings.sort_values('avg_rating', ascending=False)

moviemat = df.pivot_table(index='userID', columns='title', values='rating')

movienameinput = input("Enter a movie name (exactly as in the dataset): ")

starwars_user_ratings = moviemat[movienameinput]
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

corr_starwars = corr_starwars.join(ratings['num_of_ratings'])

print("\nTop Correlated Movies to that movie (with more than 100 ratings):")
top_similar_starwars = corr_starwars[corr_starwars['num_of_ratings'] > 100].sort_values('Correlation', ascending=False).head()
print(top_similar_starwars)