"""*
 * Play a sound sample and pass it through a tape delay, changing the delay
 * parameters based on the mouse position.
 """

add_library("sound")

def setup() :
  global soundfile
  global delay

  size(640, 360)
  background(255)

  # Load a soundfile
  soundfile = SoundFile(this, "vibraphon.aiff")

  # Create the delay effect
  delay = Delay(this)

  # Play the file in a loop
  soundfile.loop()

  # Connect the soundfile to the delay unit, which is initiated with a
  # five second "tape"
  delay.process(soundfile, 5.0)


def draw() : 
  global soundfile
  global delay

  # Map mouseX from -1.0 to 1.0 for left to right panning
  position = map(mouseX, 0, width, -1.0, 1.0)
  soundfile.pan(position)

  # Map mouseX from 0 to 0.8 for the amount of delay feedback
  fb = map(mouseX, 0, width, 0.0, 0.8)
  delay.feedback(fb)

  # Map mouseY from 0.001 to 2.0 seconds for the length of the delay
  delayTime = map(mouseY, 0, height, 0.001, 2.0)
  delay.time(delayTime)
