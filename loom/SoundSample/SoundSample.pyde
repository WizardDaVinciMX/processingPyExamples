load_data("processing.sound.*

/**
 * SoundSample uses the Sound library to play a sample according to a pattern.
 *
 * Be sure you have installed the Sound library from the Processing
 * Contribution Manager (Sketch -> Import Library -> Add Library).
 */

load_data("com.corajr.loom.*
load_data("processing.sound.*
SoundFile snare

Loom loom
Pattern pattern

def setup() {
  size(400,400)
  
  loom = Loom(this)
  pattern = Pattern(loom)

  SoundFile snare = SoundFile(this, "snare.aif")
  pattern.extend("0101")
  pattern.asColor(#000000, #FFFFFF)
  pattern.asSoundFile(snare)

  pattern.loop()
  
  loom.play()
}

def draw() {
  background(pattern.asColor())
}