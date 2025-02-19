"""*
 * Play a sound sample and apply a reverb filter to it, changing the effect
 * parameters based on the mouse position.
 *
 * With the mouse pointer at the top of the sketch you'll only hear the "dry"
 * (unprocessed) signal, move the mouse downwards to add more of the "wet"
 * reverb signal to the mix. The left-right position of the mouse controls the
 * "room size" and damping of the effect, with a smaller room (and more refraction)
 * at the left, and a bigger (but more dampened) room towards the right.
 """

add_library("sound")

def setup() :
  global soundfile
  global reverb

  size(640, 360)
  background(255)

  # Load a soundfile
  soundfile = SoundFile(this, "vibraphon.aiff")

  # Create the effect object
  reverb = Reverb(this)

  # Play the file in a loop
  soundfile.loop()

  # Set soundfile as input to the reverb 
  reverb.process(soundfile)


def draw() :
  global soundfile
  global reverb

  # Change the roomsize of the reverb
  roomSize = map(mouseX, 0, width, 0, 1.0)
  reverb.room(roomSize)

  # Change the high frequency dampening parameter
  damping = map(mouseX, 0, width, 0, 1.0)
  reverb.damp(damping)

  # Change the wet/dry relation of the effect
  effectStrength = map(mouseY, 0, height, 0, 1.0)
  reverb.wet(effectStrength)
