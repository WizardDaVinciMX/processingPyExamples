"""
  This sketch demonstrates how to use the cue method of AudioPlayer. 
  When you cue, it is always measured from the beginning of the recording. 
  So cue(100) will set the "playhead" at 100 milliseconds from the beginning 
  no matter where it currently is. Cueing an AudioPlayer will not change the playstate, 
  meaning that if it was already playing it will continue playing from the cue point, 
  but if it was not playing, cueing will not start playback, it will simply set the po
  at which playback will begin. If an error occurs while trying to cue, the position will not change. 
  If you try to cue to a negative position or try to cue past the end of the 
  recording, the amount will be clamped to zero or length(). 

  Click in the window to cue to that position in the file.
"""

add_library("minim")

minim = None
groove = None

def setup():
  global minim
  global groove

  size(512, 200, P3D)
  
  minim = Minim(this)
  groove = minim.loadFile("groove.mp3")
  groove.loop()


def draw():
  background(0)
  stroke( 255 )
  
  for i in range(0, groove.bufferSize() - 1):
    line(i, 50  + groove.left.get(i)*50,  i+1, 50  + groove.left.get(i+1)*50)
    line(i, 150 + groove.right.get(i)*50, i+1, 150 + groove.right.get(i+1)*50)
  
  stroke( 255, 0, 0 )
  position = map( groove.position(), 0, groove.length(), 0, width )
  line( position, 0, position, height )
  
  text("Click anywhere to jump to a position in the song.", 10, 20)

def mousePressed():
  global groove

  # choose a position to cue to based on where the user clicked.
  # the length() method returns the length of recording in milliseconds.
  position = int( map( mouseX, 0, width, 0, groove.length() ) )
  groove.cue( position )
