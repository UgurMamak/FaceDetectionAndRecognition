import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('XMLDocuments\\haarcascade-frontalface-default.xml')
i=0

kisi_id=input('ID numarası giriniz:')
kisi_ad=input('isim giriniz:')
while True:
    _, img =cam.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #resmi griye çevirdik.
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        #tespit edilen yüzü yuz verileri klasörüne kaydeder. geniş alan aldık o yüzden offset kullanıldı
        cv2.imwrite("yuzler/"+kisi_ad+"-" + kisi_id + '.' + str(i) + ".jpg", gray[y:y + h , x :x + w])
        cv2.rectangle(img, (x , y), (x + w, y + h), (225, 0, 0), 2)
        cv2.imshow('resim', img[y :y + h, x :x + w])
        cv2.waitKey(100)
    if i>1:#kişinin algılanan 20 tane resmini yuzler klasörüne kaydettik.
        cam.release()
        cv2.destroyAllWindows()
        break

