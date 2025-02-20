"""
  This sketch demonstrates how to use the <code>printControls</code> method of a <code>Controller</code> object. 
  The class used here is an <code>AudioOutput</code> but you can also prthe controls of <code>AudioSample</code>, 
  <code>AudioSnippet</code>, <code>AudioInput</code>, and <code>AudioPlayer</code> objects. <code>printControls</code> 
  will prout all the available controls (such as volume, gain, etc) and their ranges to the console.
  If you are running this sketch in a web browser you will have to open the Java console to see the printout. <br />
"""

add_library("minim")

minim = None
out = None

def setup():
  global minim
  global out

  size(512, 200)
  minim = Minim(this)
  out = minim.getLineOut()
  out.printControls()


def draw():
  background(0)
