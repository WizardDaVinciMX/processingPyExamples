"""*
 * ControlP5 quick
 *
 * this example demonstrates how to quickly add Controllers such as
 * Button, Slider,Toggle and Numberbox to a sketch without having to set
 * positions, this is done automatically by cp5.
 * controllers will be aligned horizontally - .linebreak() will
 * force the next controller to the next line.
 * the example shows as well how to link variables and functions to
 * a controller. this is done by assigning the name of the variable
 * or function to a controller.  
 *
 * by Andreas Schlegel, 2012
 * www.sojamo.de/libraries/controlp5
 *
 """


add_library("controlP5.*

ControlP5 cp5

s1 = 5
s2 = 2
boolean t1 = True
boolean t2 = True
boolean t3 = True
boolean t4 = True
n1 = 100
n2 = 50

def setup() :
  size(600,400)
  noStroke()
  cp5 = ControlP5(this)
  cp5.addButton("b1",1)
  cp5.addButton("b2",2)
  cp5.addButton("b3",3)
  cp5.addButton("b4",4).linebreak()
  cp5.addSlider("s1",0,10)
  cp5.addSlider("s2",0,10).linebreak()
  cp5.addButton("b5")
  cp5.addToggle("t1")
  cp5.addToggle("t2")
  cp5.addToggle("t3")
  cp5.addToggle("t4").linebreak()
  cp5.addNumberbox("n1")
  cp5.addNumberbox("n2")


def draw() :
  background(0)
  if(t1) :
    fill(s1*25)
    rect(0,200,150,height)
  
  if(t2) :
    fill(s2*25)
    rect(150,200,150,height)
  
  if(t3) :
    fill(n1)
    rect(300,200,150,height)
  
  if(t4) :
    fill(n2)
    rect(450,200,150,height)
  


def b1(theN) :
  println(theN)


def b2(theN) :
  println(theN)





