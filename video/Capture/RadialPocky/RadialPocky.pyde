/** 
 * Radial Pocky
 * by Ben Fry. 
 *
 * Unwrap each frame of live video into a single line of pixels along a circle
 */ 
  
load_data("processing.video.*

Capture video
videoCount
currentAngle
pixelCount
angleCount = 200  # how many divisions

radii[]
angles[]


def setup() {
  # size must be set to video.width*video.height*2 in both directions
  size(600, 600) 

  # This the default video input, see the GettingStartedCapture 
  # example if it creates an error
  video = Capture(this, 160, 120)
  
  # Start capturing the images from the camera
  video.start()  
  
  videoCount = video.width * video.height

  pixelCount = width*height
  centerX = width / 2
  centerY = height / 2
  radii = int[pixelCount]
  angles = int[pixelCount]

  offset = 0
  for (y = 0 y < height y++) {
    for (x = 0 x < width x++) {
      dx = centerX - x
      dy = centerY - y

      angle = atan2(dy, dx)
      if (angle < 0) angle += TWO_PI
      angles[offset] = (int) (angleCount * (angle / TWO_PI))

      radius = (int) mag(dx, dy)
      if (radius >= videoCount) {
        radius = -1
        angles[offset] = -1
      }
      radii[offset] = radius
      
      offset++
    }
  }
  background(0)
}


def draw() {
  if (video.available()) {
    video.read()
    video.loadPixels()
  
    loadPixels()
    for (i = 0 i < pixelCount i++) {
      if (angles[i] == currentAngle) {
        pixels[i] = video.pixels[radii[i]]
      }
    }
    updatePixels()
    
    currentAngle++
    if (currentAngle == angleCount) {
      currentAngle = 0
    }
  }
}
