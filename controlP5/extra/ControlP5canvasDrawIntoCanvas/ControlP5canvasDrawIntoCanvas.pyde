"""*
 * ControlP5 DrawIntoCanvas
 *
 * this example demonstrates how to draw into a Canvas. 
 * Click and drag the mouse to show and draw into the Canvas.
 *
 * by Andreas Schlegel, 2011
 * www.sojamo.de/libraries/controlp5
 *
 """
 
add_library("controlP5.*

ControlP5 cp5

Canvas cc

# your controlWindowCanvas class
class MyCanvas extends Canvas :
  
  boolean mousePressed
  mouseX, mouseY
  public def update(PApplet theApplet) :
    mousePressed = theApplet.mousePressed
    mouseX = theApplet.mouseX
    mouseY = theApplet.mouseY
  
  
  public def draw(PGraphics theApplet) :
    theApplet.background(255)
     # a rectangle will be drawn if the mouse has been
    # pressed inside the main sketch window.
    # mousePressed here refers to the mousePressed
    # variable of your main sketch
    if(mousePressed) :
      theApplet.fill(255,0,0)
      theApplet.rect(10,10,100,100)
      theApplet.fill(0)
      theApplet.ellipse(mouseX,mouseY,20,20)
    
    # will draw a rectangle into the controlWindow
    # if the mouse has been pressed inside the controlWindow itself.
    # theApplet.mousePressed here refers to the
    # mousePressed variable of the controlWindow.
    if(mousePressed) :
      theApplet.fill(0)
      theApplet.rect(10,10,100,100)
      theApplet.fill(255,0,0)
      theApplet.ellipse(mouseX,mouseY,20,20)
    
    
  




def setup() :
  size(400,400)
  frameRate(30)
  cp5 = ControlP5(this)

  cc = MyCanvas()
  cc.pre()
  cp5.addCanvas(cc)



def draw():
  background(0)



