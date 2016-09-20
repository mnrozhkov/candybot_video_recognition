from vision.recognition import VisionRecognition

#create recognizer
vr = VisionRecognition(image='face.jpg')
#recognize objects
try:
    vr.recognize_all()
except httplib2.ServerNotFoundError:
    print('Check Internet-connection')

#get faces list    
faces = vr.get_faces()
if len(faces) > 0:
    #take the first face
    face = faces[0]
    #print eyes coordinates
    print('Eyes coordinates\n')
    print('Left eye\n\t x:',face.landmarks['LEFT_EYE']['x'], '\n\t y:',
          face.landmarks['LEFT_EYE']['y'])
    print('Right eye\n\t x:',face.landmarks['RIGHT_EYE']['x'], '\n\t y:',
          face.landmarks['RIGHT_EYE']['y'])
