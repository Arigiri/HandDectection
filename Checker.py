import cv2
import numpy as np

class Road:
    def __init__(self, obj) -> None:
        self.Image = obj
        self.Edge = self.EdgeDetection(obj)
        self.points = self.GetPoints(self.Edge)
        self.threshold = 10

    def EdgeDetection(self, Image):
    # Image = cv2.imread("Hand.png")
        gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, ksize = (5, 5), sigmaX= 0)
        
        canny = cv2.Canny(blur, 100, 200)
        return canny

    def GetPoints(self, Image):
        points = []
        for row in range(Image.shape[0]):
            for col in range(Image.shape[1]):
                intensity = Image[row][col]
                if intensity > 0:
                    points.append((row, col))
        return np.array(points)
    
    def MSE(self, points):
        tempPoints = points.copy()
        RoadPoints = np.copy(self.points)
        while len(tempPoints) < len(RoadPoints):
            tempPoints.append((0, 0))
        tempPoints = np.array(tempPoints)
        MSE = (np.sum((tempPoints - RoadPoints) ** 2) ** (1/2)) / 2
        return MSE
    
    def Checker(self, points):
        MSE = self.MSE(points)
        print(self.points)
        print(MSE)

    def PreCanvas(self):
        edge = np.uint8(self.Edge)
        tempr = np.copy(edge)
        tempg = np.copy(edge)
        edge = cv2.merge((edge, tempg, tempr))
        return edge
    
    def CheckUsingNCC(self, canvas):
        draw = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        
                

# Image = cv2.imread("Objects/circle.png")
# check = Road(Image)
# cv2.imshow("Edge", check.PreCanvas())
# cv2.waitKey()
# cv2.destroyAllWindows()