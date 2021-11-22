import projects

from datetime import datetime
from joblib import Parallel, delayed
from multiprocessing import cpu_count





if __name__ == '__main__':
    print("calculation starts")
    start_time = datetime.now()


    cpu_no = cpu_count()

    end_time = datetime.now()
    print("calculation ends")
    print("START:", start_time)
    print("END:", end_time)

