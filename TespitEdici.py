import cv2


recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/trainer.yml')
cascadePath = "XMLDocuments\\haarcascade-frontalface-default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'

cam = cv2.VideoCapture(1)
while True:
    ret, im =cam.read() # kameradaki görüntüyü aldık.
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)# kameradan alınam görüntüyü griye dönüştürdük.
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        if(tahminEdilenKisi==1):
             tahminEdilenKisi= 'ugur Mamak'
        elif(tahminEdilenKisi == 2):
            tahminEdilenKisi = 'mavili'
        else:
            tahminEdilenKisi= "Bilinmeyen kişi"
        fontFace = cv2.FONT_HERSHEY_SIMPLEX #yazı tipi belirleme
        fontScale = 1
        fontColor = (255, 255, 255)
        cv2.putText(im, str(tahminEdilenKisi), (x, y + h), fontFace, fontScale, fontColor)
        cv2.imshow('im',im)
        cv2.waitKey(10)









