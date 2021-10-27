# Converting the images from RGB to Grayscale with pixel values ranging from 0-255

import cv2
import glob
import os

os.mkdir("E:/ANN PROJECT/Datasets/fashion-dataset/Categorized Dataset/Shirts/grayscale_shirts/")
images_path = glob.glob("E:/ANN PROJECT/Datasets/fashion-dataset/Categorized Dataset/Shirts/With & without people/*.jpg")

i = 0
picnum = 1
for image in images_path:
    img = cv2.imread(image)
    grayscale_images = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Images', grayscale_images)
    cv2.imwrite("E:/ANN PROJECT/Datasets/fashion-dataset/Categorized Dataset/Shirts/grayscale_shirts/" + str(picnum) + '.jpg',grayscale_images)
    i += 1
    picnum += 1

cv2.waitKey(600)
cv2.destroyAllWindows()
