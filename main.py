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


def scenario2_supply_demand():
    df_results = pd.DataFrame()

    number_of_projects = 41
    ref_yield_scenarios = [0, 0.5, 0.99, 1.01, 1.5]
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

    writer = pd.ExcelWriter("scenario2_supply_demand.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario3_other_costs():
    df_results = pd.DataFrame()

    iterations = 1000
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.5, 0.99, 1.01, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

    for iii in demand_scenarios:
        print("demand scenario:", iii)
        demand = iii

        Master_storage = projects.ProjectsStorage(demand=demand, name="scenario3_other_costs",
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

    writer = pd.ExcelWriter("scenario3_other_costs.xlsx", engine="xlsxwriter")
    df_results.to_excel(writer, sheet_name="Results")
    writer.save()


def scenario4_model_distributions():
    df_results = pd.DataFrame()
    writer = pd.ExcelWriter("scenario4_model_distributions.xlsx", engine="xlsxwriter")

    iterations = 1000
    number_of_projects = 41
    ref_yield_scenarios = [0, 0.5, 0.99, 1.01, 1.5]
    demand_scenarios = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41]

    linspace_random = np.linspace(start=0.00001, stop=0.99999, num=number_of_projects, endpoint=True, retstep=False, dtype=None)
    distributions = example_distributions.model_distributions

    for iv in distributions:
        # submitted/won/max bid/average project
        counter = 1
        for iii in demand_scenarios:
            print(iv, "counter", counter, "out of", len(demand_scenarios))
            counter += 1

            Master_storage = projects.ProjectsStorage(demand=iii, name="{0}".format(str(iii)),
                                                      ref_yield_scenarios=ref_yield_scenarios,
                                                      project_size_adjustment=3,
                                                      ws_dist=iv["name"])

            for ii in range(iterations):
                ws_list = []
                for w in linspace_random:
                    ws_list.append(from_prob_dist(input_probabilities=iv, input_number=w))

                for i in range(number_of_projects):
                    other_costs = ran_gen_float(lower_limit=0.8, upper_limit=1.2)
                    other_prod = 1

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
        df_results = pd.DataFrame()

    writer.save()


def scenario5_german_auctions_average():
    writer = pd.ExcelWriter("scenario5_german_auctions.xlsx", engine="xlsxwriter")

    df_results = pd.DataFrame()
    iterations = 10000
    ref_yield_scenarios = [0, 1, 1.5]

    distributions = [german_auctions.A_2015_to_2018]

    for iv in distributions:
    # submitted/won/max bid/average project
        counter = 1
        for iii in auctions_supply_demand:
            print("counter", counter, "out of", len(auctions_supply_demand))
            counter += 1

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
                    other_prod = 1
                    """other_prod = ran_gen_float(lower_limit=0.9, upper_limit=1.1)"""

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
        df_results = pd.DataFrame()

    writer.save()


def scenario8_under_subscribed():
    writer = pd.ExcelWriter("scenario8_under_subscribed.xlsx", engine="xlsxwriter")

    df_results = pd.DataFrame()
    iterations = 10000
    ref_yield_scenarios = [0, 1, 1.5]

    distributions = [german_auctions.A_2015_to_2018]

    for iv in distributions:
    # submitted/won/max bid/average project
        number_of_projects = 100
        demand = 100

        Master_storage = projects.ProjectsStorage(demand=demand, name="100to100",
                                                  ref_yield_scenarios=ref_yield_scenarios,
                                                  project_size_adjustment=3,
                                                  ws_dist=iv["name"])

        for ii in range(iterations):
            ws_list = []
            for w in range(number_of_projects):
                ws_list.append(random_from_prob_dist(input_probabilities=iv))

            for i in range(number_of_projects):
                other_costs = ran_gen_float(lower_limit=0.8, upper_limit=1.2)
                other_prod = 1

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
    start_time = datetime.now()
    print("START:", start_time)
    print("calculation starts")


    scenario1()
    scenario2_supply_demand()
    scenario3_other_costs()
    scenario4_model_distributions()
    scenario5_german_auctions_average()
    scenario8_under_subscribed()


    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

