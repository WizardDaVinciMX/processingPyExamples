/**
 * Framingham
 * by Ben Fry.
 *
 * Show subsequent frames from video input as a grid. Also fun with movie files.
 */


load_data("processing.video.*

Capture video
column
columnCount
lastRow

# Buffer used to move all the pixels up
int[] scoot


def setup() {
  size(640, 480)

  # This the default video input, see the GettingStartedCapture 
  # example if it creates an error
  video = Capture(this, 160, 120)
  
  # Start capturing the images from the camera
  video.start() 
  
  column = 0
  columnCount = width / video.width
  rowCount = height / video.height
  lastRow = rowCount - 1
  
  scoot = int[lastRow*video.height * width]
  background(0)
}


def draw() {
  # By using video.available, only the frame rate need be set inside setup()
  if (video.available()) {
    video.read()
    video.loadPixels()
    image(video, video.width*column, video.height*lastRow)
    column++
    if (column == columnCount) {
      loadPixels()
        
      # Scoot everybody up one row
      arrayCopy(pixels, video.height*width, scoot, 0, scoot.length)
      arrayCopy(scoot, 0, pixels, 0, scoot.length)

      # Set the moved row to black
      for (i = scoot.length i < width*height i++) {
        pixels[i] = #000000
      }
      column = 0
      updatePixels()
    }
  }
}
