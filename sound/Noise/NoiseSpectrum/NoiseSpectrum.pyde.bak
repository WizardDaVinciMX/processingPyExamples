"""*
 * Inspect the frequency spectrum of different types of noise.
 """

add_library("sound")

# All noise generators are instances of the Noise superclass.
noises = [0]*3

# Store information on which of the noises is currently playing.
current = 0

fftBands = 512

def setup():
  global noises
  global current
  global fft
  global fftBands

  size(640, 360)
  background(255)

  # Turn the volume down globally.
  s = Sound(this)
  s.volume(0.2)

  # Create the noise generators and put them into an array.
  noises[0] = WhiteNoise(this)
  noises[1] = PinkNoise(this)
  noises[2] = BrownNoise(this)

  # Initialise the FFT and start playing the (default) noise generator.
  fft = FFT(this, 512)
  noises[current].play()
  fft.input(noises[current])


def draw() :
  global current

  # Only play one of the four oscillators, based on mouseY
  nextNoise = constrain(floor(map(mouseY, 0, height, 0, len(noises))), 0, len(noises) - 1)

  if nextNoise != current:
    noises[current].stop()
    current = nextNoise

    # Switch FFT analysis over to the newly selected noise generator.
    fft.input(noises[current])
    # Start playing noise
    noises[current].play()
  

  # Draw frequency spectrum.
  background(125, 255, 125)
  fill(255, 0, 150)
  noStroke()

  fft.analyze()

  r_width = width/float(fftBands)

  for i in range(0, fftBands):
    rect( i*r_width, height, r_width, -fft.spectrum[i]*height)
  

  # Display the name of the noise generator class.
  textSize(32)
  fill(0)
  verticalPosition = map(current, -1, len(noises), 0, height)
  text(noises[current].getClass().getSimpleName(), 0, verticalPosition)
