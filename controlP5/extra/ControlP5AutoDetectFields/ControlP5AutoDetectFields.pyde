"""*
 * ControlP5 Autodetect Fields
 *
 * test sketch, controller values will automatically be set 
 * to its corresponding sketch fields.
 *
 * by Andreas Schlegel, 2011
 * www.sojamo.de/libraries/controlp5
 *
 """


add_library("controlP5.*

s1 = 50
s2 = 50

nb1 = 50
nb2 = 50

k1 = 50
k2 = 50

boolean t1 = False
boolean t2 = False

r1 = 20
r2 = 50

def setup() :
  size(400,400)
  ControlP5 cp5 = ControlP5(this)
  cp5.addSlider("s1",10,150,10,10,100,15).setLabel("50")
  cp5.addSlider("s2",10,150,20,150,10,100,15).setLabel("20")
  
  cp5.addNumberbox("nb1",10,50,100,15).setLabel("50")
  cp5.addNumberbox("nb2",20,150,50,100,15).setLabel("20")
  
  cp5.addKnob("k1",10,150,10,150,50).setLabel("50")
  cp5.addKnob("k2",10,150,20,150,150,50).setLabel("20")
  
  cp5.addToggle("t1",10,240,100,15).setLabel("False")
  cp5.addToggle("t2",True,150,240,100,15).setLabel("True")
  
  cp5.addButton("b1",50,10,280,100,15).setLabel("50")
  cp5.addButton("b2",20,150,280,100,15).setLabel("20")
  
  cp5.addRange("r1",10,150,r1,r2,10,320,100,15).setLabel("50")
  


def draw() :
  background(0)


def controlEvent(ControlEvent c) :
  println(c.getValue())

