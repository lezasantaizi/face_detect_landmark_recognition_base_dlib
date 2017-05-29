# -*- coding: utf-8 -*-
import face_recognition
import cv2

import sys
import os
import dlib



if len(sys.argv) != 2:
    print(
        "Give the path to the trained shape predictor model as the first "
        "argument and then the directory containing the facial images.\n"
        "For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./face_landmark_detection.py shape_predictor_68_face_landmarks.dat ../examples/faces\n"
        "You can download a trained facial shape predictor from:\n"
        "    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
    exit()

predictor_path = sys.argv[1]
#faces_folder_path = sys.argv[2]


video_capture = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

flag = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video

        dets = detector(small_frame, 1)





    process_this_frame = not process_this_frame


    # Display the results
    for d in dets:

        left = d.left()
        top = d.top()
        right = d.right()
        bottom = d.bottom()
        shape = predictor(small_frame, d)
        for point_index in range(shape.num_parts):
            x,y = shape.part(point_index).x,shape.part(point_index).y
            cv2.circle(frame, (x*4, y*4), 1, (0, 255, 0), -1)
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)




    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()