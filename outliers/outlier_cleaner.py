#!/usr/bin/python
import math


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    for index in xrange(0,90):

        predicted = predictions[index]
        age = ages[index]
        net_worth = net_worths[index]
        error = math.pow((predicted - net_worth), 2)

        tuple = age, net_worth, error
        cleaned_data.append(tuple)


    ordered = sorted(cleaned_data, key=lambda x: (x[2], x[1], x[0]))

    top = 81
    cleaned_data = ordered[0:top]

    return cleaned_data

