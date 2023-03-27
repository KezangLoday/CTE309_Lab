import cv2
import numpy as np

image = cv2.imread('D:\klods\CTE309\lab2\sample.jpg')
cv2.imshow("samplepic",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#properties of the image
height , width, channel = image.shape
print("---properties---")
print("height:", height)
print("width:", width)
print("channel:", channel)

#greyscaleimage
greyImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("samplepicgrey",greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


height, width = greyImg.shape
square_size = min(height, width)

# Calculate the top-left corner of the square portion
top = int((height - square_size) / 2)
left = int((width - square_size) / 2)

# Slice the square portion from the grayscale image
lab1 = greyImg[top:top+square_size, left:left+square_size]

# Display the square portion
cv2.imshow("lab1img", lab1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#properties on textfile
ht, wt = lab1.shape
ch = 1; #for greyscale channel is 1
file = open('properties.txt',"w")
file.write(f'height: {ht}\n')
file.write(f'width: {wt}\n')
file.write(f'channel: {ch}\n')
file.write(f"Image resolution: {ht}x{wt}")
file.close()

#white pixel count
whitePixel = np.sum(lab1 == 255)
print("---white---")
print("White Pixel Count: ", whitePixel)
cv2.imshow("samplepic",lab1)

#white pixel to black
greyImg[greyImg >= 220] = 0
cv2.imshow("white2black", lab1)
cv2.waitKey(0)
cv2.destroyAllWindows