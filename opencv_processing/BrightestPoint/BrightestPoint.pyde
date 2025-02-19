add_library("opencv_processing")


def setup():
  global opencv

  src = loadImage("robot_light.jpg")
  src.resize(800, 0)
  size(800, 533)
  
  opencv = OpenCV(this, src)  


def draw():
  image(opencv.getOutput(), 0, 0) 
  loc = opencv.max()
  
  stroke(255, 0, 0)
  strokeWeight(4)
  noFill()
  ellipse(loc.x, loc.y, 10, 10)
