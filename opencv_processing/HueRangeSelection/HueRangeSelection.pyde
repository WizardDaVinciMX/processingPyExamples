add_library("opencv_processing")

lowerb = 50
upperb = 100

def setup():
  global img
  global opencv
  global histogram

  img = loadImage("colored_balls.jpg")
  opencv = OpenCV(this, img)
  size(1024, 768)
  opencv.useColor(HSB)


def draw():
  opencv.loadImage(img)
  
  image(img, 0, 0)  
  
  opencv.setGray(opencv.getH().clone())
  opencv.inRange(lowerb, upperb)
  histogram = opencv.findHistogram(opencv.getH(), 255)

  image(opencv.getOutput(), 3*width/4, 3*height/4, width/4,height/4)

  noStroke()
  fill(0)
  histogram.draw(10, height - 230, 400, 200)
  noFill()
  stroke(0)
  line(10, height-30, 410, height-30)

  text("Hue", 10, height - (textAscent() + textDescent()))

  lb = map(lowerb, 0, 255, 0, 400)
  ub = map(upperb, 0, 255, 0, 400)

  stroke(255, 0, 0)
  fill(255, 0, 0)
  strokeWeight(2)
  line(lb + 10, height-30, ub +10, height-30)
  ellipse(lb+10, height-30, 3, 3 )
  text(lowerb, lb-10, height-15)
  ellipse(ub+10, height-30, 3, 3 )
  text(upperb, ub+10, height-15)


def mouseMoved():
  global upperb, lowerb

  if keyPressed:
    upperb += mouseX - pmouseX
  else:
    if upperb < 255 or (mouseX - pmouseX) < 0:
      lowerb += mouseX - pmouseX

    if lowerb > 0 or (mouseX - pmouseX) > 0:
      upperb += mouseX - pmouseX

  upperb = constrain(upperb, lowerb, 255)
  lowerb = constrain(lowerb, 0, upperb-1)
