add_library("themidibus") #Import the library
add_library("sound")
#add_library("MidiMessage") #javax.sound.midi.MidiMessage #Import the MidiMessage classes http:#java.sun.com/j2se/1.5.0/docs/api/javax/sound/midi/MidiMessage.html
#add_library("SysexMessage") #javax.sound.midi.SysexMessage
#add_library("ShortMessage") #javax.sound.midi.ShortMessage

def setup():
  global myBus # The MidiBus
  size(400, 400)
  background(0)

  MidiBus.list() # List all available Midi devices on STDOUT. This will show each device's index and name.
  myBus = MidiBus(this, 0, 0) # Create a MidiBus object

  # On mac you will need to use MMJ since Apple's MIDI subsystem doesn't properly support SysEx. 
  # However MMJ doesn't support sending timestamps so you have to turn off timestamps.
  # myBus.sendTimestamps(false)


def draw():
  channel = 1
  pitch = 64
  velocity = 127

  myBus.sendNoteOn(channel, pitch, velocity) # Send a Midi noteOn
  delay(200)
  myBus.sendNoteOff(channel, pitch, velocity) # Send a Midi nodeOff
  delay(100)

  #Or for something different we could send a custom Midi message ...

  status_byte = 0xa0 # For instance let us send aftertouch
  channel_byte = 0 # On channel 0 again
  first_byte = 64 # The same note
  second_byte = 80 # But with less velocity

  myBus.sendMessage(status_byte, channel_byte, first_byte, second_byte)

  #Or we could even send a variable length sysex message
  #IMPORTANT: On mac you will have to use the MMJ MIDI subsystem to be able to send SysexMessages. Consult README.md for more information

#  myBus.sendMessage( [0xf0, 0x01, 0x02, 0x03, 0x04, 0xf7] )
  
  #We could also do the same thing this way ...

  try: #All the methods of SysexMessage, ShortMessage, etc, require try catch blocks
    message = SysexMessage()
    message.setMessage(
      0xf0,
      [0x05, 0x06, 0x07, 0x08, 0xf7], 5
    )
    myBus.sendMessage(message)
  except:
    println("No se pudo enviar el mensaje MIDI")

  delay(2000)


# Notice all bytes below are converted to integeres using the following system:
# i = (int)(byte & x0FF) 
# This properly convertes an unsigned byte (MIDI uses unsigned bytes) to a signed int
# Because java only supports signed bytes, you will get incorrect values if you don't do so

def rawMidi(data): # You can also use rawMidi(byte[] data, String bus_name)
  # Receive some raw data
  # data[0] will be the status byte
  # data[1] and data[2] will contain the parameter of the message (e.g. pitch and volume for noteOn noteOff)
  println()
  println("Raw Midi Data:")
  println("--------")
  println("Status Byte/MIDI Command:"+(int)(data[0] & x0FF))
  # N.B. In some cases (noteOn, noteOff, controllerChange, etc) the first half of the status byte is the command and the second half if the channel
  # In these cases (data[0] & x0F0) gives you the command and (data[0] & x00F) gives you the channel
  for i in range(1, data.length):
    println("Param "+(i+1)+": " + (data[i] & x0FF))


def midiMessage(message): # You can also use midiMessage(MidiMessage message, long timestamp, String bus_name)
  # Receive a MidiMessage
  # MidiMessage is an abstract class, the actual passed object will be either javax.sound.midi.MetaMessage, javax.sound.midi.ShortMessage, javax.sound.midi.SysexMessage.
  # Check it out here http:#java.sun.com/j2se/1.5.0/docs/api/javax/sound/midi/package-summary.html
  println()
  println("MidiMessage Data:")
  println("--------")
  println("Status Byte/MIDI Command:"+message.getStatus())
  for i in range(1, len(message.getMessage())):
    println("Param "+(i+1)+": "+ (message.getMessage()[i] & 0xff))
  
def delay(time):
  current = millis()
  while millis () < current+time:
    yield  #Thread.yield()
