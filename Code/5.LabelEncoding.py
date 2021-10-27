"""" As for the labels whick are categorical data they need to be converted into numeric data
     which each number represents different category in the dataset. Labelencoding converts the
     given column containing categorical data to numeric data. """

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


labelencoding_of_images = pd.read_csv(r"E:/dummy/combined 1.csv")

labelencoder = LabelEncoder()

labelencoding_of_images["Category"] = labelencoder.fit_transform(labelencoding_of_images["Labels"]) 

labelencoding_of_images["Labels"] = labelencoding_of_images["Labels"].astype('category')

labelencoding_of_images["Labels"] = labelencoding_of_images["Labels"].cat.codes

labelencoding_of_images.drop('Category', inplace=True, axis=1)
labelencoding_of_images.to_csv("E:/ANN PROJECT/Datasets/Train labels.csv", index=False)
