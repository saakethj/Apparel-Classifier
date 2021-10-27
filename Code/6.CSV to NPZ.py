# Store the labels with .npz
import pandas as pd
import numpy as np

dataset_csv = pd.read_csv("E:\ANN PROJECT/Datasets/Train labels.csv", usecols=["Labels"])
columns_to_numpy = dataset_csv.loc[:, "Labels"]
np.savez("E:/ANN PROJECT/Datasets/Train labels.npz", Y_train=columns_to_numpy)