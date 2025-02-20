"""
    This example demonstrates how you might use JavaSound's midi file playing
    abilities to drive UGens in Minim for synthesis, rather than using the 
    midi sounds built into JavaSound. You might want to take this 
    approach if you want to tightly couple visuals and music, like this example does,
    but don't want to hand-code your sequence using AudioOutput's playNote method,
    or if you want to synthesize a midi file you've already created with custom
    synthesis chains and effects.
    <p>
    This is a simple example, as far as it goes, and ignores NoteOff midi messages. To handle NoteOff 
    messages, you would need to conceive of some kind of system for pairing NoteOn messages with 
    NoteOff messages so that your Instrument instances (or whatever classes you write to respond
    to midi messages) behave properly.
    <p>
    For more info about what can be done with the JavaSound Sequencer and Sequence classes, see:
    <a href="http:#docs.oracle.com/javase/6/docs/api/javax/sound/midi/Sequence.html">javax.sound.midi.Sequence</a> and 
    <a href="http:#docs.oracle.com/javase/6/docs/api/javax/sound/midi/Sequencer.html">javax.sound.midi.Sequencer</a>
    <p>
    For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
    <p>
    Author: Damien Di Fede  
"""
add_library("minim")
#add_library("ddf.minim.ugens.*

from javax.sound.midi import Receiver
from javax.sound.midi import MidiUnavailableException
from javax.sound.midi import InvalidMidiDataException
from javax.sound.midi import Sequencer
from javax.sound.midi import MidiSystem, Synthesizer, MidiUnavailableException
from javax.sound.midi import Transmitter, MidiMessage, ShortMessage

from java.io import IOException

# this package is where we get our midi objects from
#add_library("javax.sound.midi.*

# two things we need from Minim synthesis
minim = None
out = None

# what we need from JavaSound for sequence playback
sequencer = None
# holds the actual midi data
sequence = None

# the Blip class is what handles our visuals.
# see below the draw function for the definition.
blips = None

# in order to be send midi messages from the Sequencer
# we must implement the JavaSound interface Receiver.
# we then set an instance of this class as the Receiver
# for on of the Sequencer's Trasmitters.
# See: http:#docs.oracle.com/javase/6/docs/api/javax/sound/midi/Receiver.html
class MidiReceiver(Receiver):
  def close(self):
      println("Closing the receiver")

  def send(self, msg, timeStamp ):
    global out
    # we only care about NoteOn midi messages.
    # here's how you check for that
    if isinstance(msg, ShortMessage):
      # if you want to handle messages other than NOTE_ON, you can refer to the constants defined in 
      # ShortMessage: http:#docs.oracle.com/javase/6/docs/api/javax/sound/midi/ShortMessage.html
      # And figure out what Data1 and Data2 will be, refer to the midi spec: http:#www.midi.org/techspecs/midimessages.php
      c = msg.getCommand()
      if c == ShortMessage.NOTE_ON:
        # note number, between 1 and 127
        note = msg.getData1()
        # velocity, between 1 and 127
        vel  = msg.getData2()
        # we could also use sm.getChannel() to do something different depending on the channel of the message
        # see below the draw method for the definition of this sound generating Instrument
        out.playNote( 0, 0.1, Synth( note, vel ) ) 

def setup():
  global minim
  global out
  global blips

  size( 640, 480 )
  
  minim = Minim(this)
  out   = minim.getLineOut()
  
  # try to get the default sequencer from JavaSound
  # if it fails, we pra message to the console
  # and don't do any of the sequencing.
  try:
    # get a disconnected sequencer. this should prevent
    # us from hearing the general midi sounds the 
    # sequecer is automatically hooked up to.
    sequencer = MidiSystem.getSequencer( False )

    # have to open it
    sequencer.open()
    
    # load our sequence
    sequence  = MidiSystem.getSequence( createInput( "bassline.MID" ) )

    # put it in the sequencer
    sequencer.setSequence( sequence )
    
    # set the tempo
    sequencer.setTempoInBPM( 128 )
    
    # hook up an instance of our Receiver to the Sequencer's Transmitter
    sequencer.getTransmitter().setReceiver( MidiReceiver() )

    # just keep looping
    sequencer.setLoopCount( Sequencer.LOOP_CONTINUOUSLY )
    
    # and away we go
    sequencer.start()

  except MidiUnavailableException: # getSequencer can throw this
    # oops there wasn't one.
    println( "No default sequencer, sorry bud." )
  
  except InvalidMidiDataException: # getSequence can throw this
    # oops, the file was bad
    println( "The midi file was hosed or not a midi file, sorry bud." )
  
  except IOException: # getSequence can throw this
    println( "Had a problem accessing the midi file, sorry bud." )

  # and we need to make our Blip list
  blips = list()
  # and set our drawing preferences
  rectMode( CENTER )

def draw():
  global blips

  background( 20 )

  # just draw all the Blips!
  for blip in blips:
    blip.draw()  

# the Instrument implementation we use for playing notes
# we have to explicitly specify the Instrument interface
# from Minim because there is also an Instrument interface
# in javax.sound.midi. We could adef this by importing
# only the classes we need from javax.sound.midi, 
# rather than importing everything.
class Synth(Instrument):
  def __init__(self, note, velocity ):
    self.noteNumber = note
    self.freq = Frequency.ofMidiNote( noteNumber ).asHz()
    self.amp  = (velocity-1) / 126.0
    
    self.wave = Oscil( freq, amp, Waves.QUARTERPULSE )
    # Damp arguments are: attack time, damp time, and max amplitude
    self.env  = Damp( 0.001, 0.1, 1.0 )
    
    self.wave.patch( env )


  def noteOn(self, dur ):

    # make visual
    c = color( 0, 200, 64, 255*(wave.amplitude.getLastValue()) )
    blip = Blip( c, map(noteNumber, 30, 55, height, 0), 200 )
    blips.append( blip )
    
    # make sound
    env.activate()
    env.patch( out )

  def noteOff(self):
    env.unpatchAfterDamp( out )
    blips.remove( blip )

# this class stores data for drawing one Blip on the screen.
# in this example, each Blip directly corresponds to a note
# played in the musical sequence. the pitch of the note
# is represented by the vertical position of the Blip on the screen,
# the velocity is represented by the opacity of the Blip,
# and the duration is represented by the width.
# The color is used to differentiate between the two
# midi instruments being used in the example.
class Blip:
  def __init__(self, c, p, s ):
    self.shade = c
    self.position = p
    self.size = s

  def draw(self):
    fill( shade )
    rect( width/2, position, size, 10 )
