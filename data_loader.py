# data_loader.py

import pandas as pd

def load_dataset(path="Monte Carlo Simulator.xlsx"):
    df = pd.read_excel(path, header=None)

    # Locate demand table (based on structure you uploaded)
    start_row = df[df.iloc[:,1] == "Day"].index[0] + 1

    demand_df = df.iloc[start_row:start_row+7, 1:26]
    demand_df.columns = range(1, 26)   # Time periods
    demand_df.index = range(1, 8)      # Days

    demand_df = demand_df.astype(float)

    return demand_df
