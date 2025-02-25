"""*
 * ControlP5 Controlframe
 *
 * this example shows you how to create separate window to 
 * display and use controllers with  processing 3
 *
 * by Andreas Schlegel, 2016
 * www.sojamo.de/libraries/controlp5
 *
 """

add_library("controlP5.*

ControlFrame cf

speed
pos
c0, c1, c2, c3
boolean auto

def settings() :
  size(400, 400, P3D)


def setup() :
  cf = ControlFrame(this, 400, 800, "Controls")
  surface.setLocation(420, 10)
  noStroke()


def draw() :
  if (auto) pos += speed
  background(0)
  translate(width/2, height/2)
  rotateY(pos)
  lights()
  fill(c0, c1, c2, c3)
  box(100)





class ControlFrame extends PApplet :

  w, h
  PApplet parent
  ControlP5 cp5

  public ControlFrame(PApplet _parent, _w, _h, String _name) :
    super()   
    parent = _parent
    w=_w
    h=_h
    PApplet.runSketch(String[]:self.getClass().getName(), this)
  

  public def settings() :
    size(w, h)
  

  public def setup() :
    surface.setLocation(10, 10)
    cp5 = ControlP5(this)
    
    cp5.addToggle("auto")
       .plugTo(parent, "auto")
       .setPosition(10, 70)
       .setSize(50, 50)
       .setValue(True)
       
    cp5.addKnob("blend")
       .plugTo(parent, "c3")
       .setPosition(100, 300)
       .setSize(200, 200)
       .setRange(0, 255)
       .setValue(200)
       
    cp5.addNumberbox("color-red")
       .plugTo(parent, "c0")
       .setRange(0, 255)
       .setValue(255)
       .setPosition(100, 10)
       .setSize(100, 20)
       
    cp5.addNumberbox("color-green")
       .plugTo(parent, "c1")
       .setRange(0, 255)
       .setValue(128)
       .setPosition(100, 70)
       .setSize(100, 20)
       
    cp5.addNumberbox("color-blue")
       .plugTo(parent, "c2")
       .setRange(0, 255)
       .setValue(0)
       .setPosition(100, 130)
       .setSize(100, 20)
       
    cp5.addSlider("speed")
       .plugTo(parent, "speed")
       .setRange(0, 0.1)
       .setValue(0.01)
       .setPosition(100, 240)
       .setSize(200, 30)
       
  

  def draw() :
    background(190)
  
