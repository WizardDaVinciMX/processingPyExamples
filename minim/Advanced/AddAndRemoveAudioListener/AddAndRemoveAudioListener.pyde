"""
  This sketch demonstrates how to implement an AudioListener and then add and remove it from one of Minim's 
  classes that support AudioListeners: AudioPlayer, AudioSample, AudioOutput, and AudioInput. 

  An AudioListener is an interface that you can implement in your own classes, which allows you to receive
  sample buffers from sound generating classes immediately after they are generated. This is particularly 
  useful when you are doing audio analysis because it ensures that you will only see each buffer of audio
  once. If instead you perform your analysis in the draw method of your sketch, you might get less than 
  perfect results because they audio samples may change while you are observing them. This happens because 
  the audio is generated in a different thread of execution than draw is called from.

  You can add an instance of an AudioListener to a sound generating object by using the addListener 
  method of the class. If you want to remove a listener that you previously added, you call the
  removeListener method, passing the listener you want to remove.

  Although possible, it is not advised that you add the same listener to more than one sound generating object. 
  Your listener will be called any time any of the objects you've added it to have samples. 
  This means that the stream of samples the listener sees will likely be interleaved buffers of samples from 
  all of the objects it is listening to, which is probably not what you want.
"""

add_library("minim")
from ddf.minim import Minim, AudioListener

minim = None
groove = None
waveform = None
listening = False

# You'll notice that the three methods of this class are synchronized. This is because the samples methods 
# will be called from a different thread than the one instances of this class will be created in. That thread 
# might try to send samples to an instance of this class while the instance is in the middle of drawing the 
# waveform, which would result in a waveform made up of samples from two different buffers. Synchronizing 
# all the methods means that while the main thread of execution is inside draw, the thread that calls 
# samples will block until draw is complete. Likewise, a call to draw will block if the sample thread is inside 
# one of the samples methods. Hope that's not too confusing!

class WaveformRenderer(AudioListener):
  def __init__(self):
    self. left = list()
    self.right = list()
  
  def WaveformRenderer(self):
    self.left = None
    self.right = None
  
  
  def samples(self, samp):
    left = samp
  
  
  def samples(self, sampL, sampR):
    self.left = sampL
    self.right = sampR
  
  
  def draw(self):
    # we've got a stereo signal if right or left are not null
    if self.left != None and self.right != None :
      noFill()
      stroke(255)
      beginShape()
      for i in range(0, len(self.left)):
        vertex(i, height/4 + self.left[i]*50)
      
      endShape()
      beginShape()
      for i in range(0, len(self.right)):
        vertex(i, 3*(height/4) + self.right[i]*50)
      
      endShape()
    
    elif self.left != None:
      noFill()
      stroke(255)
      beginShape()
      for i in range(0, len(self.left)):
        vertex(i, height/2 + left[i]*50)
      
      endShape()
    

def setup():
  global groove
  global waveform

  size(512, 200, P3D)
  
  minim = Minim(this)
  groove = minim.loadFile("groove.mp3", 512)
  groove.loop()
  waveform = WaveformRenderer()


def draw():
  global listening
  global waveform

  background(0)
  
  if listening:
    waveform.draw()
  
  if listening:
    text("Press space to remove the listener", 10, 20 )
  else:
    text("Press space to add the listener", 10, 20 )
  

def keyPressed():
  global listening
  global groove
  global waveform

  if key == ' ':
    if not listening:
      groove.addListener( waveform )
      listening = True
    else:
      groove.removeListener( waveform )
      listening = False
