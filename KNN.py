import os

import numpy as np
import pandas as pd
from scipy import spatial

columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv(os.getcwd() + '/data/ml-100k/u.data', sep='\t', names=columns, usecols=range(3))
# print ratings.head()

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.mean, np.size]})
# print movieProperties

# These raw numbers are not useful, hence we will normalize the data w.r.t the
# difference in maximum and minimum
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
# This will normalize all the movies from 0 to 1, 0 for minimum watched movies and 1 for
# maximum watched movies
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
# print movieNormalizedNumRatings.head()

movieDict = {}
with open(os.getcwd() + '/data/ml-100k/u.item') as f:
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        generes = fields[5:25]
        generes = map(int, generes)
        movieDict[movieID] = (name, generes, movieNormalizedNumRatings.loc[movieID].get('size'),
                              movieProperties.loc[movieID].rating.get('mean'))


# print movieDict[1]


def compute_distance(a, b):
    """
    Computes distance between 2 movies, based on genre and popularity
    :param a: movie property list 1
    :param b: movie property list 2
    :return: cosine distance of genre vector + abs(popularities)
    """
    genreA = a[1]
    genreB = b[1]
    genreDistance = spatial.distance.cosine(genreA, genreB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance


# print compute_distance(movieDict[2], movieDict[4])


def get_neighbours(movie_id, K):
    distances = []
    for movie in movieDict:
        if movie != movieID:
            dist = compute_distance(movieDict[movie], movieDict[movieID])
            distances.append((movie, dist))
    distances.sort(key=lambda elem: elem[1])
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors


K = 10
movieID = 4
print 'Movies similiar to : ' + movieDict[movieID][0]
for neighbors in get_neighbours(movieID, K):
    print movieDict[neighbors][0], str(movieDict[neighbors][3])
