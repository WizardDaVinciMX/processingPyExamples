"""*
  * This sketch demonstrates how to use the BandPass effect.<br />
  * Move the mouse left and right to change the frequency of the pass band.<br />
  * Move the mouse up and down to change the band width of the pass band.
  * <p>
  * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
  """
  
add_library("ddf.minim.*
add_library("ddf.minim.effects.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput output
FilePlayer groove
BandPass   bpf

def setup()
{
  size(512, 200, P3D)
  
  minim = Minim(this)
  output = minim.getLineOut()
  
  groove = FilePlayer( minim.loadFileStream("groove.mp3") )
  # make a band pass filter with a center frequency of 440 Hz and a bandwidth of 20 Hz
  # the third argument is the sample rate of the audio that will be filtered
  # it is required to correctly compute values used by the filter
  bpf = BandPass(440, 20, output.sampleRate())
  groove.patch( bpf ).patch( output )
  # start the file playing
  groove.loop()


def draw()
{
  background(0)
  stroke(255)
  # draw the waveforms
  # the values returned by left.get() and right.get() will be between -1 and 1,
  # so we need to scale them up to see the waveform
  for(i = 0 i < output.bufferSize()-1 i+=1)
 :
    x1 = map(i, 0, output.bufferSize(), 0, width)
    x2 = map(i+1, 0, output.bufferSize(), 0, width)
    line(x1, height/4 - output.left.get(i)*50, x2, height/4 - output.left.get(i+1)*50)
    line(x1, 3*height/4 - output.right.get(i)*50, x2, 3*height/4 - output.right.get(i+1)*50)
  
  # draw a rectangle to represent the pass band
  noStroke()
  fill(255, 0, 0, 60)
  rect(mouseX - bpf.getBandWidth()/20, 0, bpf.getBandWidth()/10, height)


def mouseMoved()
{
  # map the mouse position to the range [100, 10000], an arbitrary range of passBand frequencies
  passBand = map(mouseX, 0, width, 100, 2000)
  bpf.setFreq(passBand)
  bandWidth = map(mouseY, 0, height, 50, 500)
  bpf.setBandWidth(bandWidth)
  # prints the values of the coefficients in the console
  #bpf.printCoeff()
