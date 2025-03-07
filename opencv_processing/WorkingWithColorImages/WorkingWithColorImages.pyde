add_library("opencv_processing")


def setup():
  global opencv
  global threshold, blur, adaptive, gray

  img = loadImage("test.jpg")
  size(1080, 720)

  # By default, OpenCV for Processing works with a gray
  # version of the source image
  opencv = OpenCV(this, img)
  # but you can tell it explicitly to use color instead:
  opencv.useColor()  

  # A lot of OpenCV operations only work on grayscale images.
  # But some do work in color, like threshold, blur, findCannyEdges, findChessboardCorners, etc.:
  opencv.threshold(75)
  threshold = opencv.getSnapshot()

  opencv.blur(30)
  blur = opencv.getSnapshot()

  # If you try an operation that does not work in color
  # it will prout an error message and leave the image unaffected
  opencv.adaptiveThreshold(591, 1)
  adaptive = opencv.getSnapshot()
  
  # if you convert the image to gray then you can
  # do gray-only operations
  opencv.gray()
  opencv.adaptiveThreshold(591, 1)
  gray = opencv.getSnapshot()


def draw():
  global threshold

  scale(0.5)
  image(threshold, 0, 0)
  image(blur, threshold.width,0)
  image(adaptive, 0,threshold.height)
  image(gray, threshold.width, threshold.height)
