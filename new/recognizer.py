import cv2
import face_recognition
import pickle
import os

def recognize(pickle_file):
    print("Initializing...")

    encodings = pickle.load(open(f"trains/{pickle_file}", 'rb'))
    people = {person.split('.')[0]: False for person in os.listdir('videos/')}
    cam = cv2.VideoCapture(0)

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
                if not people[name]:
                    matches = []
                    for e in encoding:
                        matches.append(face_recognition.compare_faces(e, person))
                    if matches.count([True]) >= 21 and name in list(people.keys()):
                        people[name] = True
                
        print(people)
        #this_frame = not this_frame

        if cv2.waitKey(1) == 27: 
            break  # esc to quit
