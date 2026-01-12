import numpy as np
from fitness import evaluate_firefly

def firefly_optimization(demand, pop, iters, alpha, beta):
    D = len(demand)

    fireflies = np.random.uniform(0, 10, (pop, D))
    history = []

    for _ in range(iters):
        metrics = [evaluate_firefly(f, demand) for f in fireflies]

        for i in range(pop):
            for j in range(pop):
                if metrics[j]["global"] < metrics[i]["global"]:
                    fireflies[i] += (
                        beta * (fireflies[j] - fireflies[i]) +
                        alpha * np.random.randn(D)
                    )
                    fireflies[i] = np.clip(fireflies[i], 0, None)

        history.append(min(m["global"] for m in metrics))

    # MULTI-OBJECTIVE BALANCED SELECTION
    balance = [
        abs(m["shortage"] - m["workload"]) for m in metrics
    ]
    best_idx = np.argmin(balance)

    return np.round(fireflies[best_idx]).astype(int), history, metrics[best_idx]
