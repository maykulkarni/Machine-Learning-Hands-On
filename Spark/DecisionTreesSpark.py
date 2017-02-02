import os

import numpy as np
from pyspark import SparkConf, SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree


def binary(YN):
    return 1 if YN == 'Y' else 0


def map_education(degree):
    degree_dict = {
        'BS': 1,
        'MS': 2,
        'PhD': 3
    }
    return degree_dict[degree]


def create_labeled_points(field):
    years_experience = int(field[0])
    employed = binary(field[1])
    previous_employers = binary(field[2])
    education_level = map_education(field[3])
    top_tier = binary(field[4])
    interned = binary(field[5])
    hired = binary(field[6])

    return LabeledPoint(hired, np.array([years_experience, employed, previous_employers,
                                         education_level, top_tier, interned]))


if __name__ == '__main__':
    # Get Spark context object
    conf = SparkConf().setMaster('local').setAppName('SparkDecisionTree')
    sc = SparkContext(conf=conf)

    # Input file CSV
    input_file = os.getcwd() + '/../data/PastHires.csv'  # /../ because PastHires is in /data and cwd is /Spark/
    raw_data = sc.textFile(input_file)
    header = raw_data.first()
    raw_data = raw_data.filter(lambda x: x != header)

    # Split based on comma delimeter
    csv_data = raw_data.map(lambda x: x.split(','))

    training_data = csv_data.map(create_labeled_points)

    # create fake testing data
    test_data = [np.array([10, 1, 3, 1, 0, 0])]
    # create RDD
    test_data = sc.parallelize(test_data)

    # train decision tree
    model = DecisionTree.trainClassifier(training_data, numClasses=2,
                                         # this maps fields to
                                         # the number of fields they have, not defined to continuous values
                                         categoricalFeaturesInfo={1: 2, 3: 4, 4: 2, 5: 2},
                                         impurity='gini', maxDepth=5, maxBins=32)
    # Make predictions
    prediction = model.predict(test_data)
    print 'Hire predictions: '
    results = prediction.collect()
    for result in results:
        print result

    print 'Learned classification tree: '
    print model.toDebugString()
