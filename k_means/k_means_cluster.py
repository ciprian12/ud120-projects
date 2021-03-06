#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""

from __future__ import division


import pickle
import numpy
import matplotlib.pyplot as plt
import sys

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import preprocessing



def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"

poi  = "poi"
features_list = [poi, feature_1, feature_2]
# features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
max_stock = 0
min_stock = 1111110

max_salary = 0
min_salary = 1111110


# for f1, f2, _ in finance_features:
for f1, f2 in finance_features:
    if max_stock < f2:
        max_stock = f2
    if f2 > 0:
        if min_stock > f2:
            min_stock = f2

    if max_salary < f1:
        max_salary = f1
    if f1 > 0:
        if min_salary > f1:
            min_salary = f1

    plt.scatter( f1, f2 )
plt.show()

print "max_stock %d" % max_stock
print "min_stock %d" % min_stock

print "max_salary %d" % max_salary
print "min_salary %d" % min_salary

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

min_max_scaler = preprocessing.MinMaxScaler()
data_train_minmax = min_max_scaler.fit_transform(data)
finance_features_train_minmax = min_max_scaler.fit_transform(finance_features)

print finance_features_train_minmax

print data_train_minmax


print "scaled salary %s" % ((200000. - min_salary)/(max_salary - min_salary))
print "scaled stock %s" % ((1000000. - min_stock)/(max_stock - min_stock))


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2).fit(data_train_minmax)
pred = kmeans.predict(data_train_minmax)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features_train_minmax, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
