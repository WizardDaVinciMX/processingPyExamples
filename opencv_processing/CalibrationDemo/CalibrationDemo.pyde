add_library("opencv_processing")


def setup():
  global src
  global cornerPoints
  global opencv
  src = loadImage("checkerboard.jpg")
  src.resize(500, 0)
  size(500, 333)

  opencv = OpenCV(this, src)
  opencv.gray()
  
  cornerPoints = opencv.findChessboardCorners(9,6)


def draw():
  image( opencv.getOutput(), 0, 0)
  fill(255,0,0)
  noStroke()
  for p in cornerPoints:
    ellipse(p.x, p.y, 5, 5)
  
