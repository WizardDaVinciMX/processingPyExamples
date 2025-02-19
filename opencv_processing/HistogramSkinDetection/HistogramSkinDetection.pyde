add_library("opencv_processing")

from org.opencv.core import Core
from org.opencv.core import Mat
from org.opencv.core import Size
from org.opencv.core import Point
from org.opencv.core import Scalar
from org.opencv.core import CvType
from org.opencv.imgproc import Imgproc


def setup():
  global opencv
  global src,dst, hist, histMask

  global skinHistogram

  src = loadImage("test.jpg")
  src.resize(src.width/2, 0)
  size(1336, 360)
  # third argument is: useColor
  opencv = OpenCV(this, src, True)  

  skinHistogram = Mat.zeros(256, 256, CvType.CV_8UC1)
  Imgproc.ellipse(skinHistogram, Point(113.0, 155.6), Size(40.0, 25.2), 43.0, 0.0, 360.0, Scalar(255, 255, 255), Core.FILLED)

  histMask = createImage(256,256, ARGB)
  opencv.toPImage(skinHistogram, histMask)
  hist = loadImage("cb-cr.png")
  hist.blend(histMask, 0,0,256,256,0,0,256,256, ADD)
 
  dst = opencv.getOutput()
  dst.loadPixels()
 
  for i in range(0, len(dst.pixels)):
    
    input = Mat(Size(1, 1), CvType.CV_8UC3)
    input.setTo(colorToScalar(dst.pixels[i]))
    output = opencv.imitate(input)
    Imgproc.cvtColor(input, output, Imgproc.COLOR_BGR2YCrCb )
    inputComponents = output.get(0,0)
    if skinHistogram.get(int(inputComponents[1]), int(inputComponents[2]))[0] > 0:
      dst.pixels[i] = color(255)
    else:
      dst.pixels[i] = color(0)

  dst.updatePixels()

# in BGR
def colorToScalar(c):
  return Scalar(blue(c), green(c), red(c))

def draw():
  image(src,0,0)
  image(dst, src.width, 0)
  image(hist, src.width*2, 0)
