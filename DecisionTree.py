import os

import pandas as pd
import pydotplus
from IPython.core.display import Image
from sklearn import tree
from sklearn.externals.six import StringIO

input_file = os.getcwd() + '\data\PastHires.csv'
df = pd.read_csv(input_file, header=0)
yn_mapper = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(yn_mapper)
df['Employed?'] = df['Employed?'].map(yn_mapper)
df['Top-tier school'] = df['Top-tier school'].map(yn_mapper)
df['Interned'] = df['Interned'].map(yn_mapper)
year_mapper = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(year_mapper)
features = [col for col in df.columns if col != 'Hired']
print features
y = df[features]
x = pd.DataFrame(df['Hired'], columns=['Hired'])
print y
print x
clf = tree.DecisionTreeClassifier().fit(x, y)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
print graph
Image(graph.create_png())
