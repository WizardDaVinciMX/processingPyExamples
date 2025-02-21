"""
 MultipleColorTracking
 Select 4 colors to track them separately

 It uses the OpenCV for Processing library by Greg Borenstein
 https:#github.com/atduskgreg/opencv-processing

 @author: Jordi Tost (@jorditost)
 @url: https:#github.com/jorditost/ImageFiltering/tree/master/MultipleColorTracking

 University of Applied Sciences Potsdam, 2014

 Instructions:
 Press one numerical key [1-4] and click on one color to track it
"""
 
add_library("opencv_processing")
add_library("video")
from java.awt import Rectangle

video = None
opencv = None
src = None
contours = None

# <1> Set the range of Hue values for our filter
#ArrayList<Integer> colors
maxColors = 4
hues = None
colors = None
rangeWidth = 10

outputs = [None] * maxColors

colorToChange = -1

def setup():
  global video
  global opencv
  global contours
  global colors
  global hues
  global outputs

  video = Capture(this, "pipeline:autovideosrc")
  opencv = OpenCV(this, video.width, video.height)
  contours = list()
  
  size(830, 480, P2D)
  
  # Array for detection colors
  colors = [0] * maxColors
  hues   = [0] * maxColors
  
  outputs = [None] * maxColors
  
  video.start()


def draw():
  global video
  global opencv
  global outputs

  background(150)
  
  if video.available():
    video.read()
  

  # <2> Load the frame of our movie in to OpenCV
  opencv.loadImage(video)
  
  # Tell OpenCV to use color information
  opencv.useColor()
  src = opencv.getSnapshot()
  
  # <3> Tell OpenCV to work in HSV color space.
  opencv.useColor(HSB)
  
  detectColors()
  
  # Show images
  image(src, 0, 0)
  for i in range(0, len(outputs)):
    if outputs[i] != None:
      image(outputs[i], width-src.width/4, i*src.height/4, src.width/4, src.height/4)
      
      noStroke()
      fill(colors[i])
      rect(src.width, i*src.height/4, 30, src.height/4)
    
  
  
  # Prtext if color expected
  textSize(20)
  stroke(255)
  fill(255)
  
  if colorToChange > -1:
    text("click to change color " + str(colorToChange), 10, 25)
  else:
    text("press key [1-4] to select color", 10, 25)
  
  
  displayContoursBoundingBoxes()


###########
# Detect Functions
###########

def detectColors():
  global hues
  global outputs

  for i in range(0, len(hues)):
    
    if hues[i] <= 0:
      continue
    
    opencv.loadImage(src)
    opencv.useColor(HSB)
    
    # <4> Copy the Hue channel of our image into 
    #     the gray channel, which we process.
    opencv.setGray(opencv.getH().clone())
    
    hueToDetect = hues[i]
    #println("index " + i + " - hue to detect: " + hueToDetect)
    
    # <5> Filter the image based on the range of 
    #     hue values that match the object we want to track.
    opencv.inRange(hueToDetect-rangeWidth/2, hueToDetect+rangeWidth/2)
    
    #opencv.dilate()
    opencv.erode()
    
    # TO DO:
    # Add here some image filtering to detect blobs better
    
    # <6> Save the processed image for reference.
    outputs[i] = opencv.getSnapshot()
  
  
  # <7> Find contours in our range image.
  #     Passing 'true' sorts them by descending area.
  if outputs[0] != None:
    opencv.loadImage(outputs[0])
    contours = opencv.findContours(true,true)
  


def displayContoursBoundingBoxes():
  
  for i in range(0, len(contours)):
    contour = contours[i]
    r = contour.getBoundingBox()
    
    if r.width < 20 or r.height < 20:
      continue
    
    stroke(255, 0, 0)
    fill(255, 0, 0, 150)
    strokeWeight(2)
    rect(r.x, r.y, r.width, r.height)
  


###########
# Keyboard / Mouse
###########

def mousePressed():
  global hues
  global colors

  if colorToChange > -1:
    
    c = get(mouseX, mouseY)
    println("r: " + str(red(c)) + " g: " + str(green(c)) + " b: " + str(blue(c)))
   
    h = int(map(hue(c), 0, 255, 0, 180))
    
    colors[colorToChange-1] = c
    hues[colorToChange-1] = h
    
    println("color index " + str(colorToChange-1) + ", value: " + str(h))
  


def keyPressed():
  global colorToChange

  if    key == '1':
    colorToChange = 1
  elif key == '2':
    colorToChange = 2
  elif key == '3':
    colorToChange = 3
  elif key == '4':
    colorToChange = 4
  

def keyReleased():
  global colorToChange

  colorToChange = -1 
