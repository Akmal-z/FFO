# fitness.py

import numpy as np
from config import *

def evaluate_firefly(solution, demand):
    """
    solution: staff assigned per time period
    demand  : demand per time period
    """

    # Deviation (hard)
    deviation = np.abs(solution - demand)
    deviation_penalty = np.sum(deviation) * W_DEVIATION

    # Workload balance (hard)
    avg = np.mean(solution)
    workload_penalty = np.sum(np.abs(solution - avg)) * W_WORKLOAD

    # Soft: minimum staff
    min_staff_penalty = 0
    if np.sum(solution) < MIN_STAFF:
        min_staff_penalty = (MIN_STAFF - np.sum(solution)) * W_MINSTAFF

    global_fitness = (
        deviation_penalty +
        workload_penalty +
        min_staff_penalty
    )

    return {
        "global": global_fitness,
        "deviation": deviation_penalty,
        "workload": workload_penalty
    }
