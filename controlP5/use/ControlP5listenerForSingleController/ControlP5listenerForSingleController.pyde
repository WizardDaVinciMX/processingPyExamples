"""*
 * ControlP5 Listener.
 * the ControlListener interface can be used to implement a custom 
 * ControlListener which listens for incoming ControlEvent from specific
 * controller(s). MyControlListener in the example below listens to
 * ControlEvents coming in from controller 'mySlider'.
 *
 * by andreas schlegel, 2012
 """
add_library("controlP5.*

ControlP5 cp5
MyControlListener myListener

def setup() :
  size(700,400)


  cp5 = ControlP5(this)
  cp5.setColor(ControlP5.THEME_RED)  
  
  cp5.addSlider("mySlider")
     .setRange(100,200)
     .setValue(140)
     .setPosition(200,200)
     .setSize(200,20)
  
  myListener = MyControlListener()
  
  cp5.getController("mySlider").addListener(myListener)


def draw() :
  background(myListener.col)  



class MyControlListener implements ControlListener :
  col
  public def controlEvent(ControlEvent theEvent) :
    println("i got an event from mySlider, " +
            "changing background color to "+
            theEvent.getController().getValue())
    col = (int)theEvent.getController().getValue()
  


