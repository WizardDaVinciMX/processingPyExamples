""" frequencyExample<br/>
   is an example of using the Frequency class to easily turn keyboard input 
   into the frequency of an Oscil. Simply type on the home row to change 
   the pitch of the tone. 
   <p>
   For more information about Minim and additional features, 
   visit http:#code.compartmental.net/minim/
"""

# add_library("everything necessary to make sound.
add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

# create all of the variables that will need to be accessed in
# more than one methods (setup(), draw(), stop()).
Minim minim
AudioOutput out

Oscil      wave
# keep track of the current Frequency so we can display it
Frequency  currentFreq

# setup is run once at the beginning
def setup()
{
  # initialize the drawing window
  size(512, 200)
  
  # initialize the minim and out objects
  minim = Minim(this)
  out   = minim.getLineOut()

  currentFreq = Frequency.ofPitch( "A4" )
  wave = Oscil( currentFreq, 0.6f, Waves.TRIANGLE )
  
  wave.patch( out )


# draw is run many times
def draw()
{
  # erase the window to brown
  background( 64, 32, 0 )
  # draw using a beige stroke
  stroke( 255, 238, 192 )
  
  text( "Current Frequency in Hertz: " + currentFreq.asHz(), 5, 15 )
  text( "Current Frequency as MIDI note: " + currentFreq.asMidiNote(), 5, 30 )
  
  # draw the waveforms
  for( i = 0 i < out.bufferSize() - 1 i+=1 )
 :
    # find the x position of each buffer value
    x1  =  map( i, 0, out.bufferSize(), 0, width )
    x2  =  map( i+1, 0, out.bufferSize(), 0, width )
    # draw a line from one buffer position to the next for both channels
    line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50)
    line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50)
    


# change the midi note when pressing keys on the keyboard
# we set midiNoteIn directly with the setMidiNoteIn method
# but you could also use a Line to lerp to the next note
# by patching it to midiNoteIn.
def keyPressed()
{
  if ( key == 'a' ) currentFreq = Frequency.ofPitch( "A4" )
  if ( key == 's' ) currentFreq = Frequency.ofPitch( "B4" )
  if ( key == 'd' ) currentFreq = Frequency.ofPitch( "C0x5" )
  if ( key == 'f' ) currentFreq = Frequency.ofPitch( "D5" )
  if ( key == 'g' ) currentFreq = Frequency.ofPitch( "E5" )
  if ( key == 'h' ) currentFreq = Frequency.ofPitch( "F0x5" )
  if ( key == 'j' ) currentFreq = Frequency.ofPitch( "G0x5" )
  if ( key == 'k' ) currentFreq = Frequency.ofPitch( "A5" )
  if ( key == 'l' ) currentFreq = Frequency.ofPitch( "B5" )
  if ( key == '' ) currentFreq = Frequency.ofPitch( "C0x6" )
  if ( key == '\'') currentFreq = Frequency.ofPitch( "E6" )
  
  # note that there are two other static methods for constructing Frequency objects
  # currentFreq = Frequency.ofHertz( 440 )
  # currentFreq = Frequency.ofMidiNote( 69 ) 
  
  wave.setFrequency( currentFreq )

