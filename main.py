from datetime import datetime
import numpy as np
import pandas as pd

import projects
import power_curves
from fun import ran_gen_float
from german_auctions import auctions_supply_demand
from storage import Storage


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
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

    # submitted/won/max bid/average project
    for ii in range(1, number_of_projects+1):
        demand = ii

        Master_storage = projects.ProjectsStorage(demand=demand, name="{0}".format(str(ii)),
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  project_size_adjustment=3)

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

    writer = pd.ExcelWriter("scenario3_supply_demand.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario4_other_costs():
    df_results = pd.DataFrame()

    iterations = 100
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

    for iii in range(1, number_of_projects+1):
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


def scenario3_german_auctions():
    df_results = pd.DataFrame()
    iterations = 10000
    ref_yield_scenarios = [0, 1, 1.5]

    # submitted/won/max bid/average project
    for iii in auctions_supply_demand:

        number_of_projects = auctions_supply_demand[iii][0]
        demand = auctions_supply_demand[iii][1]
        max_bid_possible = auctions_supply_demand[iii][2]
        project_size_adjustment = auctions_supply_demand[iii][3]

        Master_storage = projects.ProjectsStorage(demand=demand, name="{0}".format(str(iii)),
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  max_bid_possible=max_bid_possible,
                                                  project_size_adjustment=project_size_adjustment)

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

    writer = pd.ExcelWriter("scenario3_german_auctions.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def test():
    number_of_projects = 3
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    """[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]"""

    Master_storage = projects.ProjectsStorage(demand=4, name="test",
                                              ref_yield_scenarios=ref_yield_scenarios,)

    ws_list = np.linspace(start=5, stop=9, num=number_of_projects, endpoint=True, retstep=False, dtype=None)

    for i in range(number_of_projects):
        Master_storage.add_project(base_lcoe=50,
                                   ws100=ws_list[i],
                                   hub_height=128,
                                   installed_capacity=3,
                                   power_curve=power_curves.Enercon_E115,
                                   turbine_name="Enercon_E115",
                                   other_cost=1.8,
                                   other_production=1)

    Master_storage.auction_results()
    Master_storage.export(projects_export=True)


if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()

    """
    scenario1()
    scenario2_other_costs()
    scenario3_german_auctions()
    test()
    scenario3_german_auctions()
    scenario2()

    scenario3_supply_demand()
    """

    scenario4_other_costs()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

