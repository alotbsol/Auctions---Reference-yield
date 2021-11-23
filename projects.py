import math
import numpy as np

import power_curves
from ref_yield import calculate_correction
from ref_yield import calculate_extrapolated_correction


class Project:
    def __init__(self, base_lcoe, ws100, hub_height, installed_capacity, power_curve, other_cost, other_production):
        self.base_lcoe = base_lcoe
        self.ws100 = ws100
        self.hub_height = hub_height
        self.installed_capacity = installed_capacity
        self.power_curve = power_curve
        self.other_cost = other_cost
        self.other_production = other_production

        self.wsHH = 1
        self.production = 1
        self.production_per_MW = 1
        self.reference_production = 1
        self.site_quality = 1
        self.capacity_factor = 1
        self.correction_factor = 1
        self.extrapolated_correction_factor = 1
        self.lcoe = 1
        self.min_bid = 1

        self.hours = 8760
        self.losses = 0.8

        self.wsHH = self.calculate_wsHH(ws100_input=self.ws100)
        self.production = self.calculate_production(ws_input=self.wsHH)
        self.production_per_MW = (self.production / self.installed_capacity)
        self.calculate_reference_production()
        self.capacity_factor = self.production_per_MW/self.hours/1000
        self.calculate_correction_factor()
        self.calculate_lcoe()
        self.calculate_min_bid()

    def calculate_wsHH(self, ws100_input):
        reference_hub = 100
        roughness_length = 0.1

        return ws100_input*(math.log(self.hub_height/roughness_length)/math.log(reference_hub/roughness_length))

    def calculate_production(self, ws_input):
        wind_speed_dist = []

        constant = 1.12
        a = 2
        b = ws_input * constant
        x_min = 1
        x_max = 30
        e = np.exp(1)

        val = 0
        for i in range(x_min, x_max):
            cumulative = (1 - e ** -(i / b) ** a)

            wind_speed_dist.append(cumulative - val)
            val = cumulative

        production_list = []

        for i in range(0, len(wind_speed_dist)):
            production_list.append(((self.power_curve[i] + self.power_curve[i+1])/2) * wind_speed_dist[i]
                                   * self.hours * self.losses * self.other_production)

        return sum(production_list)

    def calculate_reference_production(self):
        reference_ws100 = 6.45
        reference_wshh = self.calculate_wsHH(ws100_input=reference_ws100)
        self.reference_production = self. calculate_production(ws_input=reference_wshh)

        self.site_quality = self.production/self.reference_production

    def calculate_correction_factor(self):
        self.correction_factor = calculate_correction(self.site_quality)
        self.extrapolated_correction_factor = calculate_extrapolated_correction(self.site_quality)

    def calculate_lcoe(self):
        self.lcoe = self.base_lcoe * self.extrapolated_correction_factor * self.other_cost

    def calculate_min_bid(self):
        self.min_bid = self.lcoe / self.correction_factor

    def print_project_info(self):
        print("WS100:", self.ws100,
              "\nHub height:", self.hub_height,
              "\nInstalled capacity:", self.installed_capacity,
              "\nOther costs:", self.other_cost,
              "\nOther production:", self.other_production,
              "\nWS HUb height:", self.wsHH,
              "\nProduction:", self.production,
              "\nProduction per MW:", self.production_per_MW,
              "\nReference production:", self.reference_production,
              "\nSite quality:", self.site_quality,
              "\nCapacity factor:", self.capacity_factor,
              "\nCorrection factor:", self.correction_factor,
              "\nExtrapolated Correction factor:", self.extrapolated_correction_factor,
              "\nLCOE:", self.lcoe,
              "\nMIN BID:", self.min_bid,
              )


class ProjectsStorage:
    def __init__(self, demand):
        self.project_dict = {}
        self.number_of_projects = 1

        self.demand = demand

    def add_project(self, base_lcoe=50, ws100=6, hub_height=128, installed_capacity=3,
                    power_curve=power_curves.Enercon_E115, other_cost=1, other_production=1):
        self.project_dict[str(self.number_of_projects)] = Project(base_lcoe=base_lcoe,
                                                                  ws100=ws100,
                                                                  hub_height=hub_height,
                                                                  installed_capacity=installed_capacity,
                                                                  power_curve=power_curve,
                                                                  other_cost=other_cost,
                                                                  other_production=other_production
                                                                  )
        self.number_of_projects += 1
