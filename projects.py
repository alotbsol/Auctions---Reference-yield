
class Project:
    def __init__(self, ws100, hub_height, installed_capacity, power_curve):
        self.ws100 = ws100
        self.hub_height = hub_height
        self.installed_capacity = installed_capacity

        self.power_curve = power_curve

        self.wsHH = 1

        self.production = 1
        self.production_per_MW = 1

        self.site_quality = 1
        self.capacity_factor = 1

        self.correction_factor = 1

        self.lcoe = 1
        self.min_bid = 1

