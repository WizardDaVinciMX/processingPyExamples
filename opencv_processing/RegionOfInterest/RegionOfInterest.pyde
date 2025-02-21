add_library("opencv_processing")

roiWidth = 150
roiHeight = 150

useROI = True

def setup():
  global src
  global opencv

  src = loadImage("test.jpg")
  opencv = OpenCV(this, src)
  size(1080, 720)
  println(str(opencv.width) + ' ' + str(opencv.height))


def draw():
  opencv.loadImage(src)

  if useROI:
    opencv.setROI(mouseX, mouseY, roiWidth, roiHeight)
  

  opencv.findCannyEdges(20,75)
  image(opencv.getOutput(), 0, 0)
  
  # if an ROI is in-use then getSnapshot()
  # will return an image with the dimensions
  # and content of the ROI
  if useROI:
    image(opencv.getSnapshot(), width-roiWidth,0)


# toggle ROI on and off
def keyPressed():
  global userROI

  useROI = not useROI

  if not useROI:
    opencv.releaseROI()
