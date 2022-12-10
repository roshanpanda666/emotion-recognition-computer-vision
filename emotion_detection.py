# importing the dependencies
import cv2

#loading the data

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# detection

def detect(gray,frame):
    face=face_cascade.detectMultiScale(gray,1.3,5)
    smile=smile_cascade.detectMultiScale(gray,2.6,30)
    eye=eye_cascade.detectMultiScale(gray,1.5,7)

    # putting the rectangle

#detecting the face
    if face==():
        cv2.putText(frame,"Face Not detected",(360,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    for(x,y,w,h) in face:
        rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
        if rectangle.any()==True:
            cv2.putText(rectangle,"Face detected",(400,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
#detecting the smile
    if smile==():
        cv2.putText(frame,"normal",(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    for(ex,ey,ew,eh)in smile:
        rectangle2= cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,255,255),1)
        if rectangle2.any()==True:
            cv2.putText(frame,"smiling",(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

#detecting the eyes
    if eye==():
            cv2.putText(frame,"eyes closed",(400,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    for(eex,eey,eew,eeh)in eye:
        rectangle2= cv2.rectangle(frame,(eex,eey),(eex+eew,eey+eeh),(255,255,255),1)

        if rectangle2.any()==True:
            cv2.putText(rectangle2,"eyes opened",(400,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
