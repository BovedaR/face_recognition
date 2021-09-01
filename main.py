import cv2


def show_webcam():
    cam = cv2.VideoCapture(0)
    if not (cam.isOpened()):
        print("Could not open video device")
        return
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()