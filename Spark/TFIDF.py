import os

from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

conf = SparkConf().setMaster('local').setAppName('TFIDF')
sc = SparkContext(conf=conf)

input_file = os.getcwd() + '/../data/subset-small.tsv'
raw_data = sc.textFile(input_file)
fields = raw_data.map(lambda x: x.split('\t'))
documents = fields.map(lambda x: x[3].split(' '))

# store document names for later
document_names = fields.map(lambda x: x[1])

# hash the words with their term frequencies
hashingTF = HashingTF(100000)
tf = hashingTF.transform(documents)

# compute tdidf for every word in the document
tf.cache()
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)

# compute the hash value for Gettysburg
gettysbergTF = hashingTF.transform(['Gettysburg'])
gettysbergHashValue = gettysbergTF.indices[0]

# extract TF*IDF score for Gettysburg's hash value into
# a new RDD for every document
gettysbergRelevance = tfidf.map(lambda x: x[gettysbergHashValue])

# zip the document names so we know which one's the best match
zippedResults = gettysbergRelevance.zip(document_names)

print 'Best document match is : '
print zippedResults.max()
