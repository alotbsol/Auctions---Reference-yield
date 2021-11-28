from datetime import datetime
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from multiprocessing import cpu_count

import projects
import power_curves
from fun import ran_gen_float
from german_auctions import auctions_supply_demand
from storage import Storage

storage_german_a = Storage(name="German_Auctions_multi")


def scenario3_german_auctions_multi(iterations=1, process_id=1):
    ref_yield_scenarios = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

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
                                                  process_id=process_id )

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

        storage_german_a.data_in(data_in=Master_storage.return_results())


def multi_german_auctions():
    iterations = 40

    cpu_no = cpu_count()
    if cpu_no > iterations:
        cpu_no = 1

    it_per_cpu = round(iterations/cpu_no)

    print(it_per_cpu)
    print("cpus", cpu_no)
    left_iter = iterations - (it_per_cpu*cpu_no)
    print(left_iter)

    Parallel(n_jobs=cpu_no, require='sharedmem')(delayed(scenario3_german_auctions_multi)(iterations=it_per_cpu,
                                                                                          process_id=w)
                                                 for w in range(cpu_no))



    print("done")
    storage_german_a.data_export()


if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()

    multi_german_auctions()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)