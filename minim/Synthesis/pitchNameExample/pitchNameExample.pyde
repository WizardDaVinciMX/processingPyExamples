""" pitchNameExample<br/>
   is an example of using the pitch names for notes instead
   of the frequency in Hertz or the midi note number.  This is
   achieved in the pitchNameInstrument using the ofPitch() and
   asHz() methods of the Frequency class.
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
  size( 512, 200, P2D )

  # initialize the minim and out objects
  minim = Minim( this )
  out = minim.getLineOut( Minim.MONO, 2048 )
  
  # pause time when adding a bunch of notes at once
  # This guarantees accurate timing between all notes added at once.
  out.pauseNotes()
  
  # set the tempo for the piece
  out.setTempo( 90.0 )
  
  # a pause before the music starts
  out.setNoteOffset( 2.0 )

  # using a single parameter to control the amplitude (volume) of all notes
  vol = 0.33
  
  # the first bit all in English note names with octave numbers
  # Capital letters are needed for the notes in English.
  # The notes can also have a series of flats (b) and sharps (0x).
  # A4 is 440 Hz in this equal-temperment tuning.
  out.playNote( 0.00, 0.2, PitchNameInstrument( "E5", vol ) )
  out.playNote( 0.25, 0.2, PitchNameInstrument( "E5", vol ) )
  out.playNote( 0.75, 0.2, PitchNameInstrument( "E5", vol ) )
  out.playNote( 1.25, 0.2, PitchNameInstrument( "C5", vol ) )
  out.playNote( 1.50, 0.2, PitchNameInstrument( "E5", vol ) )
  out.playNote( 2.00, 0.2, PitchNameInstrument( "G5", vol ) )
  out.playNote( 2.75, 0.2, PitchNameInstrument( "G4", vol ) )
  
  # the rest in solfege.
  # Note that a missing octave number defaults to octave 4
  out.playNote( 0.00, 0.1, PitchNameInstrument( "Fa0x", vol ) )
  
  out.playNote( 0.25, 0.1, PitchNameInstrument( "Fa", vol ) )
  out.playNote( 0.75, 0.1, PitchNameInstrument( "Fa", vol ) )
  out.playNote( 1.25, 0.1, PitchNameInstrument( "Fa0x", vol ) )
  out.playNote( 1.50, 0.1, PitchNameInstrument( "Fa", vol ) )
  out.playNote( 2.00, 0.1, PitchNameInstrument( "Si", vol ) )
  out.playNote( 2.75, 0.1, PitchNameInstrument( "Sol", vol ) )
  
  out.playNote( 0.00, 0.15, PitchNameInstrument( "Re 3", vol ) )

  out.playNote( 0.25, 0.15, PitchNameInstrument( "Re 3", vol ) )
  out.playNote( 0.75, 0.15, PitchNameInstrument( "Re 3", vol ) )
  out.playNote( 1.25, 0.15, PitchNameInstrument( "Re 3", vol ) )
  out.playNote( 1.50, 0.15, PitchNameInstrument( "Re 3", vol ) )
  # an empty note has the default pitch of C4 (Sol 4).
  out.playNote( 2.00, 0.15, PitchNameInstrument( "", vol ) )
  out.playNote( 2.75, 0.15, PitchNameInstrument( "Sol 3", vol ) )
  
  # a section of notes just for testing
  out.setNoteOffset( 6.5 )
  out.playNote( 0.00, 0.2, PitchNameInstrument( "La-1", vol ) )
  out.playNote( 0.25, 0.2, PitchNameInstrument( "La0x0", vol ) )
  out.playNote( 0.50, 0.2, PitchNameInstrument( "La0x0x1", vol ) )
  out.playNote( 0.75, 0.2, PitchNameInstrument( "La 2", vol ) )
  out.playNote( 1.00, 0.2, PitchNameInstrument( "La 3", vol ) )
  out.playNote( 1.25, 0.2, PitchNameInstrument( "La 4", vol ) )
  out.playNote( 1.50, 0.2, PitchNameInstrument( "La 5", vol ) )
  out.playNote( 1.75, 0.2, PitchNameInstrument( "La 6", vol ) )
  out.playNote( 2.00, 0.2, PitchNameInstrument( "La 7", vol ) )
  out.playNote( 2.25, 0.2, PitchNameInstrument( "La 8", vol ) )
  out.playNote( 2.50, 0.2, PitchNameInstrument( "La 9", vol ) )
  out.playNote( 2.75, 0.2, PitchNameInstrument( "La 10", vol ) )
  out.playNote( 3.00, 0.2, PitchNameInstrument( "La 11", vol ) )
  out.playNote( 3.25, 0.2, PitchNameInstrument( "La 8", vol ) )
 
  # a few notes showing some weird cases.
  out.playNote( 4.00, 0.2, PitchNameInstrument( "C 4", vol ) )
  # extra spaces
  out.playNote( 4.25, 0.2, PitchNameInstrument( "Do ", vol ) )
  # nothing but a flat
  out.playNote( 4.50, 0.2, PitchNameInstrument( " b ", vol ) )
  # only an octave number 
  out.playNote( 4.75, 0.2, PitchNameInstrument( "  5", vol ) )
  # something that doen't even make sense
  out.playNote( 5.00, 0.2, PitchNameInstrument( " y ", vol ) )
  out.playNote( 5.25, 0.2, PitchNameInstrument( "Fa  ", vol ) )

  # finally, resume time after adding all of these notes at once.
  out.resumeNotes()
 

# draw is run many times
def draw()
{
  # erase the window to black
  background( 64, 64, 192 )
  # draw using a white stroke
  stroke( 64, 192, 64 )
  # draw the waveforms
  for( i = 0 i < out.bufferSize() - 1 i+=1 )
 :
    # find the x position of each buffer value
    x1  =  map( i, 0, out.bufferSize(), 0, width )
    x2  =  map( i+1, 0, out.bufferSize(), 0, width )
    # draw a line from one buffer position to the next for both channels
    line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50)
    line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50)
    


