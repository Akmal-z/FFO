import streamlit as st
import pandas as pd
from ffo import firefly_optimization
from config import DEPARTMENTS, SHIFT_LENGTH

st.title("FFO – Staff Scheduling (6 Departments)")

# Example demand (boleh ganti dengan dataset sebenar)
demand = st.number_input(
    "Daily demand per department",
    min_value=1,
    value=6
)

demand_vector = [demand] * 6

pop = st.slider("Population", 5, 30, 15)
iters = st.slider("Iterations", 50, 300, 100)
alpha = st.slider("Alpha", 0.0, 1.0, 0.3)
beta = st.slider("Beta", 0.1, 1.0, 0.6)

if st.button("Run FFO"):
    best, history, metrics = firefly_optimization(
        demand_vector, pop, iters, alpha, beta
    )

    st.subheader("Best BALANCED Solution")
    st.write(metrics)

    table = []
    for i, s in enumerate(best):
        table.append({
            "Department": i + 1,
            "Staff Assigned": s,
            "Shift Length (period)": SHIFT_LENGTH,
            "Total Working Hours": SHIFT_LENGTH * 0.5
        })

    st.dataframe(pd.DataFrame(table))
    st.line_chart(history)
