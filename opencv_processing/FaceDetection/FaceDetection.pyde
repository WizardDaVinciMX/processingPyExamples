add_library("opencv_processing")
from java.awt import Rectangle


def setup():
  global opencv
  global faces

  opencv = OpenCV(this, "test.jpg")
  size(1080, 720)

  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)  
  faces = opencv.detect()


def draw():
  image(opencv.getInput(), 0, 0)

  noFill()
  stroke(0, 255, 0)
  strokeWeight(3)
  for i in range(0, len(faces)):
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height)
  
