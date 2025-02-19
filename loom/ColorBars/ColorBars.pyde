/**
 * ColorBars renders a pattern spread out in space.
 *
 * Rather than showing just the present value, future pattern values
 * scroll across the screen.
 */

load_data("com.corajr.loom.*

Loom loom
Pattern pattern

def setup() {
  size(400, 400)

  loom = Loom(this)
  pattern = Pattern(loom)
    .extend("0123456")
    .loop()

  pattern.asColor(#EBEBEB, 
    #EBEB10, 
    #10EBEB, 
    #10EB10, 
    #EB10EB, 
    #EB1010, 
    #1010EB)

  loom.play()
}

def draw() {
  background(0)

  # Render the full pattern as a rectangle (args in x, y, w, h order)
  pattern.rect(0, 0, width, height)
}