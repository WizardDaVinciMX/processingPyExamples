""" filterExample<br/>
 * is an example of using the different filters
 * in continuous sound.
 * <p>
 * For more information about Minim and additional features, 
 * visit http:#code.compartmental.net/minim/
 * <p> 
 * author: Damien Di Fede, Anderson Mills<br/>
 * Anderson Mills's work was supported by numediart (www.numediart.org)
 """

# add_library("everything necessary to make sound.
add_library("ddf.minim.*
add_library("ddf.minim.ugens.*
# the effects package is needed because the filters are there for now.
add_library("ddf.minim.effects.*

# create all of the variables that will need to be accessed in
# more than one methods (setup(), draw(), stop()).
Minim minim
AudioOutput out

# setup is run once at the beginning
def setup()
{
# initialize the drawing window
  size(300, 200, P2D)
  
  # initialize the minim and out objects
  minim = Minim(this)
  out = minim.getLineOut()
  
  # create all of the variables
  IIRFilter filt
  Oscil osc
  Oscil cutOsc
  Constant cutoff

  # initialize the oscillator 
  # (a sawtooth wave has energy across the spectrum)
  osc = Oscil(500, 0.2, Waves.SAW)

  # uncoment one of the filters to hear it's effect
  #filt = LowPassSP(400, out.sampleRate())
  #filt = LowPassFS(400, out.sampleRate())
  filt = BandPass(400, 100, out.sampleRate())
  #filt = HighPassSP(400, out.sampleRate())
  #filt = NotchFilter(400, 100, out.sampleRate())

  # create an Oscil we will use to modulate 
  # the cutoff frequency of the filter.
  # by using an amplitude of 800 and an
  # offset of 1000, the cutoff frequency 
  # will sweep between 200 and 1800 Hertz.
  cutOsc = Oscil(1, 800, Waves.SINE)
  # offset the center value of the Oscil by 1000
  cutOsc.offset.setLastValue( 1000 )

  # patch the oscil to the cutoff frequency of the filter
  cutOsc.patch(filt.cutoff)
  
  # patch the sawtooth oscil through the filter and then to the output
  osc.patch(filt).patch(out)



# draw is run many times
def draw()
{
  # erase the window to black
  background( 0 )
  # draw using a white stroke
  stroke( 255 )
  # draw the waveforms
  for( i = 0 i < out.bufferSize() - 1 i+=1 )
 :
    # find the x position of each buffer value
    x1  =  map( i, 0, out.bufferSize(), 0, width )
    x2  =  map( i+1, 0, out.bufferSize(), 0, width )
    # draw a line from one buffer position to the next for both channels
    line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50)
    line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50)
    

