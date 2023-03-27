import cv2
import numpy as np
from math import sqrt

image = cv2.imread('D:\klods\CTE309\lab3\lenna.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("lenna",image)
cv2.waitKey(0)
cv2.imwrite("GsLenna.png ",image)
cv2.destroyAllWindows()

#the minMaxLoc() returns four values where second one is the maximun value
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image)
print("---Properties---")
print("Highest valued pixel(with OpenCV):", max_val)

#without using the opencv inbuilt function
max_value = 0
min_value = 255
for i in range(image.shape[0]): # shape[0] returns the height
    for j in range(image.shape[1]): # shape[1] returns the width
        if image[i,j] > max_value:
            max_value = image[i,j]
            high_pixelloc = np.array([i, j])
        if image[i,j] < min_value:
            min_value = image[i,j]
            low_pixelloc = np.array([i, j])
print("Highest valued pixel (without OpenCV):", max_value)
print("Lowest valued pixel :", min_value)

# Calculate Euclidean distance without OpenCV
Eudistance = sqrt((high_pixelloc[0] - low_pixelloc[0]) ** 2 + (high_pixelloc[1] - low_pixelloc[1]) ** 2)
print()
print("---Euclidean distance---")
print("Euclidean distance (without OpenCV): ", Eudistance)

low_pixel = np.array(low_pixelloc) 
high_pixel = np.array(high_pixelloc)

# Calculate Euclidean distance using OpenCV
distance = cv2.norm(low_pixel, high_pixel)
print("Euclidean distance (With OpenCV): ", distance)  
print()

# occurence of lowest value pixel
count=0
for i in range(image.shape[0]): #  
    for j in range(image.shape[1]): 
        if image[i,j] == min_value:
            count=count+1
print("---pixel count---")
print("lowest value pixel count:" , count)    