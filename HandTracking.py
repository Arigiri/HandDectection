import cv2
import mediapipe as mp
import time
import numpy as np
import os, random
from Checker import *
 
class handDetector():
    def __init__(self, mode=False, maxHands=1, modelC = 1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelC = modelC
        self.mpHands = mp.solutions.hands
        self.indexFinger = 4
        # self.hands = self.mpHands.
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelC,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
 
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
 
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                                self.mpHands.HAND_CONNECTIONS)
        return img
 
    def findPosition(self, img, handNo=0, draw=True):
 
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
 
        return lmList

def CheckDraw(lmList):
    # return False
    return lmList[8][2] < lmList[6][2]

def GetObjectToShow():
    Path = "Objects/"
    files = os.listdir(Path)
    #Object = random.choice(files)
    Object = "circle.jpg"
    return cv2.imread(Path + Object)

def main():
    pTime = 0
    cTime = 0
    Object = GetObjectToShow()
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    points = []
    Roads = Road(Object)
    cv2.imshow("Target", Object)
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img, draw= True)
        lmList = detector.findPosition(img, draw= False)
        if len(lmList) > 1:
            cv2.circle(img, lmList[8][1:], 15, color = (187, 181,255), thickness= cv2.FILLED)
            # cv2.circle(img, lmList[6][1:], 15, color = (0, 0,255), thickness= cv2.FILLED) #This checker
            if CheckDraw(lmList):
                points.append(lmList[8][1:])
        #Draw Color
        CanvasImage = np.zeros(img.shape, dtype= np.uint8)
        RoadImage = Roads.PreCanvas()
        offsetx = 150
        offsety = 50
        CanvasImage[offsety: offsety + RoadImage.shape[0], offsetx : offsetx + RoadImage.shape[1]] = RoadImage
        NewCanvas = np.zeros(CanvasImage.shape)
        # CanvasImage = cv2.addWeighted(CanvasImage, 1, RoadImage, 0.2, 0)
        for ptIdx in range(len(points) - 1):
            startpoint = points[ptIdx]
            endpoint = points[ptIdx + 1]
            cv2.line(CanvasImage, startpoint, endpoint, color=(255, 255, 255), thickness= 20)
            cv2.line(NewCanvas, startpoint, endpoint, color=(255, 255, 255), thickness= 20)
            
        img = cv2.add(img, CanvasImage)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
 
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        
        #Check if go collect side
        Roads.Checker(points)

        cv2.imshow("Image", img)
        cv2.imshow("Canvas", CanvasImage)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        if key == ord(' '):
            cv2.imwrite("Hand.png", NewCanvas)
        if key == ord('w'):
            points = []
        # if key == ord('e'):
        #     CheckMSE(Object, CanvasImage)



if __name__ == "__main__":
    main()