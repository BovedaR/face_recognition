import cv2
import face_recognition
from datetime import datetime
import os
import pickle
from utils import loading_bar

def train(path="videos/"):
    encodings = {}
    videos = os.listdir(path)

    for video in videos:
        vid = cv2.VideoCapture(f"{path}{video}")
        name = video.split('.')[0]
        encodings[name] = []
        frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
        l = loading_bar(frame_count)
        print(name, end='\n\n')
        for _ in range(frame_count):
            frame = vid.read()[1]
            encodings[name].append(face_recognition.face_encodings(frame, face_recognition.face_locations(frame)))
            l.add(1)
            print(l, end='\r')

    file_name = datetime.now().strftime('%H%M%S%f')
    pickle.dump(encodings, open(f"trains/{file_name}", 'ab'))

if __name__ == "__main__":
    train()