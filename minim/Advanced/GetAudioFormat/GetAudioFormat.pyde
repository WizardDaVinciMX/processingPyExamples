"""
  This sketch demonstrates how to use the <code>getFormat</code> method of a <code>Recordable</code> class. 
  The class used here is <code>AudioOutput</code>, but you can also get the format of <code>AudioInput</code>, 
  <code>AudioPlayer</code>, and <code>AudioSample</code> objects. The <code>getFormat</code> method returns 
  an object of type <code>AudioFormat</code> which is a class defined in the JavaSound API. An <code>AudioFormat</code>
  is a container for information about an audio source, such as the framerate, encoding and so forth. The following 
  methods are available on an <code>AudioFormat</code> object and all are demonstrated in this sketch.

  <pre>
    getChannels()
      Obtains the number of channels.
       
    AudioFormat.Encoding getEncoding()
      Obtains the type of encoding for sounds in this format.
      
    getFrameRate()
      Obtains the frame rate in frames per second.

    getFrameSize()
      Obtains the frame size in bytes.
      
    getSampleRate()
      Obtains the sample rate.
      
    getSampleSizeInBits()
      Obtains the size of a sample.
      
    boolean isBigEndian()
      Indicates whether the audio data is stored in big-endian or little-endian byte order.

    boolean matches(AudioFormat format)
      Indicates whether this format matches the one specified.
      
    String toString()
      Returns a string that describes the format, such as: "PCM SIGNED 22050 Hz 16 bit mono big-endian".
    </pre>
"""

add_library("minim")

minim = None
out = None

def setup():
  global out
  size(760, 140, P3D)
  textFont(loadFont("CourierNewPSMT-12.vlw"))

  minim = Minim(this)
  # this should give us a stereo output with a 1024 sample buffer, 
  # a sample rate of 44100 and a bit depth of 16
  out = minim.getLineOut()

def draw():
  global out

  background(0)
  text("The output has " + str(out.getFormat().getChannels()) + " channels.", 5, 15)
  text("The output's encoding is " + str(out.getFormat().getEncoding()) + ".", 5, 30)
  text("The output's frame rate is " + str(out.getFormat().getFrameRate()) + " frames per second.", 5, 45)
  text("The output's frame size is " + str(out.getFormat().getFrameSize()) + " bytes.", 5, 60)
  text("The output's sample rate is " + str(out.getFormat().getSampleRate()) + " Hz.", 5, 75)
  text("The output's sample size is " + str(out.getFormat().getSampleSizeInBits()) + " bits.", 5, 90)
  if out.getFormat().isBigEndian():
    endianess = "big-endian"
  else:
    endianess = "little-endian"
  text("The output's byte order is " + endianess + ".", 5, 105)
  text("The output's format as a string is " + str(out.getFormat()), 5, 120)
