import projects

from datetime import datetime
from joblib import Parallel, delayed
from multiprocessing import cpu_count
import numpy as np

import projects
import power_curves

def scenario1():
    number_of_projects = 41
    Master_storage = projects.ProjectsStorage(demand=2, name="scenario1")

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

    for i in Master_storage.project_dict:
        print(Master_storage.project_dict[i].print_project_info())

    Master_storage.export()



if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()

    scenario1()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

