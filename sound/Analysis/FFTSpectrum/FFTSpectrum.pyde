"""*
 * This sketch shows how to use the FFT class to analyze a stream
 * of sound. Change the number of bands to get more spectral bands
 * (at the expense of more coarse-grained time resolution of the spectrum).
 """

add_library("sound")

# Define how many FFT bands to use (this needs to be a power of two)
bands = 128

# Define a smoothing factor which determines how much the spectrums of consecutive
# points in time should be combined to create a smoother visualisation of the spectrum.
# A smoothing factor of 1.0 means no smoothing (only the data from the newest analysis
# is rendered), decrease the factor down towards 0.0 to have the visualisation update
# more slowly, which is easier on the eye.
smoothingFactor = 0.2

# Create a vector to store the smoothed spectrum data in
sum = [0.0]*bands

# Variables for drawing the spectrum:
# Declare a scaling factor for adjusting the height of the rectangles
scale = 5

def setup() :
  global sample
  global fft
  global bands
  global smoothingFactor
  global sum
  global scale
  global barWidth
  
  size(640, 360)
  background(255)

  # Calculate the width of the rects depending on how many bands we have
  barWidth = width/float(bands)

  # Load and play a soundfile and loop it.
  sample = SoundFile(this, "beat.aiff")
  sample.loop()

  # Create the FFT analyzer and connect the playing soundfile to it.
  fft = FFT(this, bands)
  fft.input(sample)


def draw() :
  global sample
  global fft
  global bands
  global smoothingFactor
  global sum
  global scale
  global barWidth
  
  # Set background color, noStroke and fill color
  background(125, 255, 125)
  fill(255, 0, 150)
  noStroke()

  # Perform the analysis
  fft.analyze()

  for i in range(0, bands) :
    # Smooth the FFT spectrum data by smoothing factor
    sum[i] += (fft.spectrum[i] - sum[i]) * smoothingFactor

    # Draw the rectangles, adjust their height using the scale factor
    rect(i*barWidth, height, barWidth, -sum[i]*height*scale)
  
