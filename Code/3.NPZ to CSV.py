# load and use file
# Variables x_train & x_test are used to load the dataset
import numpy as np
import pandas as pd

path = "E:/dummy/test_images.npz"
with np.load(path) as data:
    # load X_train as train_data, X_test as test_data
    test_data = data['X_test'] 
    #Reshape the numpy format having the exact number of rows as no of images and no of columns as pixel values
    converted_image = test_data.reshape(10, 784)
    # Convert the numpy reshaped format to dataframe and save to csv
    a = np.asarray(converted_image)
    pd.DataFrame(a).to_csv("E:/dummy/test labels.csv")    






