"""" The category of the dataset is categorical, data should be converted to numeric data
     with labelling encoding which lables the categorical data. """

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

labelencoding_of_images = pd.read_csv(r"E:\ANN PROJECT\Datasets\fashion-dataset\Test_labels.csv")

labelencoder = LabelEncoder() #Instance of the class LabelEncoder

# Labelencoding the respected categorical column column in the data
labelencoding_of_images["Category"] = labelencoder.fit_transform(labelencoding_of_images["labels"])


# Conversion of datatype of the labelled column in the data
labelencoding_of_images["labels"] = labelencoding_of_images["labels"].astype('category')
#print(labelencoding_of_images.dtypes)

labelencoding_of_images["labels"] = labelencoding_of_images["labels"].cat.codes
print(labelencoding_of_images)

labelencoding_of_images.to_csv('E:/ANN PROJECT/Datasets/test labels.csv', index=False)