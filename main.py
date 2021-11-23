import projects

from datetime import datetime
from joblib import Parallel, delayed
from multiprocessing import cpu_count

import projects


def scenario1():
    number_of_projects = 1
    Master_storage = projects.ProjectsStorage()

    for i in range(number_of_projects):
        Master_storage.add_project()

    print(Master_storage.project_dict)

    for i in Master_storage.project_dict:
        print(Master_storage.project_dict[i].print_project_info())



if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()

    scenario1()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

