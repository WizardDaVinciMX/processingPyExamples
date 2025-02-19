"""*
 * This is a sine wave oscillator. The method .play() starts the oscillator. There
 * are several setter functions for configuring the oscillator, such as .amp(),
 * .freq(), .pan() and .add(). If you want to set all of them at the same time you can
 * use .set(freq, amp, add, pan)
 """

add_library("sound")

def setup():
  global sine

  size(640, 360)
  background(255)

  # create and start the sine oscillator.
  sine = SinOsc(this)
  sine.play()


def draw() :
  global sine

  # Map mouseY from 0.0 to 1.0 for amplitude
  amplitude = map(mouseY, 0, height, 1.0, 0.0)
  sine.amp(amplitude)

  # Map mouseX from 20Hz to 1000Hz for frequency  
  frequency = map(mouseX, 0, width, 80.0, 1000.0)
  sine.freq(frequency)

  # Map mouseX from -1.0 to 1.0 for panning the audio to the left or right
  panning = map(mouseX, 0, width, -1.0, 1.0)
  sine.pan(panning)
