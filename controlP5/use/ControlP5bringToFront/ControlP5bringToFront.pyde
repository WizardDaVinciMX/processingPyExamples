add_library("controlP5.*

ControlP5 cp5

def setup() :
  size(700, 400)

  cp5 = ControlP5(this)

  CallbackListener toFront = CallbackListener() :
    public def controlEvent(CallbackEvent theEvent) :
        theEvent.getController().bringToFront()
        ((ScrollableList)theEvent.getController()).open()
    
  

  CallbackListener close = CallbackListener() :
    public def controlEvent(CallbackEvent theEvent) :
        ((ScrollableList)theEvent.getController()).close()
    
  

  cp5.addScrollableList("myList1")
          .setPosition(100, 100)
          .addItems(String[] :"a-1","b-1","c-1","d-1","e-1")
          .onEnter(toFront)
          .onLeave(close)
          .setWidth(200)
          .setItemHeight(20)
          .setBarHeight(20)
          .setBackgroundColor(color(128))
          .setHeight(100)
          .close()
          

  cp5.addScrollableList("myList2")
          .setPosition(100, 125)
          .addItems(String[] :"a-2","b-2","c-2","d-2","e-2")
          .onEnter(toFront)
          .onLeave(close)
          .setWidth(200)
          .setItemHeight(20)
          .setBarHeight(20)
          .setBackgroundColor(color(128))
          .setHeight(100)
          .setColor(ControlP5.THEME_RED)
          .close()
          




def draw() :
  background(220)

