/**
 * Clap replicates a famous composition by a minimalist composer.
 *
 * There are two patterns: one stays the same and the other shifts.
 * The procedure for shifting the second pattern is described declaratively,
 * rather than written out.
 *
 * You will need The MidiBus <https:#github.com/sparks/themidibus/> and a MIDI synthesizer
 * installed for this example. If you don't hear any sound, please consult the instructions at:
 * https:#corajr.github.io/loom/reference/com/corajr/loom/wrappers/MidiBusImpl.html#midi
 */
load_data("themidibus.*

load_data("com.corajr.loom.*
load_data("com.corajr.loom.transforms.*
load_data("com.corajr.loom.continuous.*
load_data("com.corajr.loom.util.MidiTools.Percussion

MidiBus myBus
Loom loom
Pattern pattern, pattern2

def setup() {
  size(400, 400)

  loom = Loom(this, 112)

  # List valid MIDI devices.
  # MidiBus.list()

  # Initialize the MIDI bus and add it to the Loom.
  myBus = MidiBus(this, -1, "Bus 1")
  loom.setMidiBus(myBus)

  pattern = Pattern(loom)

  # define the basic beat pattern
  pattern.extend("111011010110").loop()
  pattern.asColor(#000000, #FFFFFF)  
  pattern2 = pattern.clone()

  pattern.asMidiPercussion(Percussion.HAND_CLAP)
  pattern2.asMidiPercussion(Percussion.CLAVES)

  # This is the crucial piece: every 4 bars, shift the 12-beat pattern left by 1.
  pattern2.every(4, Transforms.Shift(-1, 12))

  loom.play()
}

def draw() {
  background(0)

  fill(pattern.asColor())
  rect(0, 0, width / 2, height)

  fill(pattern2.asColor())
  rect(width / 2, 0, width / 2, height)
}