import cv2
import face_recognition

def show_webcam():
    cam = cv2.VideoCapture(0)
    if not (cam.isOpened()):
        print("Could not open video device")
        return
    var = True
    while True:
        _, img = cam.read()
        small_frame = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        if var:
            face_locations = face_recognition.face_locations(small_frame)
            for (top, right, bottom, left) in face_locations:
                left *=2
                top *=2
                right *=2
                bottom *= 2
                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(img, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "hola", (left + 6, bottom - 6),cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    
        cv2.imshow('cam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
        var != var
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()