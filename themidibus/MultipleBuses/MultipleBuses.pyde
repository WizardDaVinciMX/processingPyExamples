add_library("themidibus") #Import the library

def setup():
  global busA #The first MidiBus
  global busB #The second MidiBus
  size(400, 400)
  background(0)

  MidiBus.list() #List all available Midi devices. This will show each device's index and name.

  #This is a different way of listing the available Midi devices.
  println("")
  println("Available MIDI Devices:") 

  println("----------Input (from availableInputs())----------")
  available_inputs = MidiBus.availableInputs() #Returns an array of available input devices
  for i in range( 0, len(available_inputs)):
    println("[" + str(i) + "] \"" + str(available_inputs[i]) + "\"")

  println("----------Output (from availableOutputs())----------")
  available_outputs = MidiBus.availableOutputs() #Returns an array of available output devices
  for i in range(0, len(available_outputs)):
    println("[" + str(i) + "] \"" + str(available_outputs[i]) + "\"")

  println("----------Unavailable (from unavailableDevices())----------")
  unavailable = MidiBus.unavailableDevices() #Returns an array of unavailable devices
  for i in range(0, len(unavailable)):
    println("[" + str(i) + "] \"" + str(unavailable[i]) + "\"")

  busA = MidiBus(this, "IncomingA", "OutgoingA", "busA") #Create a first MidiBus attached to the IncommingA Midi input device and the OutgoingA Midi output device. We will name it busA.
  busB = MidiBus(this, "IncomingB", "OutgoingB", "busB") #Create a second MidiBus attached to the IncommingB Midi input device and the OutgoingB Midi output device. We will name it busB.

  busA.addOutput("OutgoingC") #Add a output device to busA called OutgoingC
  busB.addInput("IncomingC") #Add a input device to busB called IncommingC

  #It is also possible to check what devices are currently attached as inputs or outputs on a bus

  println("")
  println("Inputs on busA")
  println(busA.attachedInputs()) #Prthe devices attached as inputs to busA
  println("")
  println("Outputs on busB")
  println(busB.attachedOutputs()) #Prints the devices attached as outpus to busB


def draw():
  channel = 0
  pitch = 64
  velocity = 127

  busA.sendNoteOn(channel, pitch, velocity) #Send a noteOn to OutgoingA and OutgoingC through busA
  delay(200)
  busB.sendNoteOn(channel, pitch, velocity) #Send a noteOn to OutgoingB through busB
  delay(100)
  busA.sendNoteOff(channel, pitch, velocity) #Send a noteOff to OutgoingA and OutgoingC through busA
  busB.sendNoteOff(channel, pitch, velocity) #Send a noteOff to OutgoingB through busB

  number = 0
  value = 90

  busA.sendControllerChange(channel, number, value) #Send a controllerChange to OutgoingA and OutgoingC through busA
  busB.sendControllerChange(channel, number+10, value+10) #Send a controllerChange to OutgoingB through busB
  delay(2000)

def noteOn(channel, pitch, velocity, timestamp, bus_name):
  println()
  println("Note On:")
  println("--------")
  println("Channel:"+channel)
  println("Pitch:"+pitch)
  println("Velocity:"+velocity)
  println("Timestamp:"+timestamp)
  println("Recieved on Bus:"+bus_name)
  if   bus_name == "busA":
    println("This came from IncomingA")
  elif bus_name == "busB":
    println("This came from IncomingB or IncomingC")


def noteOff(channel, pitch, velocity, timestamp, bus_name):
  println()
  println("Note Off:")
  println("--------")
  println("Channel:"+channel)
  println("Pitch:"+pitch)
  println("Velocity:"+velocity)
  println("Timestamp:"+timestamp)
  println("Recieved on Bus:"+bus_name)
  if   bus_name == "busA":
    println("This came from IncomingA")
  elif bus_name == "busB":
    println("This came from IncomingB or IncomingC")


def controllerChange(channel, number, value, timestamp, bus_name):
  println()
  println("Controller Change:")
  println("--------")
  println("Channel:"+channel)
  println("Number:"+number)
  println("Value:"+value)
  println("Timestamp:"+timestamp)
  println("Recieved on Bus:"+bus_name)
  if bus_name == "busA":
    println("This came from IncomingA")
  elif bus_name == "busB":
    println("This came from IncomingB or IncomingC")

def delay(time):
  current = millis()
  while millis () < current + time:
    yield
