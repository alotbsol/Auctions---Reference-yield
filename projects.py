import math
import numpy as np

import power_curves


class Project:
    def __init__(self, ws100, hub_height, installed_capacity, power_curve, other_cost, other_production):
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
        self.lcoe = 1
        self.min_bid = 1

        self.hours = 8760

        self.calculate_wsHH()
        self.calculate_production()

    def calculate_wsHH(self):
        reference_hub = 100
        roughness_length = 0.1

        self.wsHH = self.ws100*(math.log(self.hub_height/roughness_length)/math.log(reference_hub/roughness_length))

        print("WS100", self.ws100,
              "WSHH", self.wsHH,
              )

    def calculate_production(self):
        wind_speed_dist = []

        constant = 1.12
        a = 2
        b = self.wsHH * constant
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
            production_list.append(((self.power_curve[i] + self.power_curve[i+1])/2) * wind_speed_dist[i] * self.hours)

        self.production = sum(production_list)
        self.production_per_MW = self.production/self.installed_capacity

    def print_project_info(self):
        print("WS100:", self.ws100,
              "Hub height:", self.hub_height,
              "Installed capacity:", self.installed_capacity,
              "Other costs:", self.other_cost,
              "Other production:", self.other_production,
              "WS HUb height:", self.wsHH,
              "Production:", self.production,
              "Production per MW:", self.production_per_MW,
              "Reference production:", self.reference_production,
              "Site quality:", self.site_quality,
              "Capacity factor:", self.capacity_factor,
              "Correction factor:", self.correction_factor,
              "LCOE:", self.lcoe,
              "MIN BID:", self.min_bid,
              )






class ProjectsStorage:
    def __init__(self):
        self.project_dict = {}
        self.number_of_projects = 1

    def add_project(self):
        self.project_dict[str(self.number_of_projects)] = Project(ws100=6,
                                                                  hub_height=128,
                                                                  installed_capacity=3,
                                                                  power_curve=power_curves.Enercon_E115,
                                                                  other_cost=1,
                                                                  other_production=1
                                                                  )
        self.number_of_projects += 1
