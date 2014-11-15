FacesInSelfie
=============

In this project we have used Instagram API and programming languages like python, R (for visulization)

The purpose of this project is to Find a survey and visulize it using various graphs and plots.

The survey is to find number of faces in an selfie Image.

Mostly there is only one face but there are cases when people just tag "selfie" without even a face in it.

First Step:
=============

Download images using Instagram API tagged with "selfie"
See downloadimage.py file

Second Step:
=============

from command line:

python making_csv.py haarcascade_frontalface_default.xml

This will create a csv file which will look something like this:

Serial No.  File Name    Number of Faces

1              abc.png        2
2              pqr.png        1

and so on



