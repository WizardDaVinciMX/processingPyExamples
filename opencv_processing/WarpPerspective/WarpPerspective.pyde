add_library("opencv_processing")

from org.opencv.imgproc import Imgproc
from org.opencv.core import MatOfPoint2f
from org.opencv.core import Point
from org.opencv.core import Size

from org.opencv.core import Mat
from org.opencv.core import CvType

cardWidth = 250
cardHeight = 350

def setup():
  global opencv
  global src
  global card
  global contour

  src = loadImage("cards.png")
  size(950, 749)
  opencv = OpenCV(this, src)

  opencv.blur(1)
  opencv.threshold(120)

  contour = opencv.findContours(False, True)[0].getPolygonApproximation()

  card = createImage(cardWidth, cardHeight, ARGB)  
  opencv.toPImage(warpPerspective(contour.getPoints(), cardWidth, cardHeight), card)


def getPerspectiveTransformation(inputPoints, w, h):
  global canonicalPoints

  canonicalPoints = [Point()] * 4
  canonicalPoints[0] = Point(w, 0)
  canonicalPoints[1] = Point(0, 0)
  canonicalPoints[2] = Point(0, h)
  canonicalPoints[3] = Point(w, h)

  canonicalMarker = MatOfPoint2f()
  canonicalMarker.fromArray(canonicalPoints)

  points = list() #[Point()] * 4
  for p in inputPoints:
    points.append(Point(p.x, p.y))
  
  marker = MatOfPoint2f(points)
  return Imgproc.getPerspectiveTransform(marker, canonicalMarker)


def warpPerspective(inputPoints, w, h):
  transform = getPerspectiveTransformation(inputPoints, w, h)
  unWarpedMarker = Mat(w, h, CvType.CV_8UC1)    
  Imgproc.warpPerspective(opencv.getColor(), unWarpedMarker, transform, Size(w, h))
  return unWarpedMarker

def draw():
  image(src, 0, 0)
  noFill() 
  stroke(0, 255, 0) 
  strokeWeight(4)
  contour.draw()
  fill(255, 0)
  points = contour.getPoints()
  for i in range(0, len(points)):
    text(i, points[i].x, points[i].y)

  pushMatrix()
  translate(src.width, 0)
  image(card, 0, 0)
  popMatrix()
