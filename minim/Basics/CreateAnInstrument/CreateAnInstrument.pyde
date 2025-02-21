"""*
  * This sketch demonstrates how to create synthesized sound with Minim using an AudioOutput and
  * an Instrument we define. By using the playNote method you can schedule notes to played 
  * at some poin the future, essentially allowing to you create musical scores with code. 
  * Because they are constructed with code, they can be either deterministic or different every time. 
  * This sketch creates a deterministic score, meaning it is the same every time you run the sketch.
  * <p>
  * For more complex examples of using playNote check out algorithmicCompExample and compositionExample
  * in the Synthesis folder.
  * <p>
  * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput out

# to make an Instrument we must define a class
# that implements the Instrument interface.
class SineInstrument implements Instrument
{
  Oscil wave
  Line  ampEnv
  
  SineInstrument( frequency )
 :
    # make a sine wave oscillator
    # the amplitude is zero because 
    # we are going to patch a Line to it anyway
    wave   = Oscil( frequency, 0, Waves.SINE )
    ampEnv = Line()
    ampEnv.patch( wave.amplitude )
  
  
  # this is called by the sequencer when this instrument
  # should start making sound. the duration is expressed in seconds.
  def noteOn( duration )
 :
    # start the amplitude envelope
    ampEnv.activate( duration, 0.5f, 0 )
    # attach the oscil to the output so it makes sound
    wave.patch( out )
  
  
  # this is called by the sequencer when the instrument should
  # stop making sound
  def noteOff()
 :
    wave.unpatch( out )
  


def setup()
{
  size(512, 200, P3D)
  
  minim = Minim(this)
  
  # use the getLineOut method of the Minim object to get an AudioOutput object
  out = minim.getLineOut()
  
  # when providing an Instrument, we always specify start time and duration
  out.playNote( 0.0, 0.9, SineInstrument( 97.99 ) )
  out.playNote( 1.0, 0.9, SineInstrument( 123.47 ) )
  
  # we can use the Frequency class to create frequencies from pitch names
  out.playNote( 2.0, 2.9, SineInstrument( Frequency.ofPitch( "C3" ).asHz() ) )
  out.playNote( 3.0, 1.9, SineInstrument( Frequency.ofPitch( "E3" ).asHz() ) )
  out.playNote( 4.0, 0.9, SineInstrument( Frequency.ofPitch( "G3" ).asHz() ) )


def draw()
{
  background(0)
  stroke(255)
  
  # draw the waveforms
  for(i = 0 i < out.bufferSize() - 1 i+=1)
 :
    line( i, 50 + out.left.get(i)*50, i+1, 50 + out.left.get(i+1)*50 )
    line( i, 150 + out.right.get(i)*50, i+1, 150 + out.right.get(i+1)*50 )
  

