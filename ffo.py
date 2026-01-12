# ffo.py

import numpy as np
from fitness import evaluate_firefly

def firefly_optimization(demand, pop_size, iterations, alpha, beta):
    T = len(demand)

    fireflies = np.random.randint(0, 10, size=(pop_size, T))
    metrics_list = []
    history = []

    for _ in range(iterations):
        metrics_list = [
            evaluate_firefly(f, demand) for f in fireflies
        ]

        for i in range(pop_size):
            for j in range(pop_size):
                if metrics_list[j]["global"] < metrics_list[i]["global"]:
                    fireflies[i] += (
                        beta * (fireflies[j] - fireflies[i]) +
                        alpha * np.random.randn(T)
                    )
                    fireflies[i] = np.clip(fireflies[i], 0, None)

        history.append(min(m["global"] for m in metrics_list))

    # Best balanced (deviation vs workload)
    balance = [
        abs(m["deviation"] - m["workload"]) for m in metrics_list
    ]
    best_idx = int(np.argmin(balance))

    return fireflies[best_idx], history, metrics_list[best_idx]
