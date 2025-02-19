"""
 * Grab audio from the microphone input and draw a circle whose size
 * is determined by how loud the audio input is.
"""

add_library("sound")

def setup() :
  global input
  global loudness

  size(640, 360)
  background(255)

  # Create an Audio input and grab the 1st channel
  input = AudioIn(this, 0)

  # Begin capturing the audio input
  input.start()
  # start() activates audio capture so that you can use it as
  # the input to live sound analysis, but it does NOT cause the
  # captured audio to be played back to you. if you also want the
  # microphone input to be played back to you, call
  input.play()
  # instead (be careful with your speaker volume, you might produce
  # painful audio feedback. best to first try it out wearing headphones!)

  # Create a Amplitude analyzer
  loudness = Amplitude(this)

  # Patch the input to the volume analyzer
  loudness.input(input)



def draw() :
  global input
  global loudness

  # Adjust the volume of the audio input based on mouse position
  inputLevel = map(mouseY, 0, height, 1.0, 0.0)
  input.amp(inputLevel)

  # loudness.analyze() return a value between 0 and 1. To adjust
  # the scaling and mapping of an ellipse we scale from 0 to 0.5
  volume = loudness.analyze()
  size = int(map(volume, 0, 0.5, 1, 350))

  background(125, 255, 125)
  noStroke()
  fill(255, 0, 150)
  # We draw a circle whose size is coupled to the audio analysis
  ellipse(width/2, height/2, size, size)
