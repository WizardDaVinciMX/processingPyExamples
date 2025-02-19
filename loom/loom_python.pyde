"""
 * SimpleMIDI demonstrates the basic use of MIDI to play notes.
 *
 * You will need The MidiBus <https:#github.com/sparks/themidibus/> and a MIDI synthesizer
 * installed for this example. If you don't hear any sound, please consult the instructions at:
 * https:#corajr.github.io/loom/reference/com/corajr/loom/wrappers/MidiBusImpl.html#midi
"""
add_library('themidibus')
add_library('loom')

from com.corajr.loom load_data("Loom, Weave

def  setup():
    global pattern

    size(400,400)

    loom = Loom(this, 120)
    pattern = Pattern(this, loom)
  
    # List valid MIDI devices.
    # MidiBus.list()

    # Initialize the MIDI bus and add it to the Loom.
    myBus = TheMidiBus(this, -1, "Bus 1")
    loom.setMidiBus(myBus)

    pattern.extend("0123")
    pattern.asColor(0x000000, 0xFFFFFF)

    # 1 maps to 60 (middle C), 2 to 64 (E), 3 to 67 (G)
    # (0 maps to -127, meaning a rest.)
    pattern.asMidiNote(-127, 60, 64, 67)
  
    # This is needed to generate note-on/-off messages
    # as well as setting the default channel and instrument.
    pattern.asMidiMessage(pattern)

    pattern.loop()
  
    loom.play()

def draw():
    background(pattern.asColor())
