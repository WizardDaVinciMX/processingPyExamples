"""*
  * This sketch demonstrates how to patch more than one UGen
  * to a Summer. It works just like patching any other two 
  * UGens together, the difference being that a Summer 
  * can have more than one UGen patched to it and will 
  * output the sum of all signals, whereas most other UGens
  * allow only one input.
  * 
  * For many more examples of UGens included with Minim, 
  * have a look in the Synthesis folder of the Minim examples.
  * <p>
  * For more information about Minim and additional features, 
  * visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

Minim       minim
AudioOutput out

def setup()
{
  size(512, 200, P3D)
  
  minim = Minim(this)
  
  # use the getLineOut method of the Minim object to get an AudioOutput object
  out = minim.getLineOut()
  
  Summer sum = Summer()
  
  # create some Oscils to patch to the Summer
  Oscil wave = Oscil( Frequency.ofPitch("A4"), 0.3f, Waves.SINE )
  # patch the Oscil to the Summer
  wave.patch( sum )
  
  wave = Oscil( Frequency.ofPitch("C0x5"), 0.3f, Waves.SINE )
  wave.patch( sum )
  
  wave = Oscil( Frequency.ofPitch("E5"), 0.3f, Waves.SINE )
  wave.patch( sum )
  
  # and the Summer to the output and you should hear a major chord
  sum.patch( out )


def draw()
{
  background(0)
  stroke(255)
  strokeWeight(1)
  
  # draw the waveform of the output
  for(i = 0 i < out.bufferSize() - 1 i+=1)
 :
    line( i, 50  - out.left.get(i)*50,  i+1, 50  - out.left.get(i+1)*50 )
    line( i, 150 - out.right.get(i)*50, i+1, 150 - out.right.get(i+1)*50 )
  

