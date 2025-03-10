add_library("opencv_processing")


def setup():
  global opencv
  global img, thresh, blur, adaptive

  img = loadImage("test.jpg")
  size(1080, 720)

  opencv = OpenCV(this, img)  
  gray = opencv.getSnapshot()
 
  opencv.threshold(80)
  thresh = opencv.getSnapshot()
  
  opencv.loadImage(gray)
  opencv.blur(12)  
  blur = opencv.getSnapshot()
  
  opencv.loadImage(gray)
  opencv.adaptiveThreshold(591, 1)
  adaptive = opencv.getSnapshot()


def draw():
  pushMatrix()
  scale(0.5)
  image(img, 0, 0)
  image(thresh, img.width, 0)
  image(blur, 0, img.height)
  image(adaptive, img.width, img.height)
  popMatrix()

  fill(0)
  text("source", img.width/2 - 100, 20 )
  text("threshold", img.width - 100, 20 )
  text("blur", img.width/2 - 100, img.height/2 + 20 )
  text("adaptive threshold", img.width - 150, img.height/2 + 20 )
