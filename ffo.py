# ffo.py

import numpy as np
from fitness import evaluate_firefly

def firefly_optimization(demand, pop_size, iterations, alpha, beta):
    T = len(demand)

    # 🔥 IMPORTANT: fireflies as FLOAT
    fireflies = np.random.uniform(
        low=0,
        high=10,
        size=(pop_size, T)
    )

    history = []
    metrics_list = []

    for _ in range(iterations):
        metrics_list = [
            evaluate_firefly(f, demand) for f in fireflies
        ]

        for i in range(pop_size):
            for j in range(pop_size):
                if metrics_list[j]["global"] < metrics_list[i]["global"]:
                    fireflies[i] = (
                        fireflies[i]
                        + beta * (fireflies[j] - fireflies[i])
                        + alpha * np.random.randn(T)
                    )

                    # 🔒 Bound constraint
                    fireflies[i] = np.clip(fireflies[i], 0, None)

        history.append(min(m["global"] for m in metrics_list))

    # 🔥 Multi-objective balanced selection
    balance_scores = [
        abs(m["deviation"] - m["workload"])
        for m in metrics_list
    ]

    best_idx = int(np.argmin(balance_scores))

    # 🔥 Convert to integer staff counts ONLY at the end
    best_solution = np.round(fireflies[best_idx]).astype(int)

    return best_solution, history, metrics_list[best_idx]
