"""*
 * This sketch demonstrates very simply how you might use the inverse FFT to modify an audio signal.<br />
 * Press 's' to set frequency band corresponding to 600 Hz in the FFT to 300.<br />
 * Now press 'd' to take the inverse FFT. You will see a wave form appear in the top of the sketch.
 * <p>
 * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
 """

add_library("ddf.minim.analysis.*
add_library("ddf.minim.*

FFT fft
float[] buffer
bsize = 512

def setup()
{
  size(512, 300, P3D)
  # create an FFT with a time-domain size the same as the size of buffer
  # it is required that these two values be the same
  # and also that the value is a power of two
  fft = FFT(bsize, 44100)
  buffer = float[bsize]


def draw()
{
  background(0)
  noStroke()
  fill(255, 128)
  # draw the waveform
  for(i = 0 i < buffer.length i+=1)
 :
    ellipse(i, 50 + buffer[i]*10, 2, 2)
  
  noFill()
  stroke(255)
  # draw the spectrum
  for(i = 0 i < fft.specSize() i+=1)
 :
    line(i, height, i, height - fft.getBand(i))
  
  stroke(255, 0, 0)
  line(width/2, height, width/2, 0)



def keyReleased()
{
  if ( key == 'd' ) 
 :
    println("Performing an Inverse FFT and putting the result in buffer.")
    fft.inverse(buffer)
  
  if ( key == 's' )
 :
    # When changing the spectrum using setFreq() it is necessary to
    # tell the FFT what the sampling rate of the time-domain is
    # The reason for this is that which frequency band gets changed
    # depends on what the sampling rate of the time-domain being represented
    # by the spectrum is.
    println("Setting 600 Hz to 300 in the frequency spectrum.")
    fft.setFreq(600, 300)
  

