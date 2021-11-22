import math

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

        self.all_vars = []

        self.calculate_wsHH()

    def calculate_wsHH(self):
        reference_hub = 100
        roughness_length = 0.1

        self.wsHH = self.ws100*(math.log(self.hub_height/roughness_length)/math.log(reference_hub/roughness_length))

        print("WS100", self.ws100,
              "WSHH", self.wsHH,
              )

    def calculate_production(self):
        = a/b *

        =WEIBULL.DIST(A26,$C$12,$C$14, TRUE)-SUM($C$25: C25)



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
