# generate and save file
"""Converting the original images located dataset directory to  Numpy arrays(.npz files). 
   Arrays store the pixel values of the respective image which later 
   are loaded to variables and used to retrieve in the model."""

from PIL import Image
import os
import numpy as np

path_to_files = "E:/dummy/Dataset/Train Dataset/T-shirts/"
vectorized_images = []

for _, file in enumerate(os.listdir(path_to_files)):
    image = Image.open(path_to_files + file)
    image_array = np.array(image)
    vectorized_images.append(image_array)

# Save the files as .npz extension with variable X_train
np.savez("E:/dummy/NPZ files/T-shirts.npz", X_train=vectorized_images)
