# Transform the csv to numpy array with pixel values
# Store them with .npz
import numpy as np
import pandas as pd

imagescsv_to_array = np.genfromtxt("E:/dummy/CSV files/final train images.csv", delimiter=",", skip_header=1)
reshaped_array = imagescsv_to_array.reshape(7400, 28, 28)
np.savez("E:/ANN PROJECT/Datasets/Train images.npz", X_train=reshaped_array)
