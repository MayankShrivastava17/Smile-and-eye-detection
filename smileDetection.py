import cv2

#loading face and eye cascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    #for face detection
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        r_gray=gray[y:y+h,x:x+w]
        r_color=frame[y:y+h,x:x+w]
        #for eyes detection
        eyes=eye_cascade.detectMultiScale(r_gray, 1.1, 15)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(r_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #for smile detection
        smiles=smile_cascade.detectMultiScale(r_gray, 1.7, 35)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(r_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    return frame
#accessing the webcam
webcam=cv2.VideoCapture(0)

while True:
    _, frame=webcam.read()
    gray=cv2.cvtColor(qrame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Face and Eye Detection',canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()
