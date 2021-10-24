""" Extract the column which is converted from categorical to numeric 
    and convert the respected column to numpy array and compress the whole
    array to .npz files """

import pandas as pd
import numpy as np


dataset_csv = pd.read_csv("E:/dummy/final test labels.csv", usecols=["Labels"])
columns_to_numpy = dataset_csv.loc[:, "Labels"]
np.savez("E:/dummy/final test labels.npz", Y_test=columns_to_numpy)