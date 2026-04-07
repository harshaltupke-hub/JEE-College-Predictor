import pandas as pd 
import numpy as np

dfA = pd.read_csv("ADV1ws.csv")
dfM = pd.read_csv("Mainws.csv")

rank_cols = [
    "Closing Rank",
    "Closing Rank 2024",
    "Closing Rank 2023",
    "Closing Rank 2022",
    "Closing Rank 2021",
    "Closing Rank 2020"
]


dfA["mean_rank"] = dfA[rank_cols].mean(axis=1)
dfA["median_rank"] = dfA[rank_cols].median(axis=1)
dfA["std_dev"] = dfA[rank_cols].std(axis=1)
dfA["min_rank"] = dfA[rank_cols].min(axis=1)
dfA["max_rank"] = dfA[rank_cols].max(axis=1)
dfA["lower_limit"] = dfA["median_rank"]-dfA["std_dev"]
dfA["upper_limit"] = dfA["median_rank"]+dfA["std_dev"]

dfM["mean_rank"] = dfM[rank_cols].mean(axis=1)
dfM["median_rank"] = dfM[rank_cols].median(axis=1)
dfM["std_dev"] = dfM[rank_cols].std(axis=1)
dfM["min_rank"] = dfM[rank_cols].min(axis=1)
dfM["max_rank"] = dfM[rank_cols].max(axis=1)
dfM["lower_limit"] = dfM["median_rank"]-dfM["std_dev"]
dfM["upper_limit"] = dfM["median_rank"]+dfM["std_dev"]

dfA.to_csv("ADVlogic.csv")
dfM.to_csv("Mainlogic.csv")