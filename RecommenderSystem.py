import os

import numpy as np
import pandas as pd

# Read CSVs to fill in the movie data
cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(os.getcwd() + '\\data\\ml-100k\\u.data', sep='\t', names=cols, usecols=range(3))

cols2 = ['movie_id', 'title']
movies = pd.read_csv(os.getcwd() + '\\data\\ml-100k\\u.item', sep='|', names=cols2, usecols=range(2))

ratings = pd.merge(ratings, movies)
# print ratings.head()

movieRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
# print movieRatings.head()

star_wars_ratings = movieRatings['Star Wars (1977)']
# print star_wars_ratings
# print movieRatings['Alien 3 (1992)']

# Compute correlation with other movies
similar_movies = movieRatings.corrwith(star_wars_ratings)
similar_movies = similar_movies.dropna()
df = pd.DataFrame(similar_movies).dropna()

# print star_wars_ratings.dropna()
# print similar_movies.corr(pd.DataFrame(similar_movies).dropna())
# print df.sort(0, ascending=False)
# On printing the movies which have high correlation with Star Wars
# there are also movies with no relation with Star Wars. Why so?
# df = df.sort(0, ascending=False)
# print df

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
# print movieStats.head(10)

# Observe that size (number of people) who voted is also important
# we were getting garbage recommendations because there might be just
# one or two ratings which were similar to star wars and hence had
# perfect correlation and since correlation is computed only with
# int values and not NaNs, which lead to bad recommendations
popularMovies = movieStats[movieStats['rating']['size'] >= 100]
# print popularMovies.sort([('rating', 'size')], ascending=False)
nice = [1 if x in popularMovies.index else 0 for x in movieStats.index]
df = popularMovies.join(pd.DataFrame(similar_movies, columns=['similarity']))
# print df.sort_values('similarity', ascending=False)


# Make actual recommendations
myRatings = movieRatings.loc[0].dropna()
# print myRatings

# Compute correlation matrix
correlation_matrix = movieRatings.corr(method='pearson', min_periods=100)
# print correlation_matrix.head()

similar_candidates = pd.Series()
for i in range(len(myRatings.index)):
    print 'Adding recommendations for ' + myRatings.index[i] + '...'
    similars = correlation_matrix[myRatings.index[i]].dropna()
    similars = similars.map(lambda x: x * myRatings[i] if myRatings[i] > 3 else x / myRatings[i])
    similar_candidates = similar_candidates.append(similars)
print 'sorting..'
similar_candidates = similar_candidates.groupby(similar_candidates.index).sum()
similar_candidates.sort_values(inplace=True, ascending=False)
print similar_candidates.head(10)
