"""*
  * This sketch demonstrates how to use the notch, or band reject, filter that comes with Minim.<br />
  * Move mouse left and right change the center frequency of the band to reject, <br />
  * move it up and down to change the band width of the reject band.
  * <p>
  * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/ 
  """

add_library("ddf.minim.*
add_library("ddf.minim.effects.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput  output
FilePlayer groove
NotchFilter ntf

def setup()
{
  size(512, 200, P3D)
  minim = Minim(this)
  output = minim.getLineOut()
  groove = FilePlayer( minim.loadFileStream("groove.mp3") )
  # make a low pass filter with a cutoff frequency of 100 Hz
  # the second argument is the sample rate of the audio that will be filtered
  # it is required to correctly compute values used by the filter
  ntf = NotchFilter(440, 20, output.sampleRate())
  groove.patch(ntf).patch(output)
  
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
  
  # draw a rectangle to represent the reject band
  noStroke()
  fill(255, 0, 0, 60)
  rect(mouseX - ntf.getBandWidth()/20, 0, ntf.getBandWidth()/10, height)


def mouseMoved()
{
  # map mouseX to the range [100, 10000], an arbitrary range of band reject frequencies
  notchBand = map(mouseX, 0, width, 100, 2000)
  ntf.setFreq(notchBand)
  # map mouseY to the range [50, 500], and arbitrary range of band widths
  bandWidth = map(mouseY, 0, height, 50, 500)
  ntf.setBandWidth(bandWidth)
  ntf.printCoeff()
