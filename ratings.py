""" Implementation of five-star rating algorithm considering quality and quantity 
    Author : Theophilus Okoye
"""

from math import exp

ARBITRARY = 100

def rate(params = {}):

    if params != {}:
        rating = 0
        for i in range(len(params)):
            rating += (i + 1) * (0.25 * (i + 1) + 2.5 * (1 - exp(-params[i + 1]/ARBITRARY)))

        return round(rating/10, 2)
