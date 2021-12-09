from datetime import datetime
import numpy as np
import pandas as pd

import projects
import power_curves
from fun import ran_gen_float
from fun import random_from_prob_dist
from german_auctions import auctions_supply_demand
import german_auctions


def scenario1():
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    """[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]"""

    Master_storage = projects.ProjectsStorage(demand=35, name="scenario1",
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
    Master_storage.export(projects_export=True)

def scenario2():
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    """[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]"""

    Master_storage = projects.ProjectsStorage(demand=31, name="scenario2",
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
    Master_storage.export(projects_export=True)


def scenario3_supply_demand():
    df_results = pd.DataFrame()

    number_of_projects = 41
    ref_yield_scenarios = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

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

    writer = pd.ExcelWriter("scenario3_supply_demand.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario4_other_costs():
    df_results = pd.DataFrame()

    iterations = 10000
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

    for iii in demand_scenarios:
        demand = iii

        Master_storage = projects.ProjectsStorage(demand=demand, name="scenario4_other_costs",
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  project_size_adjustment=3)

        for ii in range(iterations):
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

            Master_storage.auction_results()
            Master_storage.delete_projects()
            Master_storage.iteration += 1

        df_results = df_results.append(Master_storage.return_results())

    writer = pd.ExcelWriter("scenario4_other_costs.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario5_other_costs_production():
    df_results = pd.DataFrame()

    iterations = 10000
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

    for iii in demand_scenarios:
        demand = iii

        Master_storage = projects.ProjectsStorage(demand=demand, name="scenario5_other_costs_production",
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  project_size_adjustment=3)

        for ii in range(iterations):
            ws_list = np.linspace(start=5, stop=9, num=number_of_projects, endpoint=True, retstep=False, dtype=None)

            for i in range(number_of_projects):
                other_costs = ran_gen_float(lower_limit=0.8, upper_limit=1.2)
                other_prod = ran_gen_float(lower_limit=0.9, upper_limit=1.1)

                Master_storage.add_project(base_lcoe=50,
                                           ws100=ws_list[i],
                                           hub_height=128,
                                           installed_capacity=3,
                                           power_curve=power_curves.Enercon_E115,
                                           turbine_name="Enercon_E115",
                                           other_cost=other_costs,
                                           other_production=other_prod)

            Master_storage.auction_results()
            Master_storage.delete_projects()
            Master_storage.iteration += 1

        df_results = df_results.append(Master_storage.return_results())

    writer = pd.ExcelWriter("scenario5_other_costs_production.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario6_german_auctions():
    writer = pd.ExcelWriter("scenario6_german_auctions.xlsx", engine="xlsxwriter")

    df_results = pd.DataFrame()
    iterations = 5000
    ref_yield_scenarios = [0, 1, 1.5]

    distributions = [german_auctions.uniform, german_auctions.A_2015_to_2018]

    for iv in distributions:

    # submitted/won/max bid/average project
        for iii in auctions_supply_demand:

            number_of_projects = auctions_supply_demand[iii][0]
            demand = auctions_supply_demand[iii][1]
            max_bid_possible = auctions_supply_demand[iii][2]
            project_size_adjustment = auctions_supply_demand[iii][3]

            Master_storage = projects.ProjectsStorage(demand=demand, name="{0}".format(str(iii)),
                                                      ref_yield_scenarios=ref_yield_scenarios,
                                                      max_bid_possible=max_bid_possible,
                                                      project_size_adjustment=project_size_adjustment,
                                                      ws_dist=iv["name"])

            for ii in range(iterations):
                ws_list = []
                for w in range(number_of_projects):
                    ws_list.append(random_from_prob_dist(input_probabilities=iv))

                for i in range(number_of_projects):
                    other_costs = ran_gen_float(lower_limit=0.8, upper_limit=1.2)
                    other_prod = ran_gen_float(lower_limit=0.9, upper_limit=1.1)

                    Master_storage.add_project(base_lcoe=50,
                                               ws100=ws_list[i],
                                               hub_height=128,
                                               installed_capacity=3,
                                               power_curve=power_curves.Enercon_E115,
                                               turbine_name="Enercon_E115",
                                               other_cost=other_costs,
                                               other_production=other_prod)

                Master_storage.auction_results()
                Master_storage.delete_projects()
                Master_storage.iteration += 1

            df_results = df_results.append(Master_storage.return_results())

        df_results.to_excel(writer, sheet_name=(iv["name"]))

    writer.save()


if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()

    scenario6_german_auctions()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

