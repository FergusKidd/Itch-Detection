# import open cv
import cv2
# import azure face api
from azure.cognitiveservices.vision.face import FaceClient

# start a face client
face_client = FaceClient.open_from_key('<your subscription key>')

# open the webcam stream and loop image by image
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# function to detect faces using azure
def detect_faces(frame):
    # detect faces in the frame
    faces = face_client.face.detect_with_stream(frame)
    # loop through the faces and draw a rectangle around them
    for face in faces:
        face_rectangle = face.face_rectangle
        cv2.rectangle(frame, (face_rectangle.left, face_rectangle.top), (face_rectangle.left + face_rectangle.width, face_rectangle.top + face_rectangle.height), (0, 255, 0), 2)
    # return the frame
    return frame
