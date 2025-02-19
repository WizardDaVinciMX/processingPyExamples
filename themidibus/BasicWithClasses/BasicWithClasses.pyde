add_library("themidibus") #Import the library

def setup():
  global myBus # The MidiBus
  size(400, 400)
  background(0)

  MidiBus.list() # List all available Midi devices on STDOUT. This will show each device's index and name.

  # Either you can
  #                   Parent In Out
  #                     |    |  |
  #myBus = MidiBus(this, 0, 1) # Create a MidiBus using the device index to select the Midi input and output devices respectively.

  # or you can ...
  #                   Parent         In                   Out
  #                     |            |                     |
  #myBus = MidiBus(this, "IncomingDeviceName", "OutgoingDeviceName") # Create a MidiBus using the device names to select the Midi input and output devices respectively.

  # or for testing you could ...
  #                 Parent  In        Out
  #                   |     |          |
  myBus = MidiBus(this, -1, "Real Time Synthetizer") # Create a MidiBus with no input device and the default Java Sound Synthesizer as the output device.

def draw():
  channel = 0
  pitch = 64
  velocity = 127
  note = Note(channel, pitch, velocity)

  myBus.sendNoteOn(note) # Send a Midi noteOn
  delay(200)
  myBus.sendNoteOff(note) # Send a Midi nodeOff

  number = 0
  value = 90
  change = ControlChange(channel, number, velocity)

  myBus.sendControllerChange(change) # Send a controllerChange
  delay(2000)

def noteOn(note):
  # Receive a noteOn
  println()
  println("Note On:")
  println("--------")
  println("Channel:" + note.channel())
  println("Pitch:" + note.pitch())
  println("Velocity:" + note.velocity())

def noteOff(note):
  # Receive a noteOff
  println()
  println("Note Off:")
  println("--------")
  println("Channel:" + note.channel())
  println("Pitch:" + note.pitch())
  println("Velocity:" + note.velocity())

def controllerChange(change):
  # Receive a controllerChange
  println()
  println("Controller Change:")
  println("--------")
  println("Channel:" + change.channel())
  println("Number:" + change.number())
  println("Value:" + change.value())


def delay(time):
  current = millis()
  while millis () < current+time:
    yield
