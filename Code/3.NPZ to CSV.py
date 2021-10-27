# load and use file
# Variables x_train & x_train are used to load the dataset
import numpy as np
import pandas as pd

path = "E:/dummy/NPZ files/T-shirts.npz"
with np.load(path) as data:
    # load the data using stored variables 'X_train'
    train_data = data['X_train'] 
    #Reshape the numpy format having the exact number of rows as no of images and no of columns as pixel values
    converted_image = train_data.reshape(2600, 784)
    # Convert the numpy reshaped format to dataframe and save to csv
    a = np.asarray(converted_image)
    pd.DataFrame(a).to_csv("E:/dummy/CSV files/T-shirts.csv")    






