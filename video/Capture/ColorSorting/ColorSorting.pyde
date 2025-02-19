"""
 * Color Sorting  
 * by Ben Fry. 
 *
 * Example that sorts all colors from the incoming video
 * and arranges them into vertical bars.
"""
 
 
add_library("video")

cheatScreen = False

# How many pixels to skip in either direction
increment = 5

def setup():
  global video
  global cheatScreen
  global captureColors
  global bright

  size(800, 600)
  
  # This the default video input, see the GettingStartedCapture 
  # example if it creates an error
  video = Capture(this, 160, 120)
  
  # Start capturing the images from the camera
  video.start()  
  
  count = (video.width * video.height) / (increment * increment)
  bright = [0] * count
  captureColors = [0] * count
  drawColors = [0] * count
  for i in range(0, count):
    captureColors[i] = list()
    drawColors[i] = [0.5, 0.5, 0.5]


def draw():
  global captureColors

  if video.available():
    video.read()
    video.loadPixels()
    
    background(0)
    noStroke()

    index = 0
    for j in range(0, video.height, increment):
      for i in range(0, video.width, increment):
        pixelColor = video.pixels[j*video.width + i]

        r = (pixelColor >> 16) & 0xff
        g = (pixelColor >> 8) & 0xff
        b = pixelColor & 0xff

        # Technically would be sqrt of the following, but no need to do
        # sqrt before comparing the elements since we're only ordering
        bright[index] = r*r + g*g + b*b
        captureColors[index] = (r, g, b)

        index+=1

    sort(index, bright, captureColors)

    beginShape(QUAD_STRIP)
    for i in range(0, index):
      drawColors[i].target(captureColors[i], 0.1)
      drawColors[i].phil()

      x = map(i, 0, index, 0, width)
      vertex(x, 0)
      vertex(x, height)
    endShape()

    if cheatScreen:
      #image(video, 0, height - video.height)
      # Faster method of displaying pixels array on screen
      set(0, height - video.height, video)


def keyPressed():
  if   key == 'g':
    saveFrame()
  elif key == 'c':
    cheatScreen = !cheatScreen


# Functions to handle sorting the color data

def sort(length, a, stuff):
  sortSub(a, stuff, 0, length - 1)

def sortSwap(a, stuff, i, j):
  T = a[i]
  a[i] = a[j]
  a[j] = T

  v = stuff[i]
  stuff[i] = stuff[j]
  stuff[j] = v

def sortSub(a, stuff, lo0, hi0):
  lo = lo0
  hi = hi0

  if hi0 > lo0:
    mid = a[(lo0 + hi0) / 2]

    while lo <= hi:
      while (lo < hi0) and (a[lo] < mid):
        ++lo

      while (hi > lo0) and (a[hi] > mid):
        --hi

      if lo <= hi:
        sortSwap(a, stuff, lo, hi)
        ++lo
        --hi

    if lo0 < hi:
      sortSub(a, stuff, lo0, hi)

    if lo < hi0:
      sortSub(a, stuff, lo, hi0)
