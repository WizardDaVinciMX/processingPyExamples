""" multipleOutputsExample
   <p>
   this is an example of how a single UGen can be patched to multiple things
   in order to control them simultaneously.
   <p>
   For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
   <p>   
   author: Damien Di Fede, Anderson Mills<br/>
   Anderson Mills's work was supported by numediart (www.numediart.org) 
"""

add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput out
WobbleInstrument myWobble

def setup()
{
  # initialize the drawing window
  size( 512, 200, P2D )

  # initialize the minim and out objects
  minim = Minim( this )
  out = minim.getLineOut( Minim.MONO )

  out.playNote(0.5, 6.1, WobbleInstrument( 330f, 0.3, 1.0, out) )


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
    

