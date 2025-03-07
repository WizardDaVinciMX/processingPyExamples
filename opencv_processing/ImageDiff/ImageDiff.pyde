add_library("opencv_processing")

def setup():
  global opencv
  global before, after, grayDiff
# colorDiff

  before = loadImage("before.jpg")
  after = loadImage("after.jpg")
  size(640, 480)

  opencv = OpenCV(this, before)    
  opencv.diff(after)
  grayDiff = opencv.getSnapshot() 

#  opencv.useColor()
#  opencv.loadImage(after)
#  opencv.diff(after)
#  colorDiff = opencv.getSnapshot()

def draw():
  pushMatrix()
  scale(0.5)
  image(before, 0, 0)
  image(after, before.width, 0)
#  image(colorDiff, 0, before.height)
  image(grayDiff, before.width, before.height)
  popMatrix()

  fill(255)
  text("before", 10, 20)
  text("after", before.width/2 +10, 20)
  text("gray diff", before.width/2 + 10, before.height/2+ 20)

#  text("color diff", 10, before.height/2+ 20)
