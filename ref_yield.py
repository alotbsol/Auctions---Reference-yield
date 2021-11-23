from numpy import array

site_qualities = array([0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5])
correction_factors = {0.7: 1.29, 0.8: 1.16, 0.9: 1.07, 1: 1, 1.1: 0.94, 1.2: 0.89, 1.3: 0.85, 1.4: 0.81, 1.5: 0.79}


def calculate_correction(input_sq):
    correction_factor = 0
    if input_sq > 1.5:
        correction_factor = 0.79
        return correction_factor

    else:
        if input_sq < 0.7:
            correction_factor = 1.29
            return correction_factor

        else:
            lower = site_qualities[site_qualities <= input_sq].max()
            upper = site_qualities[site_qualities > input_sq].min()

            proportion_lower = round((0.1 - (upper - input_sq))/0.1, 5)
            correction_factor_difference = correction_factors[lower]-correction_factors[upper]
            correction_factor = correction_factors[lower] - (correction_factor_difference * proportion_lower)

            return correction_factor

def calculate_extrapolated_correction(input_sq):
    correction_factor = 0
    if input_sq > 1.5:
        correction_factor = 0.79 - (input_sq - 1.5)/0.1 * 0.02
        return correction_factor

    else:
        if input_sq < 0.7:
            correction_factor = 1.29 + (0.7 - input_sq)/0.1 * 0.13
            return correction_factor

        else:
            lower = site_qualities[site_qualities <= input_sq].max()
            upper = site_qualities[site_qualities > input_sq].min()

            proportion_lower = round((0.1 - (upper - input_sq))/0.1, 5)
            correction_factor_difference = correction_factors[lower]-correction_factors[upper]
            correction_factor = correction_factors[lower] - (correction_factor_difference * proportion_lower)

            return correction_factor
