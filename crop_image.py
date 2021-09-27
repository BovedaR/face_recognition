import cv2
import face_recognition
import os
import numpy as np

def main(img:str) -> bool:
    nparr = np.fromstring(img, np.uint8)
    image = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1

    face_locations = face_recognition.face_locations(image)

    for (top, right, bottom, left) in face_locations:
        img_cropped = img[top:bottom, left:right]

    if img_cropped is not None:
        cv2.imwrite('cropped/', img_cropped)
        return True

    return False
