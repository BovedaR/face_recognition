import cv2
import face_recognition
import pickle
import os
import sys
import json
from datetime import datetime

def recognize(pickle_file):
    print("Initializing...")

    encodings = pickle.load(open(f"trains/{pickle_file}", 'rb'))
    cam = cv2.VideoCapture(0)

    dt = datetime.now()
    json_info = {"date": dt.strftime('%d/%m/%Y'), "time": dt.strftime('%H:%M:%S'), "alumnos": {person.split('.')[0]: False for person in encodings.keys()}}
    with open("data.json", 'r') as fp:
        data = json.load(fp)
    data.append(json_info)
    with open("data.json", 'w') as fp: 
        json.dump(data, fp)

    if not (cam.isOpened()):
        print("Could not open video device")
        return
    print("Complete.")

    this_frame = True
    while True:
        _, frame = cam.read()

        face_encodings = face_recognition.face_encodings(frame, face_recognition.face_locations(frame))
        if this_frame and face_encodings != []:
            person = face_encodings[0]
            for name, encoding in encodings.items():
                if not json_info["alumnos"][name]:
                    matches = []
                    for e in encoding:
                        matches.append(face_recognition.compare_faces(e, person))
                    if matches.count([True]) >= 7 and name in list(json_info["alumnos"].keys()):
                        """
                        json_info["alumnos"][name] = datetime.now().strftime('%H-%M')
                        with open("data.json", 'r') as fp:
                            data = json.load(fp)
                        data[].append(json_info)
                        with open("data.json", 'w') as fp: 
                            json.dump(data, fp)
                        with open("data.json", 'w+') as fp:
                            json.dump(json_info, fp)
                        """
                        pass
        print(json_info["alumnos"])

        if cv2.waitKey(1) == 27: 
            break  # esc to quit

if __name__ == "__main__":
    recognize(sys.argv[1])