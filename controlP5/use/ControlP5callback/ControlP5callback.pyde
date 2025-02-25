"""*
 * ControlP5 Callback
 *
 * The following example demonstrates the CallbackListener and CallbackEvent. 
 * Here additional information about each available slider will be show when
 * hovering the controller with the mouse. The info will fade out when leaving
 * the controller. 
 *
 * When hovering a controller, the mouse pointer will change as well.
 * 
 * find a list of public methods available for the CallbackEvent Controller
 * at the bottom of this sketch.
 *
 * by Andreas Schlegel, 2012
 * www.sojamo.de/libraries/controlp5
 *
 """

add_library("controlP5.*

ControlP5 cp5
Slider s1, s2
Info info
CallbackListener cb

def setup() :
  size(800, 400)

  cp5 = ControlP5(this)

  
  # create a instance of class Info
  # info will be used to display a controller's information and
  # will fade in when a CallbackEvent is invoked.
  info = Info()


  # add 2 sliders
  s1 = cp5.addSlider("hello")
          .setRange(0, 100)
          .setValue(50)
          .setPosition(40, 40)
          .setSize(100, 20)
          
  s2 = cp5.addSlider("world")
          .setRange(0, 100)
          .setValue(10)
          .setPosition(40, 70)
          .setSize(100, 20)


  # the following CallbackListener will listen to any controlP5 
  # action such as enter, leave, pressed, released, releasedoutside, broadcast
  # see static variables starting with ACTION_ inside class controlP5.ControlP5Constants

  cb = CallbackListener() :
    public def controlEvent(CallbackEvent theEvent) :
      switch(theEvent.getAction()) :
        case(ControlP5.ACTION_ENTER):
        info.n = 1
        info.label.setText(theEvent.getController().getInfo())
        cursor(HAND)
        break
        case(ControlP5.ACTION_LEAVE):
        case(ControlP5.ACTION_RELEASEDOUTSIDE):
        info.n = 0
        cursor(ARROW)
        break
      
    
  

  # add the above callback to controlP5
  cp5.addCallback(cb)

  # add another callback to slider s1, callback event will only be invoked for this 
  # particular controller.
  s1.addCallback(CallbackListener() :
    public def controlEvent(CallbackEvent theEvent) :
      if (theEvent.getAction()==ControlP5.ACTION_BROADCAST) :
        s2.setValue(s2.getMax() - s1.getValue())
      
    
  
  )


def draw() :
  background(0)
  info.update()



def controlEvent(ControlEvent theEvent) :
  println("Got a ControlEvent for "+theEvent.name()+" = "+theEvent.value())
  info.label.setText(theEvent.getController().getInfo())


def keyPressed() :
  # uncomment the line below to remove callback cb from controlP5
  # when a key is pressed.
  #controlP5.removeCallback(cb)


# controlEvent(CallbackEvent) is called whenever a callback 
# has been triggered. controlEvent(CallbackEvent) is detected by 
# controlP5 automatically.
def controlEvent(CallbackEvent theEvent) :
  if (theEvent.getController().equals(s2)) :
    switch(theEvent.getAction()) :
      case(ControlP5.ACTION_ENTER): 
      println("Action:ENTER")
      break
      case(ControlP5.ACTION_LEAVE): 
      println("Action:LEAVE")
      break
      case(ControlP5.ACTION_PRESSED): 
      println("Action:PRESSED")
      break
      case(ControlP5.ACTION_RELEASED): 
      println("Action:RELEASED")
      break
      case(ControlP5.ACTION_RELEASEDOUTSIDE): 
      println("Action:RELEASED OUTSIDE")
      break
      case(ControlP5.ACTION_BROADCAST): 
      println("Action:BROADCAST")
      break
    
  




class Info :
  a
  n = 0
  String txt = ""
  Textarea label
  
  Info() :
    label = cp5.addTextarea("Hello\nWorld")
               .setSize(200,200)
               .setPosition(300,40)
               .setColor(color(255))
               .setColorBackground(color(100,0))
               .setLineHeight(12)
                   
  
  
  def update() :
    a += (n-a)*0.1
    label.setColorBackground(color(100,255*a))
  



"""
a list of all methods available for the CallbackEvent Controller
 use ControlP5.printPublicMethodsFor(CallbackEvent.class)
 to prthe following list into the console.
 
 You can find further details about class CallbackEvent in the javadoc.
 
 Format:
 ClassName : returnType methodName(parameter type)
 
 
 controlP5.CallbackEvent : Controller getController() 
 controlP5.CallbackEvent : getAction() 
 java.lang.Object : String toString() 
 java.lang.Object : boolean equals(Object) 
 
 
 """



