import numpy as np
import pandas as pd

def load_data_for_1():
    arr = np.arange(120).reshape(1, 2, 3, 4, 5).astype("M8[s]")
    np.save("data/1-task-arr1.npy", arr)
    arr = np.arange(1,7,dtype=float).reshape(2, 3)
    np.save("data/1-task-arr2.npy", arr)

    # iris_df
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    iris_df = pd.read_csv(url, header=None, names=column_names)
    iris_df.to_csv("data/iris.csv", index=True)

load_data_for_1()