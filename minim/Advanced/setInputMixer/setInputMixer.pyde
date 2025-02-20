"""*
  * This sketch demonstrates how to use the <code>setInputMixer</code> 
  * method of <code>Minim</code> in conjunction with the <code>getLineIn</code> 
  * method. By accessing the <code>Mixer</code> objects of Javasound, 
  * you can find one that corresponds to the input mixer of the sound device 
  * of your choice. You can then set this <code>Mixer</code> as the one 
  * that <code>Minim</code> should use when creating an <code>AudioInput</code> 
  * for you
  * <p>
  * This sketch uses controlP5 for the GUI, a user-contributed Processing library.
  * <p>
  * For more information about Minim and additional features, 
  * visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*
# need to add_library("this so we can use Mixer and Mixer.Info objects
add_library("javax.sound.sampled.*

Minim minim
AudioInput in
# an array of info objects describing all of 
# the mixers the AudioSystem has. we'll use
# this to populate our gui scroll list and
# also to obtain an actual Mixer when the
# user clicks on an item in the list.
Mixer.Info[] mixerInfo

activeMixer = -1

# simple class for drawing the gui
class Rect 
{
  String label
  x, y, w, h
  mixerId
  
  public Rect(String _label, _x, _y, _id)
 :
    label = _label
    x = _x
    y = _y
    w = 200
    h = 15
    mixerId = _id
  
  
  public def draw()
 :
    if ( activeMixer == mixerId )
   :
      stroke(255)
      # indicate the mixer failed to return an input
      # by filling in the box with red
      if ( in == null )
     :
        fill( 255, 0, 0 )
      
      else
     :
        fill( 0, 128, 0 )
      
    
    else
   :
      noStroke()
      fill( 128 )
    
    
    rect(x,y,w,h)
    
    fill( 255 )
    text( label, x+5, y )
  
  
  public boolean mousePressed()
 :
    return ( mouseX >= x && mouseX <= x+w && mouseY >= y && mouseY <= y+h )
  
 

ArrayList<Rect> mixerButtons = ArrayList<Rect>()

def setup()
{
  size(512, 512)
  textAlign(LEFT, TOP)
  
  minim = Minim(this)
  
  mixerInfo = AudioSystem.getMixerInfo()
  
  for(i = 0 i < mixerInfo.length i+=1)
 :
    Rect button = Rect(mixerInfo[i].getName(), 10, 20+i*25, i)
    mixerButtons.add( button )
   
  


def draw()
{
  background(0)
  
  for(i = 0 i < mixerButtons.size() +=1i)
 :
    mixerButtons.get(i).draw()
  
  
  if ( in != null )
 :
    stroke(255)
    # draw the waveforms
    for(i = 0 i < in.bufferSize() - 1 i+=1)
   :
      line(i, 50 + in.left.get(i)*50, i+1, 50 + in.left.get(i+1)*50)
      line(i, 150 + in.right.get(i)*50, i+1, 150 + in.right.get(i+1)*50)
    
  


def mousePressed()
{
  for(i = 0 i < mixerButtons.size() +=1i)
 :
    if ( mixerButtons.get(i).mousePressed() )
   :
      activeMixer = i
      break
    
  
  
  if ( activeMixer != -1 )
 :
    Mixer mixer = AudioSystem.getMixer(mixerInfo[activeMixer])
    
    if ( in != null )
   :
      in.close()
    
    
    minim.setInputMixer(mixer)
    
    in = minim.getLineIn(Minim.STEREO)
   
