import cv2
import numpy as np

image = cv2.imread('D:\klods\CTE309\lab4\lenna.png')
cv2.imshow('lenna',image)

height, width = image.shape[:2]

random_pix = np.random.randint(0, min(height,width), size=(10,2))
count=1
with open("neighbours.txt", "w") as f:
    count=1
    for coord in random_pix:
        x, y = coord 
        print("{}-Coordinate ({}, {}): {}".format(count, x, y, image[x][y]))
        print("Four Neighbours")
        print("Coordinate ({}, {}): {}".format(x+1, y, image[x+1][y]))
        print("Coordinate ({}, {}): {}".format(x-1, y, image[x-1][y]))
        print("Coordinate ({}, {}): {}".format(x, y+1, image[x][y+1]))
        print("Coordinate ({}, {}): {}".format(x, y-1, image[x][y-1 ]))
        print()
        
        f.write("{}-Coordinate ({}, {}): {}\n".format(count, x, y, image[x][y]))
        f.write("Four Neighbours:\n")
        f.write("Coordinate ({}, {}): {}\n".format(x+1, y, image[x+1][y]))
        f.write("Coordinate ({}, {}): {}\n".format(x-1, y, image[x-1][y]))
        f.write("Coordinate ({}, {}): {}\n".format(x, y+1, image[x][y+1]))
        f.write("Coordinate ({}, {}): {}\n\n".format(x, y-1, image[x][y-1 ]))
        count=count+1