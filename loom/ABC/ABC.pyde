"""
 * ABC shows the use of the text-based ABC format for entering musical notation.
 *
 * You will need The MidiBus <https:#github.com/sparks/themidibus/> and a MIDI synthesizer
 * installed for this example. If you don't hear any sound, please consult the instructions at:
 * https:#corajr.github.io/loom/reference/com/corajr/loom/wrappers/MidiBusImpl.html#midi
 *
 * Note that the key defaults to C major if you want to specify a different key,
 * you can either provide just the key in the input string (e.g. "K:D\n ..."
 * or a complete ABC header. See http:#abcnotation.com/learn for a tutorial
 * on ABC notation.
"""

add_library("loom")
add_library("themidibus")
#add_library("com.corajr.loom.wrappers.*
#add_library("com.corajr.loom.util.*
#add_library("themidibus.*

def setup():
  global loom
  global pattern
  global myBus

  size(400, 400)

  # Initialize the Loom with a tempo of 120 BPM.
  loom = Loom(this, 120)

  # Creates the pattern from a string containing ABC notation.
  # If using C major, the header can be omitted.
  pattern = Pattern.fromABC(loom, "zCDEF3/2G/4F/4EA|DG3/2A/2G/2F/2E/2||")

  # List valid MIDI devices.
  # MidiBus.list()

  # Initialize the MIDI bus and add it to the Loom.
  myBus = MidiBus(this, -1, "Bus 1")
  loom.setMidiBus(myBus)

  # Rendering as a color, interpolate between black and white
  # rendering as MIDI, get the notes and scale from the pattern.
  pattern.asColor(0x000000, 0xFFFFFF).asMidiMessage(pattern)

  # Don't repeat.
  pattern.once()

  loom.play()


def draw():
  background(pattern.asColor())
