# This class is a very simple implementation of AudioListener. By implementing this interface, 
# you can add instances of this class to any class in Minim that implements Recordable and receive
# buffers of samples in a callback fashion. In other words, every time that a Recordable object has 
# a buffer of samples, it will send a copy to all of its AudioListeners. You can add an instance of 
# an AudioListener to a Recordable by using the addListener method of the Recordable. If you want to 
# remove a listener that you previously added, you call the removeListener method of Recordable, passing 
# the listener you want to remove.
#
# Although possible, it is not advised that you add the same listener to more than one Recordable. 
# Your listener will be called any time any of the Recordables you've added it have samples. This 
# means that the stream of samples the listener sees will likely be interleaved buffers of samples from 
# all of the Recordables it is listening to, which is probably not what you want.
#
# You'll notice that the three methods of this class are synchronized. This is because the samples methods 
# will be called from a different thread than the one instances of this class will be created in. That thread 
# might try to send samples to an instance of this class while the instance is in the middle of drawing the 
# waveform, which would result in a waveform made up of samples from two different buffers. Synchronizing 
# all the methods means that while the main thread of execution is inside draw, the thread that calls 
# samples will block until draw is complete. Likewise, a call to draw will block if the sample thread is inside 
# one of the samples methods. Hope that's not too confusing!

add_library("minim")
from ddf.minim import Minim, AudioListener

class WaveformRenderer(AudioListener):

  def __init__(self):
    self.left = list()
    self.right = list()

  def samples(self, samp):
    self.left = samp
  
  def samples(self, sampL, sampR):
    self.left = sampL
    self.right = sampR

  def draw(self):
    # we've got a stereo signal if right is not null
    if self.left != None and self.right != None:
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
      for i in range(0, len(left)):
        vertex(i, height/2 + left[i]*50)
      endShape()
