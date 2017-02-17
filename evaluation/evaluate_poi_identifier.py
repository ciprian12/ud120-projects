#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import tree
from time import time

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split( features, labels, test_size=0.3, random_state=42)

# clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = tree.DecisionTreeClassifier()

# features_train = features
# features_test = features

# labels_train = labels
# labels_test = labels

print "test feature_test_size %d" % len(features_test)
print "test feature_train_size %d" % len(features_train)

print "test labels_test_size %d" % len(labels_test)
print "test labels_train_size %d" % len(labels_train)


t0 = time()
clf = clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

accuracy = clf.score(features_train, labels_train)
print "accuracy of %s" % accuracy


t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

print "predicted size %d" % len(pred)

accuracy = clf.score(features_test, labels_test)
print "accuracy of %s" % accuracy

poi_count = 0
for p in pred:
    if p == 1.0:
        poi_count += 1

print "poi_count: %d" % poi_count

not_equal_count = 0
for i in xrange(0, len(pred)):
    print "actual %s pred %s" % (labels_test[i], pred[i])
    if labels_test[i] != pred[i]:
        not_equal_count +=1

print "not_equal_count %d" % not_equal_count


# from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

precision = precision_score(labels_test, pred)
recall = recall_score(labels_test, pred)

print "precision: %s" % precision
print "recall: %s" % recall
