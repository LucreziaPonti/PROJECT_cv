import numpy as np
import cv2
from matplotlib import pyplot as plt

#### LOAD and show IMAGE
img = cv2.imread('cap-inspection-images/project_1_liner_inspection/d_16.bmp',cv2.IMREAD_GRAYSCALE)
plt.figure(1)
plt.imshow(img,cmap='gray',vmin=0,vmax=255)
#plt.show()

#### histogram 
hist, bins = np.histogram(img.flatten(), 256, [0,256])
plt.figure(2,figsize=[8,4])
plt.stem(hist)
plt.show()

######## TASK 1:  Outline the cap by generating a circle that fits the cap mouth #########

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1, 45)
print(circles)

####### TASK 1.2 : Search for the defects in each cap. ###########










####### TASK 2:  Outline the liner by generating a circle that fits the liner border (see Figure 5). For each image the program should record the position of the center of the liner and the diameter of the liner. ###############




#### PRINT RESULTS

