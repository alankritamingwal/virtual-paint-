# INTRODUCTION 
Sketching On Air is possible through our trending technology namely open cv , python. Open cv is mainly known as an open source computer vision and machine learning software . The library has more than 2400 best algorithms, which includes a comprehensive set of classic and state-of-the-art computer vision and machine learning algorithms. Most of these algorithms are used to detect and recognize faces, identify objects, classify human activities in videos track camera movements, track moving objects and , extract 3D ones. In this project we are performing the morphological operations are a set of operations that process images based on shapes. These apply a structuring element to an input image and generate an output image. The very basic morphological operations are two: Erosion and Dilation. 

Erosion:- • Eliminates away the boundaries of foreground object. 
• Mainly used to diminish the features of an image.

Dilation:- • Mostly increases the object area. 
• Used to make the features get elevated




# OBJECTIVE
• To create a virtual canvas to sketch.

• To detect the any object as a color marker. 



# METHODOLOGY
• The frames are read and convert the captured frames to HSV color space (Easy for color detection).

 • Make the canvas frame and put the respective link buttons on it. • Now, Set the track bar values for finding the mask of the colored marker.

 • Preprocessing of the mask is done with morphological operations (Eroding & Dilation). 

• The next step goes on like this by, Detecting the contours, finding the center coordinates of large contour and keep storing them in the array for next frames (Arrays for drawing points on the canvass). 

• Finally, draw the points stored in an array on the frames and canvas



![](2022-10-11%20.png)
