import cv2
from matplotlib import pyplot as plt

image = cv2.imread("D:\klods\CTE309\lab5\lenna.png")
greyImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("D:\klods\CTE309\lab5\GsLenna.jpg",greyImg)
cv2.imshow("JustGray",greyImg)
histg = cv2.calcHist([greyImg],[0],None,[256], [0,256])
plt.plot(histg, color='k')
plt.xlim([0, 256])
plt.title('brightness histogram')
plt.xlabel("pixel value")
plt.ylabel("pixel Count")
plt.show()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(greyImg)
print("min value:",min_val)
print("max value:",max_val)
# linear image correction
for i in range(greyImg.shape[0]):
    for j in range(greyImg.shape[1]):
        greyImg[i,j]=(greyImg[i,j]-min_val)*((255-0)/(max_val-min_val))
        
histg = cv2.calcHist([greyImg],[0],None,[256], [0,256])
plt.plot(histg, color='k')
plt.xlim([0, 256])
plt.title('Corrected brightness histogram')
plt.xlabel("pixel value")
plt.ylabel("pixel Count")
plt.show()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(greyImg)
print()
print("min value:",min_val)
print("max value:",max_val)
cv2.imshow("CorrectedGray",greyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()