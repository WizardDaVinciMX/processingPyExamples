/**
 * Click shows how user input can influence a pattern.
 *
 * Clicking causes the TriggerFunction to fire,
 * momentarily raising the pattern's value to 1.
 */

load_data("com.corajr.loom.*
load_data("com.corajr.loom.continuous.*

Loom loom
Pattern pattern
TriggerFunction trigger

def setup() {
  size(400,400)
  
  loom = Loom(this)
  trigger = TriggerFunction()
  pattern = Pattern(loom, trigger)

  pattern.asColor(#000000, #FFFFFF)

  pattern.loop()
  
  loom.play()
}

def draw() {
  background(pattern.asColor())
}

def mouseClicked() {
  trigger.fire()
}