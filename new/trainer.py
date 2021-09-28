import cv2
import face_recognition
from datetime import datetime
import os
import pickle


def train(path="videos/"):
    encodings = {}
    videos = os.listdir(path)

    for video in videos:
        print(f"{videos.index(video)+1}/{len(videos)}")
        vid = cv2.VideoCapture(f"{path}{video}")
        name = video.split('.')[0]
        encodings[name] = []
        for _ in range(int(vid.get(cv2.CAP_PROP_FRAME_COUNT))):
            frame = vid.read()[1]
            encodings[name].append(face_recognition.face_encodings(frame, face_recognition.face_locations(frame)))

    file_name = datetime.now().strftime('%H%M%S%f')
    pickle.dump(encodings, open(f"trains/{file_name}", 'ab'))
    return file_name