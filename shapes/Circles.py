__author__ = 'm.stanford'
import cv2
import cv2.cv as cv
import numpy as np


class Circles():

    accumulator_threshold = 75
    minCircleDist = 100
    maxCannyThresh = 175
    minRadius = 10
    maxRadius = 0

    def __init__(self):
        pass

    def getCircles(self, img):

        smoothed = cv2.medianBlur(img, 5)
        circles = cv2.HoughCircles(smoothed, cv.CV_HOUGH_GRADIENT, 1
                                   , self.minCircleDist
                                   , param1=self.maxCannyThresh
                                   , param2=self.accumulator_threshold
                                   , minRadius=self.minRadius
                                   , maxRadius=self.maxRadius)
        if circles is None:
            return None

        circles = np.uint16(np.around(circles))
        return circles

    def drawCircles(self, targetFrame, grayFrame):

        circles = self.getCircles(grayFrame)

        if circles is None:
            return

        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(targetFrame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(targetFrame, (i[0], i[1]), 2, (0, 0, 255), 3)
