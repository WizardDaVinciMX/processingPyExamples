"""
  This sketch demonstrates how to use the <code>createSample</code> method of <code>Minim</code>. 
  The <code>createSample</code> method allows you to create an <code>AudioSample</code> by provided 
  either one or two arrays, which are the sound you want be able to trigger. 
  <p>
  See the loadSample example for more information about <code>AudioSample</code>s.
  <p>
  Press 't' to trigger the sample.
  <p>
  For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
"""

add_library("minim")
#add_library("ddf.minim.ugens.*
# we must add_library("this package to create an AudioFormat object
from javax.sound.sampled import AudioFormat

minim = None
wave = None

def setup():
  global minim
  global wave

  size(512, 200, P3D)
  
  minim = Minim(this)
  
  # we'll make a MONO sample, but there is also a version
  # of createSample that you can pass two arrays to:
  # which will be used for the left and right channels
  # of a stereo sample.
  samples = [0.0]*1024*8
  
  waveFrequency  = 220.0
  waveSampleRate = 44100.0
  
  # generate the sample by using Waves.SINE
  lookUp = 0 
  lookUpStep = waveFrequency / waveSampleRate
  for i in range(0, len(samples)):
     samples[i] = Waves.SINE.value(lookUp)  
     lookUp = (lookUp + lookUpStep) % 1.0

  # when we create a sample we need to provide an AudioFormat so 
  # the sound will be played back correctly.
  format = AudioFormat( waveSampleRate, # sample rate
                                        16,    # sample size in bits
                                        1,     # channels
                                        True,  # signed
                                        True   # bigEndian
                                      )
                                      
  # finally, create the AudioSample
  wave = minim.createSample( samples, # the samples
                             format,  # the format
                             1024     # the output buffer size
                            )


def draw():
  global wave

  background(0)
  stroke(255)
  # use the mix buffer to draw the waveforms.
  for i in range(0, wave.bufferSize() - 1):
    line(i, 100 - wave.left.get(i)*50, i+1, 100 - wave.left.get(i+1)*50)

def keyPressed():
  if key == 't':
    wave.trigger()
