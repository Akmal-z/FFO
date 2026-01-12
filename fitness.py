import numpy as np
from config import SHIFT_LENGTH, MIN_STAFF, W_SHORTAGE, W_WORKLOAD, W_MINSTAFF

def evaluate_firefly(staff, demand):
    staff = np.array(staff)

    # HARD 1: Shortage
    shortage = np.maximum(0, demand - staff)
    P_shortage = np.sum(shortage) * W_SHORTAGE

    # HARD 2: Workload balance
    workload = staff * SHIFT_LENGTH
    avg = np.mean(workload)
    P_workload = np.sum(np.abs(workload - avg)) * W_WORKLOAD

    # SOFT: Minimum staff
    total_staff = np.sum(staff)
    P_soft = 0
    if total_staff < MIN_STAFF:
        P_soft = (MIN_STAFF - total_staff) * W_MINSTAFF

    global_fitness = P_shortage + P_workload + P_soft

    return {
        "global": global_fitness,
        "shortage": P_shortage,
        "workload": P_workload
    }
