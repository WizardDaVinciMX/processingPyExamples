"""* 
  * This sketch demonstrates how to use <code>setLoopPoints</code>
  * using an <code>AudioPlayer</code>. Left-click with the mouse
  * to set the start poof the loop and right-click to set the
  * end poof the loop. You will likely find
  * there to be a break during loops while the code seeks from the 
  * beginning of the file to the start of the loop. This seek time
  * can become quite noticable if you are using an mp3 file 
  * because it will need to decode as it seeks.
  """

add_library("ddf.minim.*

Minim minim
AudioPlayer snip

loopBegin
loopEnd

def setup()
{
  size(512, 200, P3D)
  minim = Minim(this)
  snip = minim.loadFile("groove.mp3")
  
  textFont(loadFont("ArialMT-14.vlw"))


def draw()
{
  background(0)
  fill(255)  
  text("Loop Count: " + snip.loopCount(), 5, 20)
  text("Looping: " + snip.isLooping(), 5, 40)
  text("Playing: " + snip.isPlaying(), 5, 60)
  p = snip.position()
  l = snip.length()
  text("Position: " + p, 5, 80)
  text("Length: " + l, 5, 100)
  x = map(p, 0, l, 0, width)
  stroke(255)
  line(x, height/2 - 50, x, height/2 + 50)
  lbx = map(loopBegin, 0, snip.length(), 0, width)
  lex = map(loopEnd, 0, snip.length(), 0, width)
  stroke(0, 255, 0)
  line(lbx, 0, lbx, height)
  stroke(255, 0, 0)
  line(lex, 0, lex, height)


def mousePressed()
{
  ms = (int)map(mouseX, 0, width, 0, snip.length())
  if ( mouseButton == RIGHT )
 :
    snip.setLoopPoints(loopBegin, ms)
    loopEnd = ms
  
  else
 :
    snip.setLoopPoints(ms, loopEnd)
    loopBegin = ms
  


def keyPressed()
{
  snip.loop(2)
