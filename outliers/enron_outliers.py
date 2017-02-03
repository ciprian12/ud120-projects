#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop('TOTAL', 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

name_index = 0
for point in data_dict:
    print "%s %s" % (name_index, point)
    name_index += 1

name_index = 0

max_bonus = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    if bonus > max_bonus:
        max_bonus = bonus
    print "%s %s" % (name_index, point)
    matplotlib.pyplot.scatter( salary, bonus )
    name_index += 1

print "max bonus %s" % max_bonus

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()