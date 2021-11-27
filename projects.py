import math
import numpy as np
import pandas as pd

import power_curves
from ref_yield import calculate_correction
from ref_yield import calculate_extrapolated_correction


class Project:
    def __init__(self, base_lcoe, ws100, hub_height, installed_capacity,
                 turbine_name, power_curve, other_cost, other_production, max_bid_possible,
                 corr_f_applicability=1):
        self.all_vars = []

        self.base_lcoe = base_lcoe
        self.ws100 = ws100
        self.hub_height = hub_height
        self.installed_capacity = installed_capacity
        self.power_curve = power_curve
        self.turbine_name = turbine_name
        self.other_cost = other_cost
        self.other_production = other_production
        self.max_bid_possible = max_bid_possible
        self.corr_f_applicability = corr_f_applicability

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

        self.winning = 0
        self.marginal = 0
        self.subsidy = 0
        self.surplus = 0

        self.hours = 8760
        self.losses = 0.8

    def update_project(self):
        self.wsHH = self.calculate_wsHH(ws100_input=self.ws100)
        self.production = self.calculate_production(ws_input=self.wsHH)
        self.production_per_MW = (self.production / self.installed_capacity)
        self.calculate_reference_production()
        self.capacity_factor = self.production_per_MW/self.hours
        self.calculate_correction_factor()
        self.calculate_lcoe()
        self.calculate_min_bid()

        self.winning = 0
        self.marginal = 0
        self.subsidy = 0
        self.surplus = 0

        self.update_variables()

    def update_variables(self):
        self.all_vars = [self.base_lcoe, self.ws100, self.hub_height, self.installed_capacity, self.turbine_name,
                         self.other_cost, self.other_production, self.wsHH, self.production, self.production_per_MW,
                         self.reference_production, self.site_quality, self.capacity_factor,
                         self.corr_f_applicability, self.correction_factor,
                         self.extrapolated_correction_factor, self.lcoe, self.min_bid, self.winning, self.marginal,
                         self.subsidy, self.surplus]

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

        return sum(production_list)/1000

    def calculate_reference_production(self):
        reference_ws100 = 6.45
        reference_wshh = self.calculate_wsHH(ws100_input=reference_ws100)
        self.reference_production = self. calculate_production(ws_input=reference_wshh)

        self.site_quality = self.production/self.reference_production

    def calculate_correction_factor(self):
        self.correction_factor = (calculate_correction(self.site_quality) - 1)*self.corr_f_applicability + 1
        self.extrapolated_correction_factor = calculate_extrapolated_correction(self.site_quality)

    def calculate_lcoe(self):
        self.lcoe = min(self.base_lcoe * self.extrapolated_correction_factor * self.other_cost,
                        self.max_bid_possible * self.correction_factor)

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

    def change_to_winning(self, in_put=1):
        self.winning = in_put
        self.update_variables()

    def change_to_marginal(self, in_put=1):
        self.marginal = in_put
        self.update_variables()

    def assign_subsidy(self, in_bid):
        self.subsidy = in_bid * self.correction_factor
        self.surplus = self.subsidy - self.lcoe
        self.update_variables()


