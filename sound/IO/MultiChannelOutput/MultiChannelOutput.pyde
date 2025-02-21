add_library("sound")

initialised = 0

def setup() :
  global sines
  global initialised
  global frequency

  size(640, 360)
  background(255)

  # some multi-channel USB audio interfaces don't show the correct number of 
  # output channels using the default audio drivers on Windows. If this is the 
  # case, try loading PortAudio support at the very top of your sketch with the 
  # following command (see the LowLevelEngine example for details):
#  MultiChannel.usePortAudio()

  foundMultiChannel = False
  deviceNames = Sound.list()
  for i in range(0, len(deviceNames)):
    if MultiChannel.availableChannels(i) > 2:
      println("Found a multi-channel device: " + deviceNames[i])
      Sound.outputDevice(i)
      foundMultiChannel = True
      break
    
  
  if not foundMultiChannel:
    println("Did not find any output devices with more than 2 channels!")
  
  
  println("Playing back different sine waves on the " + str(MultiChannel.availableChannels()) + " different channels")

  sines = [SinOsc(this)] * MultiChannel.availableChannels()
  initialised = 0
  frequency = 100
  
  textSize(128)
  fill(0)
  textAlign(CENTER)


def draw() :
  global initialised
  global sines
  global frequency

  # loop through all channels and start one sine wave on each
  if initialised < len(sines):
    # add a nice theatrical break
    delay(1000)

    background(255)
    text(str(initialised + 1) + " of " + str(len(sines)), width/2, height/2)

    MultiChannel.activeChannel(initialised)
    # create and start the sine oscillator.
    sines[initialised] = SinOsc(this)
    sines[initialised].freq(frequency)
    sines[initialised].play()

    # increase frequency on the next channel by one semitone
    frequency = frequency * 1.05946
    initialised = initialised + 1
    pass

  # as long as the oscillators are not stopped they will 'stick'
  # to the channel that they were originally added to, and we can
  # change their parameters freely
  frequency = map(mouseX, 0, width, 80.0, 1000.0)
  
  for sin in sines:
    sin.freq(frequency)
    
    # increase frequency on the next channel by one semitone (a factor of 2^(1/12))
    frequency = frequency * 1.05946
  
