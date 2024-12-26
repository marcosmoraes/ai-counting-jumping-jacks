import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture('polichinelos.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
count = 0
check = True

while True:
    success, img = video.read()
    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    height, width, _ = img.shape

    if points:
        footRightY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y * height)
        footRightX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x * width)

        footLeftY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y * height)
        footLeftX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x * width)

        handRightY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y * height)
        handRightX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x * width)

        handLeftY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y * height)
        handLeftX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x * width)

        distanceBetweenHands = math.hypot((handRightX - handLeftX), (handRightY - handLeftY))
        distanceBetweenFeets = math.hypot((footRightX - footLeftX), (footRightY - footLeftY))

        print(f'distanceBetweenHands: {distanceBetweenHands} distanceBetweenFeets: {distanceBetweenFeets}')
        if check == True and distanceBetweenHands <= 150 and distanceBetweenFeets >= 150:
            count += 1
            check = False
        if distanceBetweenHands > 150 and distanceBetweenFeets < 150:
            check = True

        print(count)
        text = f'count: {count}'
        cv2.rectangle(img, (20, 250), (290, 120), (255, 0, 0), -1)
        cv2.putText(img, text, (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

    cv2.imshow('Resultado', img)
    cv2.waitKey(40)  # valor em milisegundos
