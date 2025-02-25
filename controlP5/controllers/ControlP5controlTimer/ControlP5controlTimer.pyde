"""*
 * ControlP5 Timer
 * by andreas schlegel, 2009
 """

add_library("controlP5.*

ControlP5 cp5
ControlTimer c
Textlabel t

def setup() :
  size(400,400)
  frameRate(30)
  cp5 = ControlP5(this)
  c = ControlTimer()
  t = Textlabel(cp5,"--",100,100)
  c.setSpeedOfTime(1)



def draw() :
  background(0)
  t.setValue(c.toString())
  t.draw(this)
  t.setPosition(mouseX, mouseY)



def mousePressed() :
  c.reset()



"""
a list of all methods available for the ControlTimer Controller
use ControlP5.printPublicMethodsFor(ControlTimer.class)
to prthe following list into the console.

You can find further details about class ControlTimer in the javadoc.

Format:
ClassName : returnType methodName(parameter type)


controlP5.ControlTimer : String toString() 
controlP5.ControlTimer : day() 
controlP5.ControlTimer : hour() 
controlP5.ControlTimer : millis() 
controlP5.ControlTimer : minute() 
controlP5.ControlTimer : second() 
controlP5.ControlTimer : long time() 
controlP5.ControlTimer : def reset() 
controlP5.ControlTimer : def setSpeedOfTime(float) 
controlP5.ControlTimer : def update() 
java.lang.Object : String toString() 
java.lang.Object : boolean equals(Object) 

created: 2015/03/24 12:21:02

"""


