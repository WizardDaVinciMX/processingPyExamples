"""
 * Image Filtering
 * This sketch will help us to adjust the filter values to optimize blob detection
 * 
 * Persistence algorithm by Daniel Shifmann:
 * http:#shiffman.net/2011/04/26/opencv-matching-faces-over-time/
 *
 * @author: Jordi Tost (@jorditost)
 * @url: https:#github.com/jorditost/ImageFiltering/tree/master/ImageFilteringWithBlobPersistence
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

# Number of blobs detected over all time. Used to set IDs.
blobCount = 0

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
  global contours
  # List of detected contours parsed as blobs (every frame)
  global newBlobContours
  # List of my blob objects (persistent)
  global blobList
  # Control vars
  global cp5
  global buttonColor
  global buttonBgColor

  frameRate(15)
  
  video = Capture(this, "pipeline:autovideosrc")
  #video = Capture(this, 640, 480, "USB2.0 PC CAMERA")
  video.start()
  
  opencv = OpenCV(this, 640, 480)
  contours = ArrayList<Contour>()
  
  # Blobs list
  blobList = ArrayList<Blob>()
  
  size(840, 480, P2D)
  
  # Init Controls
  cp5 = ControlP5(this)
  initControls()
  
  # Set thresholding
  toggleAdaptiveThreshold(useAdaptiveThreshold)


def draw():
  # Read last captured frame
  if video.available():
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
    if thresholdBlockSize%2 == 0:
        thresholdBlockSize+=1
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
def detectBlobs():
  # Passing 'true' sorts them by descending area.
  #contours = opencv.findContours(true, true)

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

  # Contours
  #displayContours()
  #displayContoursBoundingBoxes()

  # Blobs
  displayBlobs()

  popMatrix() 

  popMatrix()


###########/
# Display Functions
###########/
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
  textSize(12)
  text("Source", 10, 25) 
  text("Pre-processed Image", src.width/2 + 10, 25) 
  text("Processed Image", 10, src.height/2 + 25) 
  text("Tracked Points", src.width/2 + 10, src.height/2 + 25)

def displayBlobs():  
  for b in blobList:
    strokeWeight(1)
    b.display()


def displayContours():  
  # Contours
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

#    if (#(contour.area() > 0.9 * src.width * src.height) ||
    if (r.width < blobSizeThreshold or r.height < blobSizeThreshold):
      continue

    stroke(255, 0, 0)
    fill(255, 0, 0, 150)
    strokeWeight(2)
    rect(r.x, r.y, r.width, r.height)

##########
# Blob Detection
##########
def detectBlobs():
  # Contours detected in this frame
  # Passing 'true' sorts them by descending area.
  contours = opencv.findContours(true, true)

  newBlobContours = getBlobsFromContours(contours)

  #println(contours.length)

  # Check if the detected blobs already exist are or some has disappeared. 

  # SCENARIO 1 
  # blobList is empty
  if blobList.isEmpty():
    # Just make a Blob object for every face Rectangle
    for i in range(0, newBlobContours.size()):
      println("+=1+ New blob detected with ID: " + blobCount)
      blobList.add(Blob(this, blobCount, newBlobContours.get(i)))
      blobCount += 1

  # SCENARIO 2 
  # We have fewer Blob objects than face Rectangles found from OpenCV in this frame
  elif blobList.size() <= newBlobContours.size():
    used = boolean(newBlobContours.size())
    # Match existing Blob objects with a Rectangle
    for b in blobList:
       # Find the blob newBlobContours.get(index) that is closest to blob b
       # set used[index] to true so that it can't be used twice
       record = 50000
       index = -1
       for i in range(0, newBlobContours.size()):
         d = dist(newBlobContours.get(i).getBoundingBox().x, newBlobContours.get(i).getBoundingBox().y, b.getBoundingBox().x, b.getBoundingBox().y)
         #d = dist(blobs[i].x, blobs[i].y, b.r.x, b.r.y)
         if d < record and !used[i]:
           record = d
           index = i
    
       # Update Blob object location
       used[index] = true
       b.update(newBlobContours.get(index))

    # Add any unused blobs
    for i in range(0, newBlobContours.size()):
      if !used[i]:
        println("+=1+ New blob detected with ID: " + blobCount)
        blobList.add(Blob(this, blobCount, newBlobContours.get(i)))
        #blobList.add(Blob(blobCount, blobs[i].x, blobs[i].y, blobs[i].width, blobs[i].height))
        blobCount+=1

  # SCENARIO 3 
  # We have more Blob objects than blob Rectangles found from OpenCV in this frame
  else:
    # All Blob objects start out as available
    for b in blobList:
      b.available = True

    # Match Rectangle with a Blob object
    for i in range(0, newBlobContours.size()):
      # Find blob object closest to the newBlobContours.get(i) Contour
      # set available to false
       record = 50000
       index = -1
       for j in range(0, blobList.size()):
         b = blobList.get(j)
         d = dist(newBlobContours.get(i).getBoundingBox().x, newBlobContours.get(i).getBoundingBox().y, b.getBoundingBox().x, b.getBoundingBox().y)
         #d = dist(blobs[i].x, blobs[i].y, b.r.x, b.r.y)
         if d < record and b.available:
           record = d
           index = j
        
       # Update Blob object location
       b = blobList.get(index)
       b.available = false
       b.update(newBlobContours.get(i))

    # Start to kill any left over Blob objects
    for b in blobList:
      if b.available:
        b.countDown()
        if b.dead():
          b.delete = true

  # Delete any blob that should be deleted
  for i in range(blobList.size()-1, 0, -1):
    b = blobList.get(i)
    if b.delete:
      blobList.remove(i)

def getBlobsFromContours(newContours):  
  newBlobs = ArrayList<Contour>()
  
  # Which of these contours are blobs?
  for i in range(0, newContours.size()):    
    contour = newContours.get(i)
    r = contour.getBoundingBox()
    
#    if (#(contour.area() > 0.9 * src.width * src.height) ||
    if    (r.width < blobSizeThreshold or r.height < blobSizeThreshold):
      continue
    
    newBlobs.add(contour)

  return newBlobs

#############
# CONTROL P5 Functions
#############
def initControls():
  # Slider for contrast
  cp5.addSlider("contrast")
  cp5.setLabel("contrast")
  cp5.setPosition(20,50)
  cp5.setRange(0.0,6.0)

  # Slider for threshold
  cp5.addSlider("threshold")
  cp5.setLabel("threshold")
  cp5.setPosition(20,110)
  cp5.setRange(0,255)

  # Toggle to activae adaptive threshold
  cp5.addToggle("toggleAdaptiveThreshold")
  cp5.setLabel("use adaptive threshold")
  cp5.setSize(10,10)
  cp5.setPosition(20,144)

  # Slider for adaptive threshold block size
  cp5.addSlider("thresholdBlockSize")
  cp5.setLabel("a.t. block size")
  cp5.setPosition(20,180)
  cp5.setRange(1,700)

  # Slider for adaptive threshold constant
  cp5.addSlider("thresholdConstant")
  cp5.setLabel("a.t. constant")
  cp5.setPosition(20,200)
  cp5.setRange(-100,100)

  # Slider for blur size
  cp5.addSlider("blurSize")
  cp5.setLabel("blur size")
  cp5.setPosition(20,260)
  cp5.setRange(1,20)

  # Slider for minimum blob size
  cp5.addSlider("blobSizeThreshold")
  cp5.setLabel("min blob size")
  cp5.setPosition(20,290)
  cp5.setRange(0,60)

  # Store the default background color, we gonna need it later
  buttonColor = cp5.getController("contrast").getColor().getForeground()
  buttonBgColor = cp5.getController("contrast").getColor().getBackground()


def toggleAdaptiveThreshold(theFlag):  
  useAdaptiveThreshold = theFlag
  
  if useAdaptiveThreshold:
    # Lock basic threshold
    setLock(cp5.getController("threshold"), true)
       
    # Unlock adaptive threshold
    setLock(cp5.getController("thresholdBlockSize"), false)
    setLock(cp5.getController("thresholdConstant"), false)
  else:
    # Unlock basic threshold
    setLock(cp5.getController("threshold"), false)

    # Lock adaptive threshold
    setLock(cp5.getController("thresholdBlockSize"), true)
    setLock(cp5.getController("thresholdConstant"), true)

def setLock(theController, theValue):
  theController.setLock(theValue)

  if theValue:
    theController.setColorBackground(color(150,150))
    theController.setColorForeground(color(100,100))
  else:
    theController.setColorBackground(color(buttonBgColor))
    theController.setColorForeground(color(buttonColor))
