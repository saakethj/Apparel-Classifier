# generate and save file
# Compressing the images to .npz format with pixel values of the image

from PIL import Image
import os
import numpy as np

path_to_files = "E:/dummy/Dataset/Train Dataset/T-shirts/"
vectorized_images = []

for _, file in enumerate(os.listdir(path_to_files)):
    image = Image.open(path_to_files + file)
    image_array = np.array(image)
    vectorized_images.append(image_array)

np.savez("E:/dummy/NPZ files/T-shirts.npz", X_train=vectorized_images)
