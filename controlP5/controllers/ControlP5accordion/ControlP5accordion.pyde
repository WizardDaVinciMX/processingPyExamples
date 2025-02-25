"""
 ControlP5 Accordion
 arrange controller groups in an accordion like style.

 find a list of public methods available for the Accordion Controller 
 at the bottom of this sketch. In the example below 3 groups with controllers
 are created and added to an accordion controller. Furthermore several key 
 combinations are mapped to control individual settings of the accordion.
 An accordion comes in 2 modes, Accordion.SINGLE and Accordion.MULTI where the 
 latter allows to open multiple groups of an accordion and the SINGLE mode only
 allows 1 group to be opened at a time.  

 by Andreas Schlegel, 2012
 www.sojamo.de/libraries/controlp5
 
"""

add_library("controlP5")

c = color(0, 160, 100)

def setup():
  global cp5
  global accordion

  size(400, 600)
  noStroke()
  smooth()
  gui()


def gui():
  global cp5

  cp5 = ControlP5(this)
  
  # group number 1, contains 2 bangs
  g1 = cp5.addGroup("myGroup1")
  g1.setBackgroundColor(color(0, 64))
  g1.setBackgroundHeight(150)

  cp5.addBang("bang")\
  .setPosition(10,20)\
  .setSize(100,100)\
  .moveTo(g1)\
  .plugTo(this,"shuffle")


  # group number 2, contains a radiobutton
  g2 = cp5.addGroup("myGroup2")
  g2.setBackgroundColor(color(0, 64))
  g2.setBackgroundHeight(150)


  cp5.addRadioButton("radio")\
  .setPosition(10,20)\
  .setItemWidth(20)\
  .setItemHeight(20)\
  .addItem("black", 0)\
  .addItem("red", 1)\
  .addItem("green", 2)\
  .addItem("blue", 3)\
  .addItem("grey", 4)\
  .setColorLabel(color(255))\
  .activate(2)\
  .moveTo(g2)


  # group number 3, contains a bang and a slider
  g3 = cp5.addGroup("myGroup3")
  g3.setBackgroundColor(color(0, 64))
  g3.setBackgroundHeight(150)


  cp5.addBang("shuffle")\
  .setPosition(10,20)\
  .setSize(40,50)\
  .moveTo(g3)
     
  cp5.addSlider("hello")\
  .setPosition(60,20)\
  .setSize(100,20)\
  .setRange(100,500)\
  .setValue(100)\
  .moveTo(g3)

  cp5.addSlider("world")\
  .setPosition(60,50)\
  .setSize(100,20)\
  .setRange(100,500)\
  .setValue(200)\
  .moveTo(g3)


  # create a accordion
  # add g1, g2, and g3 to the accordion.
  accordion = cp5.addAccordion("acc")\
  .setPosition(40,40)\
  .setWidth(200)\
  .addItem(g1)\
  .addItem(g2)\
  .addItem(g3)

  class ControlKey1(ControlKey):
    def keyEvent(self):
        accordion.open(0,1,2)
  
  class ControlKey2(ControlKey):
    def keyEvent(self):
        accordion.close(0,1,2)
  
  class ControlKey3(ControlKey):
    def keyEvent(self):
        accordion.setWidth(300)

  class ControlKey4(ControlKey):
     def keyEvent(self):
        accordion.setPosition(0,0)
        accordion.setItemHeight(190)

  class ControlKey5(ControlKey):
     def keyEvent(self):
        accordion.setCollapseMode(ControlP5.SINGLE)

  class ControlKey6(ControlKey):
     def keyEvent(self):
        accordion.setCollapseMode(ControlP5.ALL)

  class ControlKey7(ControlKey):
     def keyEvent(self):
        cp5.remove("myGroup1")
        
  cp5.mapKeyFor(ControlKey1(), 'o')
  cp5.mapKeyFor(ControlKey2(), 'c')
  cp5.mapKeyFor(ControlKey3(), '1')
  cp5.mapKeyFor(ControlKey4(), '2') 
  cp5.mapKeyFor(ControlKey5(), '3')
  cp5.mapKeyFor(ControlKey6(), '4')
  cp5.mapKeyFor(ControlKey7(), '0')
  
  accordion.open(0,1,2)
  
  # use Accordion.MULTI to allow multiple group 
  # to be open at a time.
  accordion.setCollapseMode(Accordion.MULTI)
  
  # when in SINGLE mode, only 1 accordion  
  # group can be open at a time.  
  # accordion.setCollapseMode(Accordion.SINGLE)

  

