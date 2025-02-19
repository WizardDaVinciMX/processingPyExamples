add_library("opencv_processing")


def setup():
  global opencv
  global lines

  src = loadImage("film_scan.jpg")
  src.resize(0, 800)
  size(796, 800)

  opencv = OpenCV(this, src)
  opencv.findCannyEdges(20, 75)

  # Find lines with Hough line detection
  # Arguments are: threshold, minLengthLength, maxLineGap
  lines = opencv.findLines(100, 30, 20)


def draw():
  image(opencv.getOutput(), 0, 0)
  strokeWeight(3)
  
  for l in lines:
    # lines include angle in radians, measured in double precision
    # so we can select out vertical and horizontal lines
    # They also include "start" and "end" PVectors with the position
    if l.angle >= radians(0) and l.angle < radians(1):
      stroke(0, 255, 0)
      line(l.start.x, l.start.y, l.end.x, l.end.y)
    

    if l.angle > radians(89) and l.angle < radians(91):
      stroke(255, 0, 0)
      line(l.start.x, l.start.y, l.end.x, l.end.y)
