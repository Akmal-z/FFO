# app.py

import streamlit as st
import pandas as pd
from data_loader import load_dataset
from ffo import firefly_optimization

st.set_page_config(layout="wide")
st.title("🔥 FFO – Monte Carlo Staff Scheduling")

# Load data
demand_matrix = load_dataset()
st.subheader("Monte Carlo Demand Matrix")
st.dataframe(demand_matrix)

# Sidebar
day = st.sidebar.selectbox("Select Day", demand_matrix.index)
pop = st.sidebar.slider("Population Size", 5, 30, 15)
iters = st.sidebar.slider("Iterations", 20, 200, 100)
alpha = st.sidebar.slider("Alpha", 0.0, 1.0, 0.3)
beta = st.sidebar.slider("Beta", 0.1, 1.0, 0.6)

demand = demand_matrix.loc[day].values

if st.button("Run FFO"):
    solution, history, metrics = firefly_optimization(
        demand, pop, iters, alpha, beta
    )

    st.success("Best BALANCED solution selected")

    st.subheader("Penalty Breakdown")
    st.write(metrics)

    st.subheader(f"Schedule for Day {day}")
    result = pd.DataFrame({
        "Time Period": range(1, len(demand)+1),
        "Demand": demand,
        "Staff Assigned": solution,
        "Deviation": abs(solution - demand)
    })
    st.dataframe(result)

    st.subheader("Global Fitness Convergence")
    st.line_chart(history)
