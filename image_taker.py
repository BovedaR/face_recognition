import cv2
import face_recognition


def main():
    print("Initializing...")
    cam = cv2.VideoCapture(0)
    if not (cam.isOpened()):
        print("Could not open video device")
        return

    print("Complete.")
    img_cropped = None
    face_locations = []
    offset=0
    while True:
        _, img = cam.read()
        small_frame = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

        face_locations = face_recognition.face_locations(small_frame)
        for (top, right, bottom, left) in face_locations:
            left *=2
            top *=2
            right *=2
            bottom *= 2

            img_cropped = img[top-offset:bottom+offset, left-offset:right+offset]

        if img_cropped is not None:
            cv2.imshow('cam', cv2.resize(img_cropped, (0, 0), fx=2, fy=2))

        if cv2.waitKey(1) == 27:
            name = input("Your name: ")
            cv2.imwrite(f"known/{name}.jpg", img_cropped)
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()