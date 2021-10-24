# generate and save file
"""Converting the original images located dataset directory to  Numpy arrays(.npz files). 
   Arrays store the pixel values of the respective image which later 
   are loaded to variables and used to retrieve in the model."""

from PIL import Image
import os
import numpy as np

path_to_files = "E:/dummy/test set/"
vectorized_images = []

for _, file in enumerate(os.listdir(path_to_files)):
    image = Image.open(path_to_files + file)
    image_array = np.array(image)
    vectorized_images.append(image_array)

# Save the format as .npz and store them in different variables which later can be useful to load in the model
np.savez("E:/dummy/test_images.npy", X_test=vectorized_images)
