"""
 * Image Filtering
 * This sketch performs some image filtering (threshold, blur) and contour detection
 *
 * @author: Jordi Tost (@jorditost)
 * @url: https:#github.com/jorditost/ImageFiltering/tree/master/ImageFiltering
 *
 * University of Applied Sciences Potsdam, 2014
 *
 * It requires the ControlP5 Processing library:
 * http:#www.sojamo.de/libraries/controlP5/
"""

add_library("opencv_processing")
add_library("video")
add_library("controlP5")

from java.awt import Rectangle

contrast = 1.35
brightness = 0
threshold = 75
useAdaptiveThreshold = False # use basic thresholding
thresholdBlockSize = 489
thresholdConstant = 45
blobSizeThreshold = 20
blurSize = 4

def setup():
  global opencv
  global video
  global src, preProcessedImage, processedImage, contoursImage

  # Control vars
  global cp5
  global buttonColor
  global buttonBgColor

  frameRate(15)

  video = Capture(this, "pipeline:autovideosrc")
  video.start()

  opencv = OpenCV(this, 640, 480)
  contours = ArrayList<Contour>()

  size(840, 480, P2D)

  # Init Controls
  cp5 = ControlP5(this)
  initControls()

  # Set thresholding
  toggleAdaptiveThreshold(useAdaptiveThreshold)


def draw():
  # Read last captured frame
  if (video.available()):
    video.read()

  # Load the frame of our camera in to OpenCV
  opencv.loadImage(video)
  src = opencv.getSnapshot()

  ###############/
  # <1> PRE-PROCESS IMAGE
  # - Grey channel
  # - Brightness / Contrast
  ###############/

  # Gray channel
  opencv.gray()

  #opencv.brightness(brightness)
  opencv.contrast(contrast)

  # Save snapshot for display
  preProcessedImage = opencv.getSnapshot()

  ###############/
  # <2> PROCESS IMAGE
  # - Threshold
  # - Noise Supression
  ###############/

  # Adaptive threshold - Good when non-uniform illumination
  if useAdaptiveThreshold:
    # Block size must be odd and greater than 3
    if thresholdBlockSize % 2 == 0:
       thresholdBlockSize += 1
    if thresholdBlockSize < 3:
       thresholdBlockSize = 3
       opencv.adaptiveThreshold(thresholdBlockSize, thresholdConstant)
    # Basic threshold - range [0, 255]
    else:
       opencv.threshold(threshold)

  # Invert (black bg, white blobs)
  opencv.invert()

  # Reduce noise - Dilate and erode to close holes
  opencv.dilate()
  opencv.erode()

  # Blur
  opencv.blur(blurSize)

  # Save snapshot for display
  processedImage = opencv.getSnapshot()

  ###############/
  # <3> FIND CONTOURS
  ###############/

  # Passing 'true' sorts them by descending area.
  contours = opencv.findContours(true, true)

  # Save snapshot for display
  contoursImage = opencv.getSnapshot()

  # Draw
  pushMatrix()

  # Leave space for ControlP5 sliders
  translate(width-src.width, 0)

  # Display images
  displayImages()

  # Display contours in the lower right window
  pushMatrix()
  scale(0.5)
  translate(src.width, src.height)

  displayContours()
  displayContoursBoundingBoxes()

  popMatrix()

  popMatrix()


##########/
# Display Methods
##########/

def displayImages():
  pushMatrix()
  scale(0.5)
  image(src, 0, 0)
  image(preProcessedImage, src.width, 0)
  image(processedImage, 0, src.height)
  image(src, src.width, src.height)
  popMatrix()

  stroke(255)
  fill(255)
  text("Source", 10, 25)
  text("Pre-processed Image", src.width/2 + 10, 25)
  text("Processed Image", 10, src.height/2 + 25)
  text("Tracked Points", src.width/2 + 10, src.height/2 + 25)


def displayContours():
  for i in range(0, contours.size()):
    contour = contours.get(i)
    noFill()
    stroke(0, 255, 0)
    strokeWeight(3)
    contour.draw()

def displayContoursBoundingBoxes():
  for i in range(0, contours.size()):
    contour = contours.get(i)
    r = contour.getBoundingBox()

#    if #(contour.area() > 0.9 * src.width * src.height) ||
    if (r.width < blobSizeThreshold or r.height < blobSizeThreshold):
      continue

    stroke(255, 0, 0)
    fill(255, 0, 0, 150)
    strokeWeight(2)
    rect(r.x, r.y, r.width, r.height)

#############
# CONTROL P5 Functions
#############
def initControls():
  # Slider for contrast
  cp5.addSlider("contrast")
  cp5.setLabel("contrast")
  cp5.setPosition(20, 50)
  cp5.setRange(0.0, 6.0)

  # Slider for threshold
  cp5.addSlider("threshold")
  cp5.setLabel("threshold")
  cp5.setPosition(20, 110)
  cp5.setRange(0, 255)

  # Toggle to activae adaptive threshold
  cp5.addToggle("toggleAdaptiveThreshold")
  cp5.setLabel("use adaptive threshold")
  cp5.setSize(10, 10)
  cp5.setPosition(20, 144)

  # Slider for adaptive threshold block size
  cp5.addSlider("thresholdBlockSize")
  cp5.setLabel("a.t. block size")
  cp5.setPosition(20, 180)
  cp5.setRange(1, 700)

  # Slider for adaptive threshold constant
  cp5.addSlider("thresholdConstant")
  cp5.setLabel("a.t. constant")
  cp5.setPosition(20, 200)
  cp5.setRange(-100, 100)

  # Slider for blur size
  cp5.addSlider("blurSize")
  cp5.setLabel("blur size")
  cp5.setPosition(20, 260)
  cp5.setRange(1, 20)

  # Slider for minimum blob size
  cp5.addSlider("blobSizeThreshold")
  cp5.setLabel("min blob size")
  cp5.setPosition(20, 290)
  cp5.setRange(0, 60)

  # Store the default background color, we gonna need it later
  buttonColor = cp5.getController("contrast").getColor().getForeground()
  buttonBgColor = cp5.getController("contrast").getColor().getBackground()

def toggleAdaptiveThreshold(theFlag):
  useAdaptiveThreshold = theFlag

  if useAdaptiveThreshold:
    # Lock basic threshold
    setLock(cp5.getController("threshold"), True)

    # Unlock adaptive threshold
    setLock(cp5.getController("thresholdBlockSize"), False)
    setLock(cp5.getController("thresholdConstant"), False)
  else:
    # Unlock basic threshold
    setLock(cp5.getController("threshold"), False)

    # Lock adaptive threshold
    setLock(cp5.getController("thresholdBlockSize"), True)
    setLock(cp5.getController("thresholdConstant"), True)


def setLock(theController, theValue):
  theController.setLock(theValue)

  if theValue:
    theController.setColorBackground(color(150, 150))
    theController.setColorForeground(color(100, 100))
  else:
    theController.setColorBackground(color(buttonBgColor))
    theController.setColorForeground(color(buttonColor))
