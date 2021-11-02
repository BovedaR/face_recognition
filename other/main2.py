import cv2
import face_recognition
import os

def load_images(path="known/"):
    print("Loading images...")
    images = {i.split('.')[0]: face_recognition.face_encodings(face_recognition.load_image_file(path+i))[0] for i in os.listdir(path)}
    print("Loading complete.")

    return images

def main(images):
    print("Initializing...")
    cam = cv2.VideoCapture(0)

    if not (cam.isOpened()):
        print("Could not open video device")
        return
    print("Complete.")

    this_frame = True

    while True:
        _, frame = cam.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)[:, :, ::-1]
        face_encodings = face_recognition.face_encodings(small_frame, face_recognition.face_locations(small_frame))
        if this_frame:
            for fe in face_encodings:
                matches = face_recognition.compare_faces(list(images.values()), fe)
            
                for i in range(len(matches)):
                    if matches[i]: print(list(images.keys())[i])
                    else: print("unknown")
        this_frame = not this_frame

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

if __name__ == '__main__':
    main(load_images())