# load the npz file and convert them into csv
import numpy as np
import pandas as pd

path = "E:/dummy/NPZ files/T-shirts.npz"
with np.load(path) as data:
    # load the data using the respective *args
    train_data = data['X_train'] 
    converted_image = train_data.reshape(2600, 784)
    a = np.asarray(converted_image)
    pd.DataFrame(a).to_csv("E:/dummy/CSV files/T-shirts.csv")    