add_library("opencv_processing")


def setup():
  global src, dst
  global opencv

  global contours
  global polygons

  src = loadImage("test.jpg") 
  size(1080, 360)
  opencv = OpenCV(this, src)

  opencv.gray()
  opencv.threshold(70)
  dst = opencv.getOutput()

  contours = opencv.findContours()
  println("found " + str(contours.size()) + " contours")


def draw():
  scale(0.5)
  image(src, 0, 0)
  image(dst, src.width, 0)

  noFill()
  strokeWeight(3)
  
  for contour in contours:
    stroke(0, 255, 0)
    contour.draw()
    
    stroke(255, 0, 0)
    beginShape()
    for point in contour.getPolygonApproximation().getPoints():
      vertex(point.x, point.y)
    
    endShape()
