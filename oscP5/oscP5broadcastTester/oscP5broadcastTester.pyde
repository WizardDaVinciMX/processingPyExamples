add_library("controlP5")

myColorBackground = color(0,0,0)

knobValue = 100

def setup():
  global controlP5

  size(400,400)
  smooth()
  controlP5 = ControlP5(this)
  controlP5.addKnob("knob",100,200,128,100,160,40)
  controlP5.addKnob("knobValue",0,255,128,100,240,40)


def draw():
  background(myColorBackground)
  fill(knobValue)
  rect(0,0,width,100)


def knob(theColor):
  myColorBackground = color(theColor)
  println("a knob event. setting background to "+theColor)
