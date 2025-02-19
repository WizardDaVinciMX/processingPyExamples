add_library("gab.opencv.*
add_library("org.opencv.imgproc.Imgproc
add_library("org.opencv.core.Core

add_library("org.opencv.core.Mat
add_library("org.opencv.core.MatOfPoint
add_library("org.opencv.core.MatOfPoint2f
add_library("org.opencv.core.MatOfPoint2f
add_library("org.opencv.core.CvType

add_library("org.opencv.core.Point
add_library("org.opencv.core.Size

#add_library("java.util.list

OpenCV opencv
PImage  src, dst, markerImg
ArrayList<MatOfPoint> contours
ArrayList<MatOfPoint2f> approximations
ArrayList<MatOfPoint2f> markers

boolean[][] markerCells

def setup():
  opencv = OpenCV(this, "marker_test.jpg")
  size(1000, 365)
  src = opencv.getInput()

  # hold on to this for later, since adaptiveThreshold is destructive
  Mat gray = OpenCV.imitate(opencv.getGray())
  opencv.getGray().copyTo(gray)

  Mat thresholdMat = OpenCV.imitate(opencv.getGray())

  opencv.blur(5)
  
  Imgproc.adaptiveThreshold(opencv.getGray(), thresholdMat, 255, Imgproc.ADAPTIVE_THRESH_GAUSSIAN_C, Imgproc.THRESH_BINARY_INV, 451, -65)

  contours = ArrayList<MatOfPoint>()
  Imgproc.findContours(thresholdMat, contours, Mat(), Imgproc.RETR_LIST, Imgproc.CHAIN_APPROX_NONE)

  approximations = createPolygonApproximations(contours)

  markers = ArrayList<MatOfPoint2f>()
  markers = selectMarkers(approximations)

  ## Mat markerMat = grat.submat()
  #  Mat warped = OpenCVPro.imitate(gray)
  #  
  MatOfPoint2f canonicalMarker = MatOfPoint2f()
  Point[] canonicalPoints = Point[4]
  canonicalPoints[0] = Point(0, 350)
  canonicalPoints[1] = Point(0, 0)
  canonicalPoints[2] = Point(350, 0)
  canonicalPoints[3] = Point(350, 350)
  canonicalMarker.fromArray(canonicalPoints)

  println("num points: " + markers.get(0).height())

  Mat transform = Imgproc.getPerspectiveTransform(markers.get(0), canonicalMarker)
  Mat unWarpedMarker = Mat(50, 50, CvType.CV_8UC1)  
  Imgproc.warpPerspective(gray, unWarpedMarker, transform, Size(350, 350))


  Imgproc.threshold(unWarpedMarker, unWarpedMarker, 125, 255, Imgproc.THRESH_BINARY | Imgproc.THRESH_OTSU)

  cellSize = 350/7.0

  markerCells = boolean[7][7]

  for (row = 0 row < 7 row+=1):
    for (col = 0 col < 7 col+=1):
      cellX = int(col*cellSize)
      cellY = int(row*cellSize)

      Mat cell = unWarpedMarker.submat(cellX, cellX +(int)cellSize, cellY, cellY+ (int)cellSize) 
      markerCells[row][col] = (Core.countNonZero(cell) > (cellSize*cellSize)/2)
    
  

  for (col = 0 col < 7 col+=1):
    for (row = 0 row < 7 row+=1):
      if (markerCells[row][col]):
        print(1)
       
      else:
        print(0)
      
    
    println()
  

  dst  = createImage(350, 350, RGB)
  opencv.toPImage(unWarpedMarker, dst)




ArrayList<MatOfPoint2f> selectMarkers(ArrayList<MatOfPoint2f> candidates):
  minAllowedContourSide = 50
  minAllowedContourSide = minAllowedContourSide * minAllowedContourSide

  ArrayList<MatOfPoint2f> result = ArrayList<MatOfPoint2f>()

  for (MatOfPoint2f candidate : candidates):

    if (candidate.size().height != 4):
      continue
     

    if (!Imgproc.isContourConvex(MatOfPoint(candidate.toArray()))):
      continue
    

    # eliminate markers where consecutive
    # points are too close together
    minDist = src.width * src.width
    Point[] points = candidate.toArray()
    for (i = 0 i < points.length i+=1):
      Poside = Point(points[i].x - points[(i+1)%4].x, points[i].y - points[(i+1)%4].y)
      squaredLength = (float)side.dot(side)
      # println("minDist: " + minDist  + " squaredLength: " +squaredLength)
      minDist = min(minDist, squaredLength)
    

    #  println(minDist)


    if (minDist < minAllowedContourSide):
      continue
    

    result.add(candidate)
  

  return result


ArrayList<MatOfPoint2f> createPolygonApproximations(ArrayList<MatOfPoint> cntrs):
  ArrayList<MatOfPoint2f> result = ArrayList<MatOfPoint2f>()

  double epsilon = cntrs.get(0).size().height * 0.01
  println(epsilon)

  for (MatOfPocontour : cntrs):
    MatOfPoint2f approx = MatOfPoint2f()
    Imgproc.approxPolyDP(MatOfPoint2f(contour.toArray()), approx, epsilon, true)
    result.add(approx)
  

  return result


def drawContours(ArrayList<MatOfPoint> cntrs):
  for (MatOfPocontour : cntrs):
    beginShape()
    Point[] points = contour.toArray()
    for (i = 0 i < points.length i+=1):
      vertex((float)points[i].x, (float)points[i].y)
    
    endShape()
  


def drawContours2f(ArrayList<MatOfPoint2f> cntrs):
  for (MatOfPoint2f contour : cntrs):
    beginShape()
    Point[] points = contour.toArray()

    for (i = 0 i < points.length i+=1):
      vertex((float)points[i].x, (float)points[i].y)
    
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
  for (col = 0 col < 7 col+=1):
    for (row = 0 row < 7 row+=1):
      if(markerCells[row][col]){
        fill(255)
       else:
        fill(0)
      
      stroke(0,255,0)
      rect(col*cellSize, row*cellSize, cellSize, cellSize)
      #line(i*cellSize, 0, i*cellSize, dst.width)
    #line(0, i*cellSize, dst.width, i*cellSize)
    
  

  popMatrix()
