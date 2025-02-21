add_library("opencv_processing")
from org.opencv.imgproc import Imgproc
from org.opencv.core import Core

from org.opencv.core import Mat
from org.opencv.core import MatOfPoint
from org.opencv.core import MatOfPoint2f
from org.opencv.core import MatOfPoint2f
from org.opencv.core import CvType

from org.opencv.core import Point
from org.opencv.core import Size

#add_library("java.util.list


def setup():
  global opencv
  global src, dst, markerImg
  global contours
  global approximations
  global markers

  global markerCells

  opencv = OpenCV(this, "marker_test.jpg")
  size(1000, 365)
  src = opencv.getInput()

  # hold on to this for later, since adaptiveThreshold is destructive
  gray = OpenCV.imitate(opencv.getGray())
  opencv.getGray().copyTo(gray)

  thresholdMat = OpenCV.imitate(opencv.getGray())

  opencv.blur(5)
  
  Imgproc.adaptiveThreshold(opencv.getGray(), thresholdMat, 255, Imgproc.ADAPTIVE_THRESH_GAUSSIAN_C, Imgproc.THRESH_BINARY_INV, 451, -65)

  contours = list()
  Imgproc.findContours(thresholdMat, contours, Mat(), Imgproc.RETR_LIST, Imgproc.CHAIN_APPROX_NONE)

  approximations = createPolygonApproximations(contours)

  markers = list()
  markers = selectMarkers(approximations)

  ## Mat markerMat = grat.submat()
  #  Mat warped = OpenCVPro.imitate(gray)
  #  
  canonicalMarker = MatOfPoint2f()
  canonicalPoints = [Point()]*4
  canonicalPoints[0] = Point(0, 350)
  canonicalPoints[1] = Point(0, 0)
  canonicalPoints[2] = Point(350, 0)
  canonicalPoints[3] = Point(350, 350)
  canonicalMarker.fromArray(canonicalPoints)

  println("num points: " + str(markers[0].height()))

  transform = Imgproc.getPerspectiveTransform(markers[0], canonicalMarker)
  unWarpedMarker = Mat(50, 50, CvType.CV_8UC1)  
  Imgproc.warpPerspective(gray, unWarpedMarker, transform, Size(350, 350))


  Imgproc.threshold(unWarpedMarker, unWarpedMarker, 125, 255, Imgproc.THRESH_BINARY | Imgproc.THRESH_OTSU)

  cellSize = 350/7.0

  markerCells = [[False] * 7] * 7

  for row in range(0, 7):
    for col in range(0, 7):
      cellX = int(col*cellSize)
      cellY = int(row*cellSize)

      cell = unWarpedMarker.submat(cellX, cellX + int(cellSize), cellY, cellY + int(cellSize))
      markerCells[row][col] = (Core.countNonZero(cell) > (cellSize*cellSize)/2)

  for col in range(0, 7):
    for row  in range(0, 7):
      if markerCells[row][col]:
        print(1)       
      else:
        print(0)
    println("")

  dst  = createImage(350, 350, RGB)
  opencv.toPImage(unWarpedMarker, dst)

def selectMarkers(candidates):
  minAllowedContourSide = 50
  minAllowedContourSide = minAllowedContourSide * minAllowedContourSide

  result = list()

  for candidate in candidates:
    if candidate.size().height != 4:
      continue

    if not Imgproc.isContourConvex(MatOfPoint(candidate.toArray())):
      continue

    # eliminate markers where consecutive
    # points are too close together
    minDist = src.width * src.width
    points = candidate.toArray()
    for i in range(0, len(points)):
      side = Point(points[i].x - points[(i+1)%4].x, points[i].y - points[(i+1)%4].y)
      squaredLength = float(side.dot(side))
      # println("minDist: " + minDist  + " squaredLength: " +squaredLength)
      minDist = min(minDist, squaredLength)

    #  println(minDist)

    if minDist < minAllowedContourSide:
      continue

    result.append(candidate)

  return result


def createPolygonApproximations(cntrs):
  global contour

  result = list()

  epsilon = cntrs[0].size().height * 0.01
  println(epsilon)

  for contour in cntrs:
    approx = MatOfPoint2f()
    Imgproc.approxPolyDP(MatOfPoint2f(contour.toArray()), approx, epsilon, True)
    result.append(approx)

  return result

def drawContours(cntrs):
  for cntr in cntrs:
    beginShape()
    points = contour.toArray()
    for i in range(0, points.length):
      vertex(float(points[i].x), float(points[i].y))

    endShape()


def drawContours2f(cntrs):
  for contour in cntrs:
    beginShape()
    points = contour.toArray()

    for point in points:
      vertex(float(point.x), float(point.y))
    
    endShape(CLOSE)

def draw():
  pushMatrix()
  background(125)
  scale(0.5)
  image(src, 0, 0)

  noFill()
  smooth()
  strokeWeight(5)
  stroke(0, 255, 0)
  drawContours2f(markers)  
  popMatrix()

  pushMatrix()
  translate(src.width/2, 0)
  strokeWeight(1)
  image(dst, 0, 0)

  cellSize = dst.width/7.0
  for col in range(0, 7):
    for row in range(0, 7):
      if markerCells[row][col]:
        fill(255)
      else:
        fill(0)
      
      stroke(0,255,0)
      rect(col*cellSize, row*cellSize, cellSize, cellSize)
      #line(i*cellSize, 0, i*cellSize, dst.width)
    #line(0, i*cellSize, dst.width, i*cellSize)

  popMatrix()
