""" maxInstrExample<br/>
   is an example of using the Oscil UGen to find out how many single oscillator
   instruments can run synchronously on one's system.  If you press a key while it is playing,
   it will write the audio so far to a WAV file.  The WAV file doesn't have any problems, but
   given enough oscillator instruments, one's system will.
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

# setup is run once at the beginning
def setup()
{
  # initialize the drawing window
  size(512, 200, P2D)

  # initialize the minim and out objects
  minim = Minim(this)
  out = minim.getLineOut(Minim.MONO, 2048)

  # choose the total number of single oscillator instruments to generate
  # i've never exceeded 100, but I'm getting closer as we refine Minim
  nNotes = 100
  # lowest frequency generated
  baseNote = 86.13
  # using tempo here just makes it easier to generate noteOns below
  out.setTempo( 200 )
  # pause time so that all notes can be added at once with guaranteed timing
  out.pauseNotes()
  
  # generate all the possible single note ascillators
  for( i = 0 i < nNotes i+=1 )
 :
    out.playNote( i , nNotes + 2 - i, 
       NumberInstrument( (3+i)*baseNote, 0.05*(nNotes-i)/nNotes, i, out) )
  
  # resume time for the group of added notes
  out.resumeNotes()


# draw is run many times
def draw()
{
  # erase the window to yellow
  background( 238, 192, 0 )
  # draw using a black stroke
  stroke( 0 )
  # draw the waveforms
  for( i = 0 i < out.bufferSize() - 1 i+=1 )
 :
    # find the x position of each buffer value
    x1  =  map( i, 0, out.bufferSize(), 0, width )
    x2  =  map( i+1, 0, out.bufferSize(), 0, width )
    # draw a line from one buffer position to the next for both channels
    line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50)
    line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50)
    
