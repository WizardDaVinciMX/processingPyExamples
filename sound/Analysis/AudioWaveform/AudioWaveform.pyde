"""*
 * This sketch shows how to use the Waveform class to analyze a stream
 * of sound. Change the number of samples to extract and draw a longer/shorter
 * part of the waveform.
 """

add_library("sound")

# Define how many samples of the Waveform you want to be able to read at once
samples = 100

def setup() :
  global sample
  global waveform
  global samples

  size(640, 360)
  background(255)

  # Load and play a soundfile and loop it.
  sample = SoundFile(this, "beat.aiff")
  sample.loop()

  # Create the Waveform analyzer and connect the playing soundfile to it.
  waveform = Waveform(this, samples)
  waveform.input(sample)


def draw() :
  global sample
  global waveform
  global samples

  # Set background color, noFill and stroke style
  background(0)
  stroke(255)
  strokeWeight(2)
  noFill()

  # Perform the analysis
  waveform.analyze()
  
  beginShape()
  for i in range( 0, samples):
    # Draw current data of the waveform
    # Each sample in the data array is between -1 and +1 
    vertex(
      map(i, 0, samples, 0, width),
      map(waveform.data[i], -1, 1, 0, height)
    )
  
  endShape()
