#!/usr/bin/python

import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from sklearn.neighbors import KNeighborsClassifier
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


neigh = KNeighborsClassifier(n_neighbors=3)

t0 = time()
neigh.fit(features_train, labels_train)
print "KNN training time:", round(time()-t0, 3), "s"

t1 = time()
pred = neigh.predict(features_test)
print "KNN prediction time:", round(time()-t1, 3), "s"

t2 = time()
accuracy = neigh.score(features_test, labels_test)
print "KNN accuracy time:", round(time()-t2, 3), "s"

print "KNN accuracy %s", accuracy

#
# try:
#     prettyPicture(neigh, features_test, labels_test)
# except NameError:
#     pass

################################################################################


rfc = RandomForestClassifier(n_estimators=10)

t0 = time()
rfc.fit(features_train, labels_train)
print "RandomForest training time:", round(time()-t0, 3), "s"

t1 = time()
pred = rfc.predict(features_test)
print "RandomForest prediction time:", round(time()-t1, 3), "s"

t2 = time()
accuracy = rfc.score(features_test, labels_test)
print "RandomForest accuracy time:", round(time()-t2, 3), "s"

print "RandomForest accuracy %s", accuracy


################################################################################


adbc = AdaBoostClassifier()

t0 = time()
adbc.fit(features_train, labels_train)
print "AdaBoost training time:", round(time()-t0, 3), "s"

t1 = time()
pred = adbc.predict(features_test)
print "AdaBoost prediction time:", round(time()-t1, 3), "s"

t2 = time()
accuracy = adbc.score(features_test, labels_test)
print "AdaBoost accuracy time:", round(time()-t2, 3), "s"

print "AdaBoost accuracy %s", accuracy
