add_library("opencv_processing")


def setup():
  global opencv
  global src, canny, scharr, sobel

  src = loadImage("test.jpg")
  size(1080, 720)
  
  opencv = OpenCV(this, src)
  opencv.findCannyEdges(20,75)
  canny = opencv.getSnapshot()
  
  opencv.loadImage(src)
  opencv.findScharrEdges(OpenCV.HORIZONTAL)
  scharr = opencv.getSnapshot()
  
  opencv.loadImage(src)
  opencv.findSobelEdges(1,0)
  sobel = opencv.getSnapshot()



def draw():
  pushMatrix()
  scale(0.5)
  image(src, 0, 0)
  image(canny, src.width, 0)
  image(scharr, 0, src.height)
  image(sobel, src.width, src.height)
  popMatrix()

  text("Source", 10, 25) 
  text("Canny", src.width/2 + 10, 25) 
  text("Scharr", 10, src.height/2 + 25) 
  text("Sobel", src.width/2 + 10, src.height/2 + 25)
