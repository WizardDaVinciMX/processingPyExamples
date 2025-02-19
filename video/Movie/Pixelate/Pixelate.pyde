/**
 * Pixelate  
 * by Hernando Barragan.  
 * 
 * Load a QuickTime file and display the video signal 
 * using rectangles as pixels by reading the values stored 
 * in the current video frame pixels array. 
 */

load_data("processing.video.*

numPixelsWide, numPixelsHigh
blockSize = 10
Movie mov
color movColors[]

def setup() {
  size(560, 406)
  noStroke()
  mov = Movie(this, "launch2.mp4")
  mov.loop()
  numPixelsWide = width / blockSize
  numPixelsHigh = height / blockSize
  println(numPixelsWide)
  movColors = color[numPixelsWide * numPixelsHigh]
}

# Display values from movie
def draw() {
  if (mov.available() == true) {
    mov.read()
    mov.loadPixels()
    count = 0
    for (j = 0 j < numPixelsHigh j++) {
      for (i = 0 i < numPixelsWide i++) {
        movColors[count] = mov.get(i*blockSize, j*blockSize)
        count++
      }
    }
  }

  background(255)
  for (j = 0 j < numPixelsHigh j++) {
    for (i = 0 i < numPixelsWide i++) {
      fill(movColors[j*numPixelsWide + i])
      rect(i*blockSize, j*blockSize, blockSize, blockSize)
    }
  }

}