""" oscilExample<br/>
   is an example of using the Oscil UGen inside an instrument.
   <p>
   For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
   <p>
   author: Anderson Mills<br/>
   Anderson Mills's work was supported by numediart (www.numediart.org)
"""

# add_library("everything necessary to make sound.
add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

# create all of the variables that will need to be accessed in
# more than one methods (setup(), draw(), stop()).
Minim minim
AudioOutput out

# Every instrument must implement the Instrument interface so 
# playNote() can call the instrument's methods.
class ToneInstrument implements Instrument
{
  # create all variables that must be used throughout the class
  Oscil sineOsc
  AudioOutput out
  
  # constructors for this intsrument
  ToneInstrument( frequency, amplitude, AudioOutput output )
 :
    # equate class variables to constructor variables as necessary 
    out = output
    
    # create instances of any UGen objects as necessary
    sineOsc = Oscil( frequency, amplitude, Waves.SINE )
  
  
  # every instrument must have a noteOn( ) method
  def noteOn( dur )
 :
    # and patch to the output
    sineOsc.patch( out )
  
  
  # every instrument must have a noteOff() method
  def noteOff()
 :
    # and unpatch the output 
    # this causes the entire instrument to stop calculating sampleframes
    # which is good when the instrument is no longer generating sound.
    sineOsc.unpatch( out )
  


# setup is run once at the beginning
def setup()
{
  # initialize the drawing window
  size( 512, 200, P2D )

  # initialize the minim and out objects
  minim = Minim( this )
  out = minim.getLineOut( Minim.MONO, 2048 )
  
  # initialize the myNote object as a ToneInstrument
  ToneInstrument myNote = ToneInstrument( 587.3f, 0.9, out )
  # play a note with the myNote object
  out.playNote( 0.5, 2.6, myNote )
  # give a note value to myNote
  myNote = ToneInstrument( 415.3f, 0.9, out )
  # play another note with the myNote object
  out.playNote(3.5, 2.6, myNote )


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
    line( x1, 50 - out.left.get(i)*50, x2, 50 - out.left.get(i+1)*50)
    line( x1, 150 - out.right.get(i)*50, x2, 150 - out.right.get(i+1)*50)
    
