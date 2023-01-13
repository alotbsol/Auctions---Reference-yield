from datetime import datetime
import numpy as np
import pandas as pd

import projects
import power_curves
from fun import ran_gen_float
from fun import random_from_prob_dist
from fun import from_prob_dist
from german_auctions import auctions_supply_demand
import german_auctions
import example_distributions


def scenario2_supply_demand():
    df_results = pd.DataFrame()

    number_of_projects = 41
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    demand_scenarios = list(range(1, number_of_projects+1))

    # submitted/won/max bid/average project
    for ii in demand_scenarios:
        demand = ii

        Master_storage = projects.ProjectsStorage(demand=demand, name="{0}".format(str(ii)),
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  project_size_adjustment=3)

        ws_list = np.linspace(start=5, stop=9, num=number_of_projects, endpoint=True, retstep=False, dtype=None)

        for i in range(number_of_projects):
            Master_storage.add_project(base_lcoe=50,
                                       ws100=ws_list[i],
                                       hub_height=128,
                                       installed_capacity=3,
                                       power_curve=power_curves.Enercon_E115,
                                       turbine_name="Enercon_E115",
                                       other_cost=1,
                                       other_production=1)

        Master_storage.auction_results()
        Master_storage.delete_projects()
        Master_storage.iteration += 1

        df_results = df_results.append(Master_storage.return_results())

    writer = pd.ExcelWriter("scenario2_supply_demand.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()

def scenario3_other_costs():
    df_results = pd.DataFrame()

    iterations = 1000
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.5, 0.99, 1.01, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

    Master_storage = projects.ProjectsStorage(name="scenario3_other_costs",
                                              ref_yield_scenarios=ref_yield_scenarios,
                                              project_size_adjustment=3, demand_list=demand_scenarios)

    for ii in range(iterations):
        print("itteration:", ii)
        ws_list = np.linspace(start=5, stop=9, num=number_of_projects, endpoint=True, retstep=False, dtype=None)

        for i in range(number_of_projects):
            other_costs = ran_gen_float(lower_limit=0.8, upper_limit=1.2)

            Master_storage.add_project(base_lcoe=50,
                                       ws100=ws_list[i],
                                       hub_height=128,
                                       installed_capacity=3,
                                       power_curve=power_curves.Enercon_E115,
                                       turbine_name="Enercon_E115",
                                       other_cost=other_costs,
                                       other_production=1)

        Master_storage.auction_results_multi_demand()
        Master_storage.delete_projects()
        Master_storage.iteration += 1

    df_results = df_results.append(Master_storage.return_results())

    writer = pd.ExcelWriter("scenario3_other_costs.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()

if __name__ == '__main__':
    start_time = datetime.now()
    print("START:", start_time)
    print("calculation starts")

    """scenario2_supply_demand()"""
    scenario3_other_costs()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)
