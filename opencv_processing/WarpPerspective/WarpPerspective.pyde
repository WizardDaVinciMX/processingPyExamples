add_library("gab.opencv.*
add_library("org.opencv.imgproc.Imgproc
add_library("org.opencv.core.MatOfPoint2f
add_library("org.opencv.core.Point
add_library("org.opencv.core.Size

add_library("org.opencv.core.Mat
add_library("org.opencv.core.CvType


OpenCV opencv
PImage src
PImage card
cardWidth = 250
cardHeight = 350

Contour contour

def setup():
  src = loadImage("cards.png")
  size(950, 749)
  opencv = OpenCV(this, src)

  opencv.blur(1)
  opencv.threshold(120)

  contour = opencv.findContours(false, true).get(0).getPolygonApproximation()

  card = createImage(cardWidth, cardHeight, ARGB)  
  opencv.toPImage(warpPerspective(contour.getPoints(), cardWidth, cardHeight), card)


Mat getPerspectiveTransformation(ArrayList<PVector> inputPoints, w, h):
  Point[] canonicalPoints = Point[4]
  canonicalPoints[0] = Point(w, 0)
  canonicalPoints[1] = Point(0, 0)
  canonicalPoints[2] = Point(0, h)
  canonicalPoints[3] = Point(w, h)

  MatOfPoint2f canonicalMarker = MatOfPoint2f()
  canonicalMarker.fromArray(canonicalPoints)

  Point[] points = Point[4]
  for (i = 0 i < 4 i+=1):
    points[i] = Point(inputPoints.get(i).x, inputPoints.get(i).y)
  
  MatOfPoint2f marker = MatOfPoint2f(points)
  return Imgproc.getPerspectiveTransform(marker, canonicalMarker)


Mat warpPerspective(ArrayList<PVector> inputPoints, w, h):
  Mat transform = getPerspectiveTransformation(inputPoints, w, h)
  Mat unWarpedMarker = Mat(w, h, CvType.CV_8UC1)    
  Imgproc.warpPerspective(opencv.getColor(), unWarpedMarker, transform, Size(w, h))
  return unWarpedMarker



def draw():
  image(src, 0, 0)
  noFill() 
  stroke(0, 255, 0) 
  strokeWeight(4)
  contour.draw()
  fill(255, 0)
  ArrayList<PVector> points = contour.getPoints()
  for (i = 0 i < points.size() i+=1):
    text(i, points.get(i).x, points.get(i).y)
  

  pushMatrix()
  translate(src.width, 0)
  image(card, 0, 0)
  popMatrix()
