from ast import Index
import numpy as np
from numpy.testing._private.utils import print_assert_equal
import pandas as pd

csv_to_npz = pd.read_csv("E:/ANN PROJECT/Datasets/Train labels.csv")
csv_without_indexcolumn = csv_to_npz.drop('Labels', inplace=True, axis=1)
csv_to_npz.to_csv("E:/dummy/CSV files/final train images.csv",  index=False) 