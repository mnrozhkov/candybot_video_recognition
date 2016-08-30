'''This module lets you get capture and save it on disk
    every 6 second
'''

import cv2
import time

cap = cv2.VideoCapture(0)
count = 0
currentTime = time.time()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if (time.time() - currentTime) >= 6:
        cv2.imwrite("images\\" + str(count)+".png", frame)
        count+=1
        currentTime = time.time()
    key = cv2.waitKey(1)
    if  key == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
