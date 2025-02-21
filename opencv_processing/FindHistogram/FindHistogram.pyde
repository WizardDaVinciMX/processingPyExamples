add_library("opencv_processing")


def setup():
  global opencv
  global grayHist, rHist, gHist, bHist

  global img

  size(640, 400)
  img = loadImage("test.jpg")
  opencv = OpenCV(this, img)

  grayHist = opencv.findHistogram(opencv.getGray(), 256)
  rHist = opencv.findHistogram(opencv.getR(), 256)
  gHist = opencv.findHistogram(opencv.getG(), 256)
  bHist = opencv.findHistogram(opencv.getB(), 256)


def draw():
  background(0)
  image(img, 10, 0, 300, 200)

  stroke(125)
  noFill()  
  rect(320, 10, 310, 180)
  
  fill(125)
  noStroke()
  grayHist.draw(320, 10, 310, 180)

  stroke(255, 0, 0)
  noFill()  
  rect(10, height - 190, 200, 180)
  
  fill(255, 0, 0)
  noStroke()
  rHist.draw(10, height - 190, 200, 180)

  stroke(0, 255, 0)
  noFill()  
  rect(220, height - 190, 200, 180)
  
  fill(0, 255, 0)
  noStroke()
  gHist.draw(220, height - 190, 200, 180)

  stroke(0, 0, 255)
  noFill()  
  rect(430, height - 190, 200, 180)
  
  fill(0, 0, 255)
  noStroke()
  bHist.draw(430, height - 190, 200, 180)
