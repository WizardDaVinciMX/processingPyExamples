"""*
 * This example shows how to create a cluster of sine oscillators, change the frequency
 * and detune them relative to each other depending on the position of the mouse in the
 * renderer window. The Y position determines the basic frequency of the oscillators,
 * the X position their detuning. The basic frequncy ranges between 150 and 1150 Hz.
 """

add_library("sound")

# The number of oscillators
numSines = 5 

def setup():
  global sineWaves
  global sineVolume

  size(500, 500)
  background(255)

  # Create the oscillators and amplitudes
  sineWaves = [SinOsc(this)] * numSines
  sineVolume = [0.0] * numSines

  for i in range(0, numSines):

    # The overall amplitude shouldn't exceed 1.0 which is prevented by 1.0/numSines.
    # The ascending waves will get lower in volume the higher the frequency.
    sineVolume[i] = (1.0 / numSines) / (i + 1)

    # Create the Sine Oscillators and start them
    sineWaves[i] = SinOsc(this)
    sineWaves[i].play()
  


def draw():
  global sineWaves

  noStroke()

  # Map mouseY to get values from 0.0 to 1.0
  yoffset = (height - mouseY) / float(height)

  # Map that value logarithmically to 150 - 1150 Hz
  frequency = pow(1000, yoffset) + 150

  # Map mouseX from -0.5 to 0.5 to get a multiplier for detuning the oscillators
  detune = float(mouseX) / width - 0.5

  # Set the frequencies, detuning and volume
  for i in range(0, numSines): 
    sineWaves[i].freq(frequency * (i + 1 + i * detune))
    sineWaves[i].amp(sineVolume[i])
  
