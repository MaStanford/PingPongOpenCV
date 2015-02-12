__author__ = 'm.stanford'
import numpy as np
import cv2

class Lines():

    minEdge = 200
    maxEdge = 300
    minLineLength = 1000
    maxLineGap = 100
    p = 1
    theta = np.pi/180
    threshhold = 200
    probability = False

    def __init__(self):
        pass

    def getLines(self, grayImage):
        edges = cv2.Canny(grayImage, self.minEdge, self.maxEdge, apertureSize=3, L2gradient=True)

        if self.probability:
            lines = cv2.HoughLinesP(edges, self.p, self.theta, self.threshhold, self.minLineLength, self.maxLineGap)
        else:
            lines = cv2.HoughLines(edges, self.p, self.theta, self.threshhold)

        return lines


    def drawLines(self, targetFrame, grayImage):

        lines = self.getLines(grayImage)

        if self.probability:
            if lines is None:
                pass
                #maxLineGap *= .99
                #minLineLength *= 1.01
            else:
                for x1, y1, x2, y2 in lines[0]:
                    cv2.line(targetFrame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        else:
            if lines is None:
                pass
                #maxLineGap *= .99
                #minLineLength *= 1.01
            else:
                for rho, theta in lines[0]:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))

                    cv2.line(targetFrame, (x1, y1), (x2, y2), (0, 255, 0), 2)