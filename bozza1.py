import numpy as np
import cv2
from matplotlib import pyplot as plt

#### LOAD and show IMAGE
img_name="d_18"
img_color = cv2.imread('cap-inspection-images/project_1_liner_inspection/'+img_name+'.bmp')
#img_color = cv2.imread('cap-inspection-images/project_1_liner_inspection/g_01.bmp')
img = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,cmap='gray',vmin=0,vmax=255)


#### histogram 
hist, bins = np.histogram(img.flatten(), 256, [0,256])

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
img_cl = clahe.apply(img)
img_blur = cv2.GaussianBlur(img_cl,(7,7),1.5)

circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT, 1, 40,param1=120,param2=80) # ok per trovare esterno dei tappi
# param1: threshold della differenza del gradiente (+alto = colori + diversi) (per il canny "integrato") - + alta mi trova solo il cerchio esterno
# param2 : perfezione del cerchio

##### tuned so that it finds only one circle

center = (circles[0][0][0],circles[0][0][1])
radius = circles[0][0][2]
cv2.circle(img_color,(int(center[0]),int(center[1])),int(radius),color=(0, 255, 0),thickness=2)
cv2.circle(img_color,(int(center[0]),int(center[1])),int(2),color=(0, 255, 0),thickness=2)
info_cap="CAP OUTLINE - center: x= "+str(center[0])+" y= "+str(center[1])+" , radius= "+str(radius) 
print("CAP OUTLINE - center: x= ", center[0]," y= ",center[1]," , radius= ",radius )
plt.imshow(img_color)


edges = cv2.Canny(img_blur,60,120,apertureSize = 3)

plt.figure(2)
plt.title("Edge map")
plt.imshow(edges,cmap='gray',vmin=0,vmax=255)
plt.axis('off')


edges = cv2.Canny(img_blur,50,100,apertureSize = 3)

plt.figure(3)
plt.title("Edge map of ROI")
plt.imshow(edges,cmap='gray',vmin=0,vmax=255)
plt.axis('off')


circles_in = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT, 1, 50,param1=100,param2=80,maxRadius=int(radius*0.9))

if circles_in is not None and len(circles_in) > 0:

    #print(circles, circles.shape)
    for c in circles_in[0,:] : 
        cv2.circle(img_color,(int(c[0]),int(c[1])),int(c[2]),color=(255, 0, 0),thickness=2)
        cv2.circle(img_color,(int(c[0]),int(c[1])),int(2),color=(255,0, 0),thickness=2)
        print("LINER - center (in roi pic): x= ", c[0]," y= ",c[1]," - center (in full pic): x= ", c[0]," y= ",c[1]," , radius= ",c[2])
        info_liner="LINER - center : x= "+ str(c[0])+" y= "+str(c[1])+" , radius= "+str(c[2])

    plt.figure(4)
    plt.imshow(img_color)
else:
    print("NO CIRCLES")

plt.show() 







####### TASK 2:  Outline the liner by generating a circle that fits the liner border (see Figure 5). For each image the program should record the position of the center of the liner and the diameter of the liner. ###############




#### PRINT RESULTS

