"""*
 * Allocate a audio sample and manually fill it with a sine wave that gets
 * scrambled every time the mouse is pressed. As the order of data points is scrambled
 * more and more, the original sine wave signal becomes less and less audible until it
 * is completely washed out by noise artefacts.
 """

add_library("sound")

def setup():
  global sample

  size(640, 360)
  background(255)

  # Manually write a sine wave oscillations into an array.
  resolution = 1000
  sinewave =[0.8]* resolution
  for i in range(0, resolution):
    sinewave[i] = sin(TWO_PI*i/resolution)
  

  # Initialize the audiosample, set framerate to play 200 oscillations/second
  sample = AudioSample(this, sinewave, 500 * resolution)

  # Play the sample in a loop (but don't make it too loud)
  sample.amp(0.2)
  sample.loop()
      


def draw():
    pass


def mousePressed():
  global sample

  # Every time the mouse is pressed, swap two of the sample frames around.
  i = int(random(0, sample.frames()))
  j = int(random(0, sample.frames()))

  # Read a frame each from their respective positions
  onevalue = sample.read(i)
  othervalue = sample.read(j)
  # and write them back the other way around
  sample.write(i, othervalue)
  sample.write(j, onevalue)
