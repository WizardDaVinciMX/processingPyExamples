"""*
  * This sketch demonstrates how to use the <code>pause</code> method of a <code>Playable</code> class. 
  * The class used here is <code>AudioPlayer</code>, but you can also pause an <code>AudioSnippet</code>.
  * Pausing a <code>Playable</code> causes it to cease playback but not change position, so that when you 
  * resume playback it will start from where you last paused it. Press 'p' to pause the player.
  *
  """

add_library("ddf.minim.*

Minim minim
AudioPlayer groove

def setup()
{
  size(512, 200, P3D)

  minim = Minim(this)
  groove = minim.loadFile("groove.mp3", 2048)
  groove.loop()


def draw()
{
  background(0)
  
  stroke(255)
  
  for(i = 0 i < groove.bufferSize() - 1 i+=1)
 :
    line(i, 50  + groove.left.get(i)*50,  i+1, 50  + groove.left.get(i+1)*50)
    line(i, 150 + groove.right.get(i)*50, i+1, 150 + groove.right.get(i+1)*50)
  


def keyPressed()
{
  if ( groove.isPlaying() )
 :
    groove.pause()
  
  else
 :
    # simply call loop again to resume playing from where it was paused
    groove.loop()
  
