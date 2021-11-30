# Apparel-Classifier
Apparel Classifier is a neural network model that classifies grayscale images of size (28X28)pixels and provides which category of clothing like shirts, T-shirts, Handbags e.tc.
This model uses fasion dataset collected from various sources containing images of clothing('Footwear', 'Handbags', 'Shirts', 'T-shirts'). Te dataset has a total o 10,714 images in total
### Development of dataset
**Train images - 7400**

**Test images - 3314**

First the images were converted to grayscale which has pixel values ranging form 0-256 then the grayscale images are pixelized to 28x28 pixels.

After pixelizing the images are compressed to .npz which stores the pixel values in 2-D array(test and train images) 

These .npz files are later made to .csv and labelled accordingly to which category they belong(_'Footwear', 'Handbags', 'Shirts', 'T-shirts'_). This categorical data is labelencoded using labelencoder from sklearn and those lables are extracted from the .csv file

So this model dataszet consists of 4 datset files

  i) Train images.npz
  
  ii) Train labels.npz
  
  iii) Test images.npz
  
  iv) Test labels.npz
  
  ### Creating the model
  
  With the help of TensorFlow framework and keras library sequential model is created to create layers, adding optimizers, activation functions, training, testing, etc.,
  
