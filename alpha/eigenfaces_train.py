import os
import cv2
import numpy as np

PATH = 'Images'

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    
    return gray[y:y+w, x:x+h], faces[0]


def train(model):
    subject_dir_path = PATH + "/u" + str(model)
    subject_images_names = os.listdir(subject_dir_path)

    faces = []
    labels = []
    label = model

    for image_name in subject_images_names:
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            
            face, rect = detect_face(image)
            # cv2.imshow(image_name, cv2.resize(face, (400, 500)))
            # cv2.waitKey(500)
            
            if face is not None:
                faces.append(face)
                labels.append(label)
    
    print(len(labels))
    return faces, labels


def train_and_save(user_id):
    faces, labels = train(user_id)

    # For Fisherfaces
    # faces2, labels2 = train(2)
    # faces.extend(faces2)
    # labels.extend(labels2)

    width_d, height_d = 280, 280
    resized = [cv2.resize(face, (width_d, height_d)) for face in faces]

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    # face_recognizer = cv2.face.FisherFaceRecognizer_create()
    face_recognizer.train(resized, np.array(labels))
    face_recognizer.write(f'trained_data/u{user_id}.txt')

train_and_save(1)