import cv2,os

import numpy as np
from PIL import Image #plıof kütüphanesi yüz tanıma için kullanılır.
re=cv2.face.EigenFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "XMLDocuments\\face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'

def get_images_and_labels(path):
     image_paths = [os.path.join(path, f) for f in os.listdir(path)]
     images = []
     labels = []
     for image_path in image_paths:
         image_pil = Image.open(image_path).convert('L')# görüntüyü griye çevirme yöntemi
         image = np.array(image_pil, 'uint8')# veri tipi dönüşümü
         nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
         print(nbr)
         faces = faceCascade.detectMultiScale(image)
         for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(nbr)
             cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
             cv2.waitKey(10)
     return images, labels


images, labels = get_images_and_labels(path)
cv2.imshow('test',images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.write('training/trainer.yml') #eğitilmiş resimler eklenir
cv2.destroyAllWindows()

