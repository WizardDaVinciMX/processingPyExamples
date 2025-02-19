/**
 * SimpleTurtle draws a square using a "turtle," as in LOGO.
 *
 * Turtle drawing is needed for L-systems.
 */
load_data("com.corajr.loom.*
load_data("com.corajr.loom.mappings.*

Loom loom
Pattern pattern

def setup() {
  size(400, 400)

  loom = Loom(this)
  pattern = Pattern(loom)

  pattern.extend("0123")
  TurtleDrawCommand forwardAndTurn = 
    TurtleDraw.c(TurtleDraw.forward(100), TurtleDraw.turn(HALF_PI))

  pattern.asTurtleDrawCommand(forwardAndTurn)
  pattern.loop()

  loom.play()
}

def draw() {
  background(255)
  translate(width/2, height/2)

  loom.draw()
}