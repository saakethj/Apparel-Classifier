# generate and save file
"""Converting the original images in dataset to  Numpy arrays. 
   Arrays store the pixel values of the respective image which later 
   are loaded to variables and used in the model."""

from PIL import Image
import os
import numpy as np

# Include the path of images which need to be converted
path_to_files = "E:/ANN PROJECT/Datasets/fashion-dataset/test set/"    
vectorized_images = []

for _, file in enumerate(os.listdir(path_to_files)):
    image = Image.open(path_to_files + file)
    image_array = np.array(image)
    vectorized_images.append(image_array)     
      
# Save the format as npz and for X_train or X_test can be helpful while loading the dataset into the model 
np.savez("E:/ANN PROJECT/Datasets/fashion-dataset/test_images.npz", X_test=vectorized_images)