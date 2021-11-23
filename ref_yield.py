from numpy import array

site_qualities = array([0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
correction_factors = {0.7: 1.29, 0.8: 1.16, 0.9: 1.07, 1: 1, 1.1: 0.94, 1.2: 0.89, 1.3: 0.85, 1.4: 0.81, 1.5: 0.79}


def calculate_correction(input_sq):
    if input_sq > 1.5:
        print("higher sq")
    else:
        if input_sq < 0.7:
            print("lower sq")
        else:
            lower = site_qualities[site_qualities < input_sq].max()
            upper = site_qualities[site_qualities > input_sq].min()

            proportion_lower = round(input_sq - lower, 5)
            proportion_upper = round(upper - input_sq, 5)

            print(lower)
            print(upper)
            print(proportion_lower)
            print(proportion_upper)


print(calculate_correction(1.6))
print(calculate_correction(0.6))
print(calculate_correction(0.8))
print(calculate_correction(0.84))
