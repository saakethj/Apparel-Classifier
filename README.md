# Apparel-Classifier
Apparel Classifier is a neural network model that classifies grayscale images of size (28X28)pixels and provides which category of clothing like shirts, T-shirts, Handbags e.tc.
This model uses fasion dataset collected from various sources containing images of clothing('Footwear', 'Handbags', 'Shirts', 'T-shirts'). Te dataset has a total o 10,714 images in total
### Development of dataset
**Train images - 7400**

**Test images - 3314**

First the images were converted to grayscale which has pixel values ranging form 0-256 then the grayscale images are pixelized to 28x28 pixels.

![1001](https://user-images.githubusercontent.com/76273604/144008638-7e3008a1-f914-4d85-97df-f4cf0829f7f8.png)

After pixelizing the images are compressed to .npz which stores the pixel values in 2-D array(test and train images) 

These .npz files are later made to .csv and labelled accordingly to which category they belong(_'Footwear', 'Handbags', 'Shirts', 'T-shirts'_). This categorical data is labelencoded using labelencoder from sklearn and those lables are extracted from the .csv file

So this model dataszet consists of 4 datset files

  1. Train images.npz
  
  2. Train labels.npz
  
  3. Test images.npz
  
  4. Test labels.npz
  
  ### Creating the model
  
  With the help of TensorFlow framework and keras library sequential model is created to create layers, adding optimizers, activation functions, training, testing, etc.,
  
  ```
model = keras.Sequential(
    [
     Flatten(input_shape=(28, 28)),
     # Flatten 28, 28 into single layer having 784 neurons
     Dense(15, activation='relu', name='layer1'),
     #Dense(4, activation='relu', name='layer2'),
     Dense(4) # output layer having exact number neurons as target outputs
    ]
)
  ```
  
 train_images and train_labels are feeded to the model for training and test_images and test_labels are used to test and make predictions
 
 ```
 history = model.fit(train_images, train_labels, epochs=10)
 
 ```
 The train accuracy of the model is around **89%**
 
 The loss for the model is **0.2698**
 
 ### Testing the model
 ```
 test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
 ```
 
 ![accuracy](https://user-images.githubusercontent.com/76273604/144008903-9f358f7d-ef8b-4a6a-95c1-ebaf820d2f34.png)

 The test accuracy of the model is around **85%**
 
 ### Predicting the model
 Among all the categories of clothis this model is able to predict _Footwear, Handbags, T-shirts_ accurately
 
 ![Screenshot 2021-11-30 133704](https://user-images.githubusercontent.com/76273604/144009088-004c3554-f447-4609-a305-58015fd1f35c.png)
