import cv2
import time
import datetime

try:
    cap = cv2.VideoCapture(0)  # 0 used to access system camera
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # xml file used to detect face
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')  # xml file used to detect smile

    while True:
        _, frame = cap.read()
        original_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting image to gray for easy detection of smile

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y + h, x:x + w]
            gray_roi = gray[y:y + h, x:x + w]

            smiles = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)

            if len(smiles) > 0:  # Check if at least one smile is detected
                for (x1, y1, w1, h1) in smiles:
                    cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)

                    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    file_name = f'selfie-{time_stamp}.png'  # saving selfie
                    cv2.imwrite(file_name, original_frame)
                    print("Selfie Captured!")
   
                    time.sleep(2)

        cv2.imshow('Auto Selfie', frame)

        if cv2.waitKey(10) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print("An exception occurred:", e)



"""
import cv2
import time
import datetime

try:
    cap = cv2.VideoCapture(0)  # 0 used to access system camera
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #('haarcascade_frontalcatface_default.xml')   xml file used to detect face
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')  # xml file used to detect smile

    while True:
        _, frame = cap.read()
        original_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converting image to gray for easy detection of smile

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y + h, x:x + w]
            gray_roi = gray[y:y + h, x:x + w]

            smiles = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)

            for (x1, y1, w1, h1) in smiles:
                cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)

                # Calculate smile detection confidence
                smile_confidence = (w1 * h1) / (w * h)

                if smile_confidence > 0.5:  # Adjust this threshold as needed
                    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    file_name = f'selfie-{time_stamp}.png'  # saving selfie
                    cv2.imwrite(file_name, original_frame)
                    print("Selfie Captured!")

        cv2.imshow('Auto Selfie', frame)

        if cv2.waitKey(10) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print("An exception occurred:", e)



"""

"""
import cv2
import time
import datetime
cap = cv2.VideoCapture(0)  #0 used to access system camera
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #xml file used to detect face
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')  #xml file used to detect smile
while True: 
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #converting image to gray for easy detection of smile
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'selfie-{time_stamp}.png'  #saving selfie 
            cv2.imwrite(file_name, original_frame)
            print("Selfie Captured!")
            time.sleep(2)
    cv2.imshow('Auto Selfie', frame)
    if cv2.waitKey(10) == ord('q'):
        break
"""