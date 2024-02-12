import cv2
import numpy as np

# Set up video capture parameters
frameWidth = 740
frameHeight = 680
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Define color to be detected in HSV and its corresponding BGR value
myColor = [[83,124,109,134,196,255]]  # HSV range of the color to be detected
mycolorvalue = [[135,206,235]]  # BGR value for marking the detected color

# Initialize an empty list to store detected points
mypoints = []

# Function to find the specified color in the image and mark detected points
def findcolor(img, myColor, mycolorvalue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, mycolorvalue[count], cv2.FILLED)
        if x != 0 and y != 0:
            newpoints.append([x, y, count])
        count += 1
    return newpoints

# Function to draw circles on the result image at detected points
def drawOnCanvas(mypoints, mycolorvalue):
    for point in mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, mycolorvalue[point[2]], cv2.FILLED)

# Function to find contours in a binary image and return the coordinates of the detected point
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

# Main loop for continuously processing video frames
while True:
    # Read a frame from the camera
    success, img = cap.read()
    imgResult = img.copy()  # Make a copy of the original frame for drawing results

    # Find the specified color in the frame and obtain new points
    newpoints = findcolor(img, myColor, mycolorvalue)

    # If new points are detected, append them to 'mypoints'
    if newpoints != 0:
        for new in newpoints:
            mypoints.append(new)

    # If there are points stored in 'mypoints', draw circles on the result image
    if len(mypoints) != 0:
        drawOnCanvas(mypoints, mycolorvalue)

    # Display the result image
    cv2.imshow("Result", imgResult)

    # Wait for a keypress. If 'q' is pressed, break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

