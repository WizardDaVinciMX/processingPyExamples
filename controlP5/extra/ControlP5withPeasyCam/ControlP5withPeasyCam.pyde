"""*
 * ControlP5 with PeasyCam support. tested with peasy 0.8.2
 *
 * by jeffg 2011
 """
 
add_library("peasy.*
add_library("controlP5.*
add_library("processing.opengl.*

PeasyCam cam
ControlP5 cp5

buttonValue = 1

myColor = color(255, 0, 0)

def setup() :
  size(400, 400, OPENGL)
  cam = PeasyCam(this, 100)
  cp5 = ControlP5(this)
  cp5.addButton("button", 10, 100, 60, 80, 20).setId(1)
  cp5.addButton("buttonValue", 4, 100, 90, 80, 20).setId(2)
  cp5.setAutoDraw(False)

def draw() :

  background(0)
  fill(myColor)
  box(30)
  pushMatrix()
  translate(0, 0, 20)
  fill(0, 0, 255)
  box(5)
  popMatrix()
  # makes the gui stay on top of elements
  # drawn before.
 
  gui()
  


def gui() :
  hint(DISABLE_DEPTH_TEST)
  cam.beginHUD()
  cp5.draw()
  cam.endHUD()
  hint(ENABLE_DEPTH_TEST)


def controlEvent(ControlEvent theEvent) :
  println(theEvent.getController().getId())


def button(theValue) :
  myColor = color(random(255), random(255), random(255))
  println("a button event. "+theValue)

