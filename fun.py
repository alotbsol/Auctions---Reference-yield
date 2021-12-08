# this file is for functions
from numpy.random import randint
import numpy as np


def ran_gen_float(lower_limit, upper_limit, size=1):
    x = np.random.uniform(lower_limit, upper_limit, int(size))
    return x[0]


testing_probability = {"limits": [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
                       "values": [4.96961689, 6.092707157, 6.582392311, 6.893632889, 7.27610836,
                                  7.583831787, 7.791398525, 7.964614773, 8.286667824, 8.537548065, 8.914340019],
                      }


def random_from_prob_dist(input_probabilities):
    random_var = np.random.random()
    limits_array = np.array(input_probabilities["limits"])

    closest_lower = limits_array[limits_array < random_var].max()
    closest_higher = limits_array[limits_array > random_var].min()

    index_lower = input_probabilities["limits"].index(closest_lower)
    index_higher = input_probabilities["limits"].index(closest_higher)

    return_value = input_probabilities["values"][index_higher] - input_probabilities["values"][index_lower]



    print(limits_array)
    print(random_var)
    print(closest_lower)
    print(closest_higher)
    print(index_lower)
    print(index_higher)
    print(return_value)





random_from_prob_dist(testing_probability)