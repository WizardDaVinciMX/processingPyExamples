""" algorithmicCompExample<br/>
   is an example of algorithmic composition.  It uses a class to construct
   sentences.  The syllables of the words are played by an Instrument.
   This is intended to sound like a conversation between two robots, where
   the voice of each robot is inspired by the teacher from the Peanuts cartoons. 
   <p>
   For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
   <p>
   authour: Anderson Mills<br/>
   Anderson Mills's work was supported by numediart (www.numediart.org)
"""

# add_library("everything necessary to make sound.
add_library("ddf.minim.*
add_library("ddf.minim.ugens.*
add_library("ddf.minim.effects.*

# create all of the variables that will need to be accessed in
# more than one methods (setup(), draw(), stop())
Minim minim
AudioOutput out

# setup is run once at the beginning
def setup()
{
  # initialize the drawing window
  size(512, 200, P2D)
  
  # initialize the minim, out, and recorder objects
  minim = Minim(this)
  out = minim.getLineOut(Minim.STEREO, 1024)

  # many different variables which give appropriate ronges for the 
  # rhythm of the sentences and the syllables
  nSentences = 23      # total number of sentences
  fundFreqA = 110.0  # fundamental freq of talker A
  fundFreqB = 146.0  # fundamental freq of talker B
  balanceA = 0.3     # stereo position of talker A
  balanceB = -0.3    # stereo position of talker B
  gapMin = 0.5       # min gap between sentences
  gapMax = 1.9       # max gap between sentences
  
  # specify that time in beats is also time in seconds
  out.setTempo( 60f )
  
  # give a 1 second pause before any talking
  out.setNoteOffset( 1.0 )
  
  # create a "teacher"
  PeanutsSentencer theTeacher
  theTeacher = PeanutsSentencer( out )
  
  # In the following for loop, theTeacher is called to create a sentence several times.
  # theTeacher eventually calls out.playNote() using the PeanutsSyllableInstrument, which
  # puts notes in the queue to be played.  theTeacher returns the length of the sentence
  # so that a gap and the next sentence can be generated. 
  
  # keeping track of where the conversation is in time
  startSum = 0.0
  
  # cycle through all of the sentences
  for ( iSent = 0 iSent < nSentences iSent +=1 )
 :
    # choose which talker will be saying the sentence
    fundFreq, balance
    if ( iSent%2 == 0 )
   :
      fundFreq = fundFreqA
      balance = balanceA
     else
   :
      fundFreq = fundFreqB
      balance = balanceB
    
    
    # set up theTeacher for the next sentence
    theTeacher.setParameters( startSum, fundFreq, balance )
    # have theTeacher make the playNote calls and return the length of the sentence
    lastLen = theTeacher.saySentence()
    # add in a little gap
    gapTime = (float)Math.random()*(gapMax - gapMin ) + gapMin
    # and move the coversation forward
    startSum += lastLen + gapTime
  


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
    
