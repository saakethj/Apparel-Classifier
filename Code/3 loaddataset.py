# load and use file
# Variables x_train & x_test are used to load the dataset
import numpy as np

path = "E:/ANN PROJECT/Datasets/fashion-dataset/train_images.npz"
with np.load(path) as data:
    # load DataX as train_data
    train_data = data['X_train']
    single_element_data = train_data[2]
    #print(single_element_data)

    print()
    print("Pixels after reshaping: \n")
    multiple_array_to_single_array = single_element_data.reshape(-1)
    print(multiple_array_to_single_array)
