add_library("opencv_processing")


def setup():
  global img
  global opencv

  img = loadImage("test.jpg")
  size(1080, 720)
  opencv = OpenCV(this, img)  


def draw():
  opencv.loadImage(img)
  opencv.brightness(int(map(mouseX, 0, width, -255, 255)))
  image(opencv.getOutput(),0,0)
