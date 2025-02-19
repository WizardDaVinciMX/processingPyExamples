"""*
 * This is a simple white noise generator. White noise has equal power at all
 * frequencies. The high frequencies can make it very grating to the ear.
 """

add_library("sound")

def setup():
  global noise

  size(640, 360)
  background(255)

  # Create and start the noise generator
  noise = WhiteNoise(this)
  noise.play()
      

def draw():
  global noise

  # Map mouseX from -1.0 to 1.0 for left to right
  noise.pan(map(mouseX, 0, width, -1.0, 1.0))

  # Map mouseY from 0.0 to 0.3 for amplitude
  # (the higher the mouse position, the louder the sound)
  noise.amp(map(mouseY, 0, height, 0.3, 0.0))
