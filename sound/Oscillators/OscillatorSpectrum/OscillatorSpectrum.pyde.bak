"""*
 * Inspect the frequency spectrum of different simple oscillators.
 """

add_library("sound")

# All oscillators are instances of the Oscillator superclass.
oscs = [0]*5

# Store information on which of the oscillators is currently playing.
current = 0

fftBands = 512

def setup() :
  global oscs
  global current
  global fft
  global fftBands

  size(640, 360)
  background(255)

  # Turn the volume down globally.
  s = Sound(this)
  s.volume(0.2)

  # Create the oscillators and put them into an array.
  oscs[0] = SinOsc(this)
  oscs[1] = TriOsc(this)
  oscs[2] = SawOsc(this)
  oscs[3] = SqrOsc(this)

  # Special treatment for the Pulse oscillator to set its pulse width.
  pulse = Pulse(this)
  pulse.width(0.05)
  oscs[4] = pulse

  # Initialise the FFT and start playing the (default) oscillator.
  fft = FFT(this, 512)
  oscs[current].play()
  fft.input(oscs[current])


def draw() :
  global current

  # Only play one of the four oscillators, based on mouseY
  nextOscillator = constrain(floor(map(mouseY, 0, height, 0, len(oscs))), 0, len(oscs) - 1)

  if nextOscillator != current:
    oscs[current].stop()
    current = nextOscillator

    # Switch FFT analysis over to the newly selected oscillator.
    fft.input(oscs[current])
    # Play
    oscs[current].play()
  

  # Map mouseX from 20Hz to 22000Hz for frequency.
  frequency = map(mouseX, 0, width, 20.0, 22000.0)
  # Update oscillator frequency.
  oscs[current].freq(frequency)


  # Draw frequency spectrum.
  background(125, 255, 125)
  fill(255, 0, 150)
  noStroke()

  fft.analyze()

  r_width = width/float(fftBands)

  for i in range(0, fftBands) :
    rect( i*r_width, height, r_width, -fft.spectrum[i]*height)
  

  # Display the name of the oscillator class.
  textSize(32)
  fill(0)
  verticalPosition = map(current, -1, len(oscs), 0, height)
  text(oscs[current].getClass().getSimpleName(), 0, verticalPosition)
