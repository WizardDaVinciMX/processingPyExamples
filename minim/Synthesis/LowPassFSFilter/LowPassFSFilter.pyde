"""*
  * This sketch demonstrates how to use one of the low pass filters that come with Minim.<br />
  * Move the mouse to the right to increase the cutoff frequency, move it to the left to decrease it.
  * <p>
  * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*
add_library("ddf.minim.effects.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput output
FilePlayer  groove
LowPassFS   lpf

def setup()
{
  size(512, 200, P3D)
  minim = Minim(this)
  output = minim.getLineOut()
  groove = FilePlayer( minim.loadFileStream("groove.mp3") )
  # make a low pass filter with a cutoff frequency of 100 Hz
  # the second argument is the sample rate of the audio that will be filtered
  # it is required to correctly compute values used by the filter
  lpf = LowPassFS(100, output.sampleRate())
  groove.patch( lpf ).patch( output )
  
  groove.loop()


def draw()
{
  background(0)
  stroke(255)
  # we multiply the values returned by get by 50 so we can see the waveform
  for ( i = 0 i < output.bufferSize() - 1 i+=1 )
 :
    x1 = map(i, 0, output.bufferSize(), 0, width)
    x2 = map(i+1, 0, output.bufferSize(), 0, width)
    line(x1, height/4 - output.left.get(i)*50, x2, height/4 - output.left.get(i+1)*50)
    line(x1, 3*height/4 - output.right.get(i)*50, x2, 3*height/4 - output.right.get(i+1)*50)
  


def mouseMoved()
{
  # map the mouse position to the range [60, 2000], an arbitrary range of cutoff frequencies
  cutoff = map(mouseX, 0, width, 60, 2000)
  lpf.setFreq(cutoff)
  #lpf.printCoeff()
