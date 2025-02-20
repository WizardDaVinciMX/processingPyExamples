"""*
  This is an example of using a Multiplier UGen, which performs the very simple operation of 
  multiplying the incoming signal by the current value of its amplitude input.
  <p>
  Move the mouse left and right to change the value of the Multiplier. 
  All the way left is 0.1 and all the way right is 1.
  <p>
  For more information about Minim and additional features,<br/>
  visit http:#code.compartmental.net/minim/
  <p>
  author: Damien Di Fede
"""

add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

Minim         minim
AudioOutput   out
Oscil         osc
Multiplier    multiplier

def setup()
{
  # setup the size of the app
  size(640, 200)
  
  # create our Minim object for loading audio
  minim = Minim(this)
  
  # get a line out from Minim. It's important that the file is the same audio format 
  # as our output (i.e. same sample rate, number of channels, etc).
  out = minim.getLineOut()
  
  osc = Oscil( 440, 1 )
  multiplier = Multiplier( 0.5f )
  
  # normally we wouldn't use a multiplier with an Oscil like this
  # because we could simply set the amplitude of the Oscil itself.
  osc.patch( multiplier ).patch( out )
                        


# draw is run many times
def draw()
{
  # map the mouse position to a value for the multiplier
  value = map(mouseX, 0, width, 0.1, 1)
  
  # set the value.
  # this is equivalent to multiplier.amplitude.setLastValue( value )
  # you'll also notice this causes audible clicks if you move the mouse quickly
  # to keep that from happening, you will usually want to use a Line patched 
  # to the Multiplier's amplitude input.
  multiplier.setValue( value )
  
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
    


