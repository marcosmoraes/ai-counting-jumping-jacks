import cv2
import mediapipe as mp
import math

# Configurar captura de vídeo e inicializar pose detector
video = cv2.VideoCapture('fran.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
count = 0
check = True

while True:
    success, img = video.read()
    if not success:
        break  # Encerra o loop se o vídeo acabou

    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRGB)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    height, width, _ = img.shape

    if points:
        # Normalizar usando a distância entre os ombros como referência
        shoulderRight = points.landmark[pose.PoseLandmark.RIGHT_SHOULDER]
        shoulderLeft = points.landmark[pose.PoseLandmark.LEFT_SHOULDER]
        shoulderDistance = math.hypot(
            (shoulderRight.x - shoulderLeft.x) * width,
            (shoulderRight.y - shoulderLeft.y) * height
        )

        # Posições das mãos
        handRight = points.landmark[pose.PoseLandmark.RIGHT_INDEX]
        handLeft = points.landmark[pose.PoseLandmark.LEFT_INDEX]
        distanceBetweenHands = math.hypot(
            (handRight.x - handLeft.x) * width,
            (handRight.y - handLeft.y) * height
        )

        # Posições dos pés
        footRight = points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX]
        footLeft = points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX]
        distanceBetweenFeets = math.hypot(
            (footRight.x - footLeft.x) * width,
            (footRight.y - footLeft.y) * height
        )

        # Definir limites dinamicamente
        handThreshold = shoulderDistance * 0.8  # Proximidade das mãos (~80% da distância dos ombros)
        feetThreshold = shoulderDistance * 1.2  # Separação dos pés (~120% da distância dos ombros)

        # Lógica para contagem
        if check and distanceBetweenHands <= handThreshold and distanceBetweenFeets >= feetThreshold:
            count += 1
            check = False
        if distanceBetweenHands > handThreshold and distanceBetweenFeets < feetThreshold:
            check = True

        # Exibir contagem no vídeo
        text = f'Count: {count}'
        #cv2.rectangle(img, (20, 250), (290, 120), (255, 0, 0), -1)
        cv2.putText(img, text, (100, 700), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

    cv2.imshow('Resultado', img)
    cv2.waitKey(40)  # Tempo em milissegundos entre frames

video.release()
cv2.destroyAllWindows()
