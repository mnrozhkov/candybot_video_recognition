import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2

import convert
from simple_tracker import SimpleTracker


if __name__ == '__main__':
	cap = cv2.VideoCapture(0)
	st = SimpleTracker(face_cascade_file='haarcascade_frontalface_default.xml')
	count = 0
	while True:
		input('capture!>')
		ret, frame = cap.read()
		if ret:
			faces = st.find_faces(frame)
			print(len(faces))
			if len(faces) > 0:
				faces.sort()
				faces[0].printface()
			
			bimg = convert.ndarray2format(raw_img=frame, format='jpeg')
			with open(str(count) + '.jpeg', 'wb') as file:
				file.write(bimg)
			
			string = convert.ndarray2str(frame)
			print(len(string))
			image = convert.str2ndarray(string)
			cv2.imwrite(str(count) + '.png', image)
			count += 1