def radio(theC):
  if   theC == 0:
    c = color(0,200)
  elif theC == 1:
    c = color(255,0,0,200)
  elif theC == 2:
    c = color(0, 200, 140,200)
  elif theC == 3:
    c = color(0, 128, 255,200)
  elif theC == 4:
    c = color(50,128)


def shuffle():
  c = color(random(255),random(255),random(255),random(128,255))

def draw() :
  global cp5
  background(220)
  
  fill(c)
  
  s1 = cp5.getController("hello").getValue()
  ellipse(200,400,s1,s1)
  
  s2 = cp5.getController("world").getValue()
  ellipse(300,100,s2,s2)


"""
a list of all methods available for the Accordion Controller
use ControlP5.printPublicMethodsFor(Accordion.class)
to prthe following list into the console.

You can find further details about class Accordion in the javadoc.

Format:
ClassName : returnType methodName(parameter type)


controlP5.Accordion : Accordion addItem(ControlGroup) 
controlP5.Accordion : Accordion close() 
controlP5.Accordion : Accordion open() 
controlP5.Accordion : Accordion remove(ControllerInterface) 
controlP5.Accordion : Accordion removeItem(ControlGroup) 
controlP5.Accordion : Accordion setCollapseMode(int) 
controlP5.Accordion : Accordion setItemHeight(int) 
controlP5.Accordion : Accordion setMinItemHeight(int) 
controlP5.Accordion : Accordion setWidth(int) 
controlP5.Accordion : Accordion updateItems() 
controlP5.Accordion : getItemHeight() 
controlP5.Accordion : getMinItemHeight() 
controlP5.ControlGroup : Accordion activateEvent(boolean) 
controlP5.ControlGroup : Accordion addListener(ControlListener) 
controlP5.ControlGroup : Accordion removeListener(ControlListener) 
controlP5.ControlGroup : Accordion setBackgroundColor(int) 
controlP5.ControlGroup : Accordion setBackgroundHeight(int) 
controlP5.ControlGroup : Accordion setBarHeight(int) 
controlP5.ControlGroup : Accordion setSize(int, int) 
controlP5.ControlGroup : Accordion updateInternalEvents(PApplet) 
controlP5.ControlGroup : String getInfo() 
controlP5.ControlGroup : String toString() 
controlP5.ControlGroup : getBackgroundHeight() 
controlP5.ControlGroup : getBarHeight() 
controlP5.ControlGroup : listenerSize() 
controlP5.ControllerGroup : Accordion add(ControllerInterface) 
controlP5.ControllerGroup : Accordion addListener(ControlListener) 
controlP5.ControllerGroup : Accordion bringToFront() 
controlP5.ControllerGroup : Accordion bringToFront(ControllerInterface) 
controlP5.ControllerGroup : Accordion close() 
controlP5.ControllerGroup : Accordion disableCollapse() 
controlP5.ControllerGroup : Accordion enableCollapse() 
controlP5.ControllerGroup : Accordion hide() 
controlP5.ControllerGroup : Accordion hideArrow() 
controlP5.ControllerGroup : Accordion hideBar() 
controlP5.ControllerGroup : Accordion moveTo(ControlWindow) 
controlP5.ControllerGroup : Accordion moveTo(PApplet) 
controlP5.ControllerGroup : Accordion open() 
controlP5.ControllerGroup : Accordion registerProperty(String) 
controlP5.ControllerGroup : Accordion registerProperty(String, String) 
controlP5.ControllerGroup : Accordion remove(CDrawable) 
controlP5.ControllerGroup : Accordion remove(ControllerInterface) 
controlP5.ControllerGroup : Accordion removeCanvas(Canvas) 
controlP5.ControllerGroup : Accordion removeListener(ControlListener) 
controlP5.ControllerGroup : Accordion removeProperty(String) 
controlP5.ControllerGroup : Accordion removeProperty(String, String) 
controlP5.ControllerGroup : Accordion setAddress(String) 
controlP5.ControllerGroup : Accordion setArrayValue(float[]) 
controlP5.ControllerGroup : Accordion setArrayValue(int, float) 
controlP5.ControllerGroup : Accordion setCaptionLabel(String) 
controlP5.ControllerGroup : Accordion setColor(CColor) 
controlP5.ControllerGroup : Accordion setColorActive(int) 
controlP5.ControllerGroup : Accordion setColorBackground(int) 
controlP5.ControllerGroup : Accordion setColorForeground(int) 
controlP5.ControllerGroup : Accordion setColorLabel(int) 
controlP5.ControllerGroup : Accordion setColorValue(int) 
controlP5.ControllerGroup : Accordion setHeight(int) 
controlP5.ControllerGroup : Accordion setId(int) 
controlP5.ControllerGroup : Accordion setLabel(String) 
controlP5.ControllerGroup : Accordion setMouseOver(boolean) 
controlP5.ControllerGroup : Accordion setMoveable(boolean) 
controlP5.ControllerGroup : Accordion setOpen(boolean) 
controlP5.ControllerGroup : Accordion setPosition(float, float) 
controlP5.ControllerGroup : Accordion setPosition(float[]) 
controlP5.ControllerGroup : Accordion setSize(int, int) 
controlP5.ControllerGroup : Accordion setStringValue(String) 
controlP5.ControllerGroup : Accordion setTitle(String) 
controlP5.ControllerGroup : Accordion setUpdate(boolean) 
controlP5.ControllerGroup : Accordion setValue(float) 
controlP5.ControllerGroup : Accordion setVisible(boolean) 
controlP5.ControllerGroup : Accordion setWidth(int) 
controlP5.ControllerGroup : Accordion show() 
controlP5.ControllerGroup : Accordion showArrow() 
controlP5.ControllerGroup : Accordion showBar() 
controlP5.ControllerGroup : Accordion update() 
controlP5.ControllerGroup : Accordion updateAbsolutePosition() 
controlP5.ControllerGroup : CColor getColor() 
controlP5.ControllerGroup : Canvas addCanvas(Canvas) 
controlP5.ControllerGroup : ControlWindow getWindow() 
controlP5.ControllerGroup : Controller getController(String) 
controlP5.ControllerGroup : ControllerProperty getProperty(String) 
controlP5.ControllerGroup : ControllerProperty getProperty(String, String) 
controlP5.ControllerGroup : Label getCaptionLabel() 
controlP5.ControllerGroup : Label getValueLabel() 
controlP5.ControllerGroup : String getAddress() 
controlP5.ControllerGroup : String getInfo() 
controlP5.ControllerGroup : String getName() 
controlP5.ControllerGroup : String getStringValue() 
controlP5.ControllerGroup : String toString() 
controlP5.ControllerGroup : Tab getTab() 
controlP5.ControllerGroup : boolean isBarVisible() 
controlP5.ControllerGroup : boolean isCollapse() 
controlP5.ControllerGroup : boolean isMouseOver() 
controlP5.ControllerGroup : boolean isMoveable() 
controlP5.ControllerGroup : boolean isOpen() 
controlP5.ControllerGroup : boolean isUpdate() 
controlP5.ControllerGroup : boolean isVisible() 
controlP5.ControllerGroup : boolean setMousePressed(boolean) 
controlP5.ControllerGroup : getArrayValue(int) 
controlP5.ControllerGroup : getValue() 
controlP5.ControllerGroup : float[] getArrayValue() 
controlP5.ControllerGroup : float[] getPosition() 
controlP5.ControllerGroup : getHeight() 
controlP5.ControllerGroup : getId() 
controlP5.ControllerGroup : getWidth() 
controlP5.ControllerGroup : listenerSize() 
controlP5.ControllerGroup : def controlEvent(ControlEvent) 
controlP5.ControllerGroup : def remove() 
java.lang.Object : String toString() 
java.lang.Object : boolean equals(Object) 

created: 2015/03/24 12:25:32

"""
