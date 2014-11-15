import cv2
import csv
import sys
import os
noOfFaces = []
#opening the csv file with three column numbers
with open('test.csv','w') as filepointer:
	a = csv.writer(filepointer, delimiter=',')
    #here are the column numbers
	data = [['SerialNo', 'ImageName', 'NoOffaces']]
	a.writerows(data)
# supply directory 'path' below so that we can loop through all images which u have downloaded in the folder
	for root, dirs, files in os.walk('path/'):
		i = 1
		for file in files:	
			imagePath = 'path/'+file
			if(imagePath.find('.DS_Store') >= 0) :
				continue
			cascPath = sys.argv[1]
			#print file
			# Create the haar cascade
			faceCascade = cv2.CascadeClassifier(cascPath)

			# Read the image
			image = cv2.imread(imagePath)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
			    gray,
			    scaleFactor=1.14,
			    minNeighbors=5,
			    minSize=(30, 30),
			    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
			)

			print file+" Found {0} faces!".format(len(faces))
            #each row has three columns which is serial number, file name, and number of faces in each file
			data = [[i ,file, len(faces)]]
			a.writerows(data)
			i = i+1
			
			noOfFaces.append(len(faces))
			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
			    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)	
            #Try different things
			#if(i>=10):
			#	break
			#cv2.imshow("Faces found", image)
			#cv2.waitKey(0)
print noOfFaces
