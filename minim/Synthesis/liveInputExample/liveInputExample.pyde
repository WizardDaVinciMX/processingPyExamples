""" liveInputExample<br/>
   is an example of using the LiveInput UGen to patch 
   the audio input from your computer (usually the microphone) to the output.
   <p>
   For more information about Minim and additional features, 
   visit http:#code.compartmental.net/minim/
   <p>
   author: Damien Di Fede
"""

add_library("ddf.minim.*
add_library("ddf.minim.ugens.*
add_library("ddf.minim.spi.* # for AudioStream

Minim minim
AudioOutput out
LiveInput in

def setup()
{
  # initialize the drawing window
  size(512, 200)
  
  # initialize the minim and out objects
  minim = Minim(this)
  out = minim.getLineOut()
  
  # we ask for an input with the same audio properties as the output.
  AudioStream inputStream = minim.getInputStream( out.getFormat().getChannels(), 
                                                  out.bufferSize(), 
                                                  out.sampleRate(), 
                                                  out.getFormat().getSampleSizeInBits())
                                                 
  # construct a LiveInput by giving it an InputStream from minim.                                                  
  in = LiveInput( inputStream )
  
  # create granulate UGen so we can hear the input being modfied before it goes to the output
  GranulateSteady grain = GranulateSteady()
  
  # patch the input through the grain effect to the output
  in.patch(grain).patch(out)


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
    

