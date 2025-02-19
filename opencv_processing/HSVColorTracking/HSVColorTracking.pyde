"""
 * HSVColorTracking
 * Greg Borenstein
 * https:#github.com/atduskgreg/opencv-processing-book/blob/master/code/hsv_color_tracking/HSVColorTracking/HSVColorTracking.pde
 *
 * Modified by Jordi Tost @jorditost (color selection)
 *
 * University of Applied Sciences Potsdam, 2014
"""
 
add_library("opencv_processing")
add_library("video")

from java.awt import Rectangle

# <1> Set the range of Hue values for our filter
rangeLow = 20
rangeHigh = 35

def setup():
  global video
  global opencv
  global src, colorFilteredImage
  global contours

  video = Capture(this, "pipeline:autovideosrc")
  video.start()
  
  opencv = OpenCV(this, video.width, video.height)
  contours = []

  size(1280, 480, P2D)


def draw():
  # Read last captured frame
  if (video.available()):
    video.read()

  # <2> Load the frame of our movie in to OpenCV
  opencv.loadImage(video)

  # Tell OpenCV to use color information
  opencv.useColor()
  src = opencv.getSnapshot()

  # <3> Tell OpenCV to work in HSV color space.
  opencv.useColor(HSB)

  # <4> Copy the Hue channel of our image into 
  #     the gray channel, which we process.
  opencv.setGray(opencv.getH().clone())

  # <5> Filter the image based on the range of 
  #     hue values that match the object we want to track.
  opencv.inRange(rangeLow, rangeHigh)

  # <6> Get the processed image for reference.
  colorFilteredImage = opencv.getSnapshot()

  #####################/
  # We could process our image here!
  # See ImageFiltering.pde
  #####################/

  # <7> Find contours in our range image.
  #     Passing 'true' sorts them by descending area.
  contours = opencv.findContours(True, True)

  # <8> Display background images
  image(video, 0, 0)
  image(colorFilteredImage, src.width, 0)

  # <9> Check to make sure we've found any contours
  if contours.size() > 0:
    # <9> Get the first contour, which will be the largest one
    biggestContour = contours.get(0)

    # <10> Find the bounding box of the largest contour,
    #      and hence our object.
    r = biggestContour.getBoundingBox()

    # <11> Draw the bounding box of our object
    noFill() 
    strokeWeight(2) 
    stroke(255, 0, 0)
    rect(r.x, r.y, r.width, r.height)

    # <12> Draw a dot in the middle of the bounding box, on the object.
    noStroke() 
    fill(255, 0, 0)
    ellipse(r.x + r.width/2, r.y + r.height/2, 30, 30)


def mousePressed():
  c = get(mouseX, mouseY)
  println("r: " + red(c) + " g: " + green(c) + " b: " + blue(c))

  hue = int(map(hue(c), 0, 255, 0, 180))
  println("hue to detect: " + hue)

  rangeLow = hue - 5
  rangeHigh = hue + 5
