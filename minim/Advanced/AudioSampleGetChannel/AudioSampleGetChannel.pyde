"""
  This sketch demonstrates how to get a channel of audio from an AudioSample 
  and then manipulate it to change the AudioSample after it has been loaded. 
  <p>
  For more information about Minim and additional features, 
  visit http:#code.compartmental.net/minim/
"""

add_library("minim")

minim = None
jingle = None

# Función de apoyo, para sustituir System.arraycopy() de Java
# FUENTE: https://stackoverflow.com/questions/20253391/does-python-have-anything-like-javas-system-arraycopy
def arrayCopy(src, srcPos, dest, destPos, length):
    for i in range(length):
        dest[i + destPos] = src[i + srcPos]

def setup():
  global jingle

  size(512, 200, P3D)

  minim = Minim(this)
  
  jingle = minim.loadSample("jingle.mp3", 2048)
  # get the left channel of the audio as a array
  # getChannel expects either AudioSample.LEFT or AudioSample.RIGHT as an argument
  leftChannel = jingle.getChannel(AudioSample.LEFT)
  # now we are just going to reverse the left channel
  reversed = reverse(leftChannel)
  arrayCopy(reversed, 0, leftChannel, 0, len(leftChannel))

def draw():
  global jingle

  background(0)
  stroke(255)
  for i in range(0, jingle.bufferSize() - 1):
    line(i, 50 - jingle.left.get(i)*50, i+1, 50 - jingle.left.get(i+1)*50)
    line(i, 150 - jingle.right.get(i)*50, i+1, 150 - jingle.right.get(i+1)*50)

  text("Press any key to trigger the sample.", 10, 20)

def keyPressed():
  jingle.trigger()
