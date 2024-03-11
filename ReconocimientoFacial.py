import cv2
import os
from dotenv import load_dotenv


load_dotenv()


def detectFace():
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('modeloLBPHFace.xml')
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    captures = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        captures += 1

        if len(faces) != 0:
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150),
                                 interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            			
            if result[1] < 60:
                print(result[1])
                return True

        if captures == 35:
            break

    cap.release()
    cv2.destroyAllWindows()
    return False