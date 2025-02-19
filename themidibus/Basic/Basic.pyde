add_library("themidibus") #Import the library

def setup():
  global myBus # The MidiBus

  size(400, 400)
  background(0)

  MidiBus.list() # List all available Midi devices on STDOUT. This will show each device's index and name.

  # Either you can
  #               Parent In Out
  #                 |    |  |
  #myBus = MidiBus(this, 0, 1) # Create a MidiBus using the device index to select the Midi input and output devices respectively.

  # or you can ...
  #                Parent         In                   Out
  #                  |            |                     |
  #myBus = MidiBus(this, "IncomingDeviceName", "OutgoingDeviceName") # Create a MidiBus using the device names to select the Midi input and output devices respectively.

  # or for testing you could ...
  #              Parent  In        Out
  #                |     |          |
  myBus = MidiBus(this, -1, "Gervill") # Create a MidiBus with no input device and the default Java Sound Synthesizer as the output device.


def draw():
  channel = 1
  pitch = 64
  velocity = 127

  myBus.sendNoteOn(channel, pitch, velocity) # Send a Midi noteOn
  delay(200)
  myBus.sendNoteOff(channel, pitch, velocity) # Send a Midi nodeOff

  number = 0
  value = 90

  myBus.sendControllerChange(channel, number, value) # Send a controllerChange
  delay(2000)


def noteOn(channel, pitch, velocity):
  # Receive a noteOn
  println()
  println("Note On:")
  println("--------")
  println("Channel:" + channel)
  println("Pitch:" + pitch)
  println("Velocity:" + velocity)


def noteOff(channel, pitch, velocity):
  # Receive a noteOff
  println()
  println("Note Off:")
  println("--------")
  println("Channel:" + channel)
  println("Pitch:" + pitch)
  println("Velocity:" + velocity)


def controllerChange(channel, number, value):
  # Receive a controllerChange
  println()
  println("Controller Change:")
  println("--------")
  println("Channel:" + channel)
  println("Number:" + number)
  println("Value:" + value)


def delay(time):
  current = millis()
  while millis () < current + time:
    yield
