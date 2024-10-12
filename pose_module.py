import cv2
import mediapipe as mp
import time
import math
import numpy as np

class poseDetector:
    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.7, trackCon=0.7):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose

        self.pose = self.mpPose.Pose(self.mode, min_detection_confidence=detectionCon, min_tracking_confidence=trackCon)

    def calculate_angle(self, a, b, c):
        a = np.array(a)  # First point
        b = np.array(b)  # Mid point
        c = np.array(c)  # End point

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * (180.0 / np.pi))

        return int(angle)

    def draw_angle_symbols(self, frame, landmarks):
        connections = [
            # Shoulder angles
            (23, 11, 13), (24, 12, 14),
            # Elbow angles
            (11, 13, 15), (12, 14, 16), 
            # Wrist angles
            (13, 15, 19), (14, 16, 20),
            # Knee angles
            (23, 25, 27), (24, 26, 28),
            # Ankle angles
            (31, 27, 25), (32, 28, 26),
        ]

        for connection in connections:
            point1 = (int(landmarks[connection[0]].x * frame.shape[1]), int(landmarks[connection[0]].y * frame.shape[0]))
            point2 = (int(landmarks[connection[1]].x * frame.shape[1]), int(landmarks[connection[1]].y * frame.shape[0]))
            point3 = (int(landmarks[connection[2]].x * frame.shape[1]), int(landmarks[connection[2]].y * frame.shape[0]))

            # Calculate angle between neighboring points
            angle = self.calculate_angle(point1, point2, point3)
            angle_text = f"{angle}*"

            # Display angle at the midpoint of the line
            midpoint = ((point1[0] + point2[0] + point3[0]) // 3, (point1[1] + point2[1] + point3[1]) // 3)
            cv2.putText(frame, angle_text, (midpoint[0] - 10, midpoint[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1, cv2.LINE_AA)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks and draw:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                if id not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20]:  # Skip facial landmarks and fingers
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

            # Manually draw connections, avoiding facial landmarks
            for conn in self.mpPose.POSE_CONNECTIONS:
                if conn[0] > 10 and conn[1] > 10:  # Exclude connections involving facial landmarks
                    pt1 = self.results.pose_landmarks.landmark[conn[0]]
                    pt2 = self.results.pose_landmarks.landmark[conn[1]]
                    x1, y1 = int(pt1.x * w), int(pt1.y * h)
                    x2, y2 = int(pt2.x * w), int(pt2.y * h)
                    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)

            # Draw angle symbols
            self.draw_angle_symbols(img, self.results.pose_landmarks.landmark)

        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3, draw=True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle

def main():
    cap = cv2.VideoCapture(r'dance_videos/right_dance.mp4')
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img, _ = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)

        lm_to_print = 20
        if len(lmList) != 0:
            print(lmList[lm_to_print])
            cv2.circle(img, (lmList[lm_to_print][1], lmList[lm_to_print][2]), 15, (0, 0, 255), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, "FPS: "+str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
