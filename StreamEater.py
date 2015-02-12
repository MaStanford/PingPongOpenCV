__author__ = 'm.stanford'

import cv2
from Shapes import Circles, Lines
cap = cv2.VideoCapture(0)
#cap.open('rtmp://flash.oit.duke.edu/vod/_definst_/test/Wildlife2.flv')

circlesObj = Circles.Circles()
linesObj = Lines.Lines()

'''Main loop to read from camera'''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Gray scale the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect and draw circles
    circlesObj.drawCircles(frame, gray)

    #detect and draw lines
    linesObj.drawLines(frame, gray)

    # Display the resulting frame
    cv2.imshow('Video Feed processed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()