# ComputerVisionProject
# CAP INSPECTION
# Project 1 – Plastic cap liner inspection
# 1 Introduction
Students should develop a software program to locate the defects in the liner of a plastic cap.
The cap is composed of two parts: the white plastic shell (1) and the silver cardboard liner (2) (see Figure 1).
The image to be processed is similar to that shown in Figure 2.

Figure 1 – The shell is 1, the liner is 2. Figure 2 – The image to process: the shell is 1, the liner is 2.

# 2 First task: cap segmentation and defect detection
Students should:
* Outline the cap by generating a circle that fits the cap mouth (see Figure 3).
HINT: Circle Hough transform can be used to find the mouth circle.
* Search for the defects in each cap. These are the minimum requirements for each image tobe recorded:

- the position of the center of the cap;
- the diameter of the cap mouth;
- the answer to the questions “Is the liner missing?” and “Is the liner incomplete?”;
- Optional requirement: in case of “incomplete liner” the program should outline the straight edge of the incomplete liner (see Figure 4).
HINT: the cap shell with no liner has a different average lightness than the liner. The incomplete liner can be detected inspecting the magnitude of the gradient.

Figure 3 – In magenta the circle fitting the cap mouth. Figure 4 – In red the outline of the "incomplete liner" defect.
Images of good cap: g_01.bmp, g_02.bmp, g_03.bmp, g_04.bmp, g_05.bmp, g_06.bmp.
Images of defective cap due to incomplete liner: d_17.bmp, d_18.bmp, d_19.bmp, d_20.bmp.
Image of defective cap due to missing liner: d_31.bmp.

# 3 Second task: liner segmentation
Students should:
Outline the liner by generating a circle that fits the liner border (see Figure 5).
For each image the program should record the position of the center of the liner and the diameter of the liner.
HINT: Circle Hough transform can be used to find the border of the liner.

Figure 5 – In magenta the circle fitting the border of the liner.
