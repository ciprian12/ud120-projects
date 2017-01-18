#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn import svm
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###


# clf = svm.SVC(kernel='linear')
# clf = svm.SVC(kernel='rbf', C=10.0)
# clf = svm.SVC(kernel='rbf', C=100.0)
# clf = svm.SVC(kernel='rbf', C=1000.0)
clf = svm.SVC(kernel='rbf', C=10000.0)


# optional: reduce training set
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy =  clf.score(features_test, labels_test)

print accuracy

nth = 10
print "element %d : %d" % (nth, pred[nth])

nth = 26
print "element %d : %d" % (nth, pred[nth])


nth = 50
print "element %d : %d" % (nth, pred[nth])


nth = 100
print "element %d : %d" % (nth, pred[nth])


count_chris = 0
for i in xrange(0,len(pred)):
    if pred[i] == 1:
        count_chris = count_chris + 1

print "chris emails %d" % count_chris

#########################################################


