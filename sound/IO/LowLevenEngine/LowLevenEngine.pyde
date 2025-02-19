add_library("sound")

#add_library("com.jsyn.engine.SynthesisEngine
# add_library("SynthesisEngine")
#add_library("com.jsyn.unitgen.ChannelOut
#add_library("ChannelOut")

def setup():

  # praudio device information to the console
  Sound.list()

  # to improve support for USB audio interfaces on Windows, it is possible to 
  # use the PortAudio bindings, which are however not enabled by default. The 
  # listing above might therefore not have given accurate input/output channel 
  # numbers. The Sound library automatically loads PortAudio drivers when it 
  # determines that it is unable to use a device correctly with the default 
  # drivers, but you can always force loading PortAudio (on both Windows and 
  # Mac) using MultiChannel.usePortAudio():
  if MultiChannel.usePortAudio():
    # if PortAudio was loaded successfully, the id's and names of the sound 
    # devices (and possibly their number of input/output channels) will have 
    # changed!
    Sound.list()
  

  # the Sound.status() method prints some general information about the current 
  # memory and CPU usage of the library to the console
  Sound.status()

  # to get programmatic access to the same information (and more), you can get 
  # and inspect the JSyn Synthesizer class yourself:
  s = Sound.getSynthesisEngine()
  println("Current CPU usage: " + str(s.getUsage()))

  # with direct access to the SynthesisEngine, you can always create and add 
  # your own JSyn unit generator chains. if you want to connect them to audio 
  # output, you can connect them to the ChannelOut units automatically 
  # generated by the library:
  outputs = MultiChannel.outputs()

  # if you want to mess
  sin = SinOsc(this)
  circuit = sin.getUnitGenerator()



# sketches without a draw() method won't get updated in the loop, and synthesis 
# won't continue
def draw():
    pass


# a useful callback method when you are debugging a sound sketch
def mouseClicked() :
  Sound.status()
