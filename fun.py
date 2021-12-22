# this file is for functions
from numpy.random import randint
import numpy as np


def ran_gen_float(lower_limit, upper_limit, size=1):
    x = np.random.uniform(lower_limit, upper_limit, int(size))
    return x[0]


def random_from_prob_dist(input_probabilities):
    random_var = np.random.random()
    limits_array = np.array(input_probabilities["limits"])

    closest_lower = limits_array[limits_array < random_var].max()
    closest_higher = limits_array[limits_array > random_var].min()

    index_lower = input_probabilities["limits"].index(closest_lower)
    index_higher = input_probabilities["limits"].index(closest_higher)

    perc = (random_var - closest_lower) / (closest_higher - closest_lower)
    return_value = perc * (input_probabilities["values"][index_higher] - input_probabilities["values"][index_lower]) + \
                   input_probabilities["values"][index_lower]

    return return_value

def from_prob_dist(input_probabilities, input_number):
    random_var = input_number
    limits_array = np.array(input_probabilities["limits"])

    closest_lower = limits_array[limits_array < random_var].max()
    closest_higher = limits_array[limits_array > random_var].min()

    index_lower = input_probabilities["limits"].index(closest_lower)
    index_higher = input_probabilities["limits"].index(closest_higher)

    perc = (random_var - closest_lower) / (closest_higher - closest_lower)
    return_value = perc * (input_probabilities["values"][index_higher] - input_probabilities["values"][index_lower]) + \
                   input_probabilities["values"][index_lower]

    return return_value

