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


def scenario6_german_auctions_uniform():
    writer = pd.ExcelWriter("scenario6_german_auctions_uniform.xlsx", engine="xlsxwriter")

    df_results = pd.DataFrame()
    iterations = 10000
    ref_yield_scenarios = [0, 1, 1.5]

    distributions = [german_auctions.uniform]

    for iv in distributions:
        print(iv)
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


def scenario7_german_auctions_quartals():
    writer = pd.ExcelWriter("scenario7_german_auctions_quartals.xlsx", engine="xlsxwriter")

    df_results = pd.DataFrame()
    iterations = 10000
    ref_yield_scenarios = [0, 1, 1.5]

    distributions = german_auctions.quartals

    for iv in distributions:
    # submitted/won/max bid/average project
        counter = 1
        for iii in auctions_supply_demand:
            print(iv, "counter", counter, "out of", len(auctions_supply_demand))
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

