import cv2
import time
import face_recognition

def take(name):
    print("Initializing...")
    cam = cv2.VideoCapture(0)
    if not (cam.isOpened()):
        print("Could not open video device")
        return

    out = cv2.VideoWriter(f'videos/{name}.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (320,320))

    print("Complete. Press P to start recording.")
    while True:
        cv2.imshow('cam', cam.read()[1])
        if cv2.waitKey(1) == ord('p'):
            print("Recording started.")
            count = 0
            while count < 30:
                _, frame = cam.read()

                face = face_recognition.face_locations(frame)
                if face  != []:
                    top, right, bottom, left = face[0]

                    out.write(cv2.resize(frame[top:bottom, left:right], (320,320)))
                    count+=1
                    print(f"{count}/30")
                    cv2.imshow('cam', frame)
                
                if cv2.waitKey(1) == 27:
                    print("Recording ended.")
                    break
            break
        
    cv2.destroyAllWindows()