class ProjectsStorage:
    def __init__(self, demand, name, ref_yield_scenarios, max_bid_possible=100, iteration=1, project_size_adjustment=3):
        self.project_dict = {}
        self.number_of_projects = 0
        self.project_size_adjustment = project_size_adjustment

        self.demand = demand
        self.name = name
        self.ref_yield_scenarios = ref_yield_scenarios
        self.max_bid_possible = max_bid_possible
        self.iteration = iteration

        self.export_dict = {}
        self.round_results = {"name": [], "iteration": [], "supply": [], "demand": [], "ref_yield": [], "marginal_bid": [],
                              "min_successful": [], "average_successful": [], "average_subsidy": [],
                              "subsidy": [], "subsidy_perMW": [], "surplus_projects": [], "surplus_projects_perMW": [],
                              "produced_el": [], "produced_el_perMW": []}

    def add_project(self, base_lcoe=50, ws100=6, hub_height=128, installed_capacity=3,
                    power_curve=power_curves.Enercon_E115, turbine_name="Enercon_E115",
                    other_cost=1, other_production=1, ):

        self.number_of_projects += 1
        self.project_dict[str(self.number_of_projects)] = Project(base_lcoe=base_lcoe,
                                                                  ws100=ws100,
                                                                  hub_height=hub_height,
                                                                  installed_capacity=installed_capacity,
                                                                  turbine_name=turbine_name,
                                                                  power_curve=power_curve,
                                                                  other_cost=other_cost,
                                                                  other_production=other_production,
                                                                  max_bid_possible=self.max_bid_possible
                                                                  )

    def delete_projects(self):
        self.project_dict = {}
        self.number_of_projects = 0

    def auction_results(self):
        self.round_results["ref_yield"].extend(self.ref_yield_scenarios)

        for i in self.ref_yield_scenarios:
            bids = []
            successful_bids = []
            subsidy = []
            surplus = []
            produced_el = []

            for ii in self.project_dict:
                self.project_dict[ii].corr_f_applicability = i
                self.project_dict[ii].update_project()
                bids.append(self.project_dict[ii].min_bid)

            winning_projects = sorted(range(len(bids)), key=lambda k: bids[k])[:self.demand]
            winning_projects = [x + 1 for x in winning_projects]

            minimum_bid = self.project_dict[str(winning_projects[0])].min_bid

            if len(winning_projects) < self.demand:
                marginal_bid = self.max_bid_possible
            else:
                marginal_project = winning_projects[-1]
                marginal_bid = float(self.project_dict[str(marginal_project)].min_bid)
                self.project_dict[str(marginal_project)].change_to_marginal()

            for ii in winning_projects:
                self.project_dict[str(ii)].change_to_winning()
                self.project_dict[str(ii)].assign_subsidy(in_bid=marginal_bid)
                successful_bids.append(self.project_dict[str(ii)].min_bid)

                # set to use production per MW and then multiplied by size of project
                subsidy.append(self.project_dict[str(ii)].subsidy * self.project_dict[str(ii)].production_per_MW * self.project_size_adjustment)
                surplus.append(self.project_dict[str(ii)].surplus * self.project_dict[str(ii)].production_per_MW * self.project_size_adjustment)
                produced_el.append(self.project_dict[str(ii)].production_per_MW * self.project_size_adjustment)

            self.export_dict[str(i)] = {}
            for ii in self.project_dict:
                self.export_dict[str(i)][str(ii)] = self.project_dict[ii].all_vars

            self.round_results["name"].append(self.name)
            self.round_results["iteration"].append(self.iteration)
            self.round_results["supply"].append(self.number_of_projects)
            self.round_results["demand"].append(self.demand)
            self.round_results["marginal_bid"].append(marginal_bid)
            self.round_results["min_successful"].append(minimum_bid)
            self.round_results["average_successful"].append(sum(successful_bids)/len(successful_bids))
            self.round_results["average_subsidy"].append(sum(subsidy)/sum(produced_el))
            self.round_results["subsidy"].append(sum(subsidy))
            self.round_results["subsidy_perMW"].append(sum(subsidy)/self.project_size_adjustment/len(winning_projects))
            self.round_results["surplus_projects"].append(sum(surplus))
            self.round_results["surplus_projects_perMW"].append(sum(surplus)/self.project_size_adjustment/len(winning_projects))
            self.round_results["produced_el"].append(sum(produced_el))
            self.round_results["produced_el_perMW"].append(sum(produced_el)/self.project_size_adjustment/len(winning_projects))


    def export(self, projects_export=True):
        writer = pd.ExcelWriter("{0}.xlsx".format(self.name), engine="xlsxwriter")

        df_results = pd.DataFrame.from_dict(self.round_results)
        df_results.to_excel(writer, sheet_name="Results")

        if projects_export:
            for i in self.export_dict:
                df_projects = pd.DataFrame.from_dict(self.export_dict[str(i)]).transpose()
                df_projects.columns = ["base_lcoe", "ws100", "hub_height", "installed_capacity", "turbine_name", "other_cost",
                                       "other_production", "wsHH", "production", "production_per_MW", "reference_production",
                                       "site_quality", "capacity_factor",
                                       "corr_f_applicability", "correction_factor", "extrapolated_correction_factor",
                                       "lcoe", "min_bid", "winning", "marginal", "subsidy", "surplus"]

                df_projects.to_excel(writer, sheet_name="Projects_ref{0}".format(i))


        writer.save()

    def return_results(self):
        return pd.DataFrame.from_dict(self.round_results)



