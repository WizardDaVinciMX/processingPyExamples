"""*
 * ControlP5 MultiList
 * by andreas schlegel, 2009
 *
 * broken with version 2.2.1+
 """

add_library("controlP5.*

ControlP5 controlP5
MultiList l

def setup() :
  size(700,400)
  frameRate(30)
  controlP5 = ControlP5(this)
  
  # sorry, MultiList is currently broken.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  # add a multiList to controlP5.
  # elements of the list have default dimensions
  # here, a width of 100 and a height of 12
  l = controlP5.addMultiList("myList",20,20,100,12)
  
  # create a multiListButton which we will use to
  # add buttons to the multilist
  MultiListButton b
  b = l.add("level1",1)
  
  # add items to a sublist of button "level1"
  b.add("level11",11).setLabel("level1 item1")
  b.add("level12",12).setLabel("level1 item2")

  b = l.add("level2",2)
  
  cnt = 100
  
  # add some more sublists.
  for(i=0i<10i+=1) :
    MultiListButton c = b.add("level2"+(i+1),20+i+1)
    c.setLabel("level2 item"+(i+1))
    c.setColorBackground(color(64 + 18*i,0,0))
    
    if(i==4) :
    # changing the width and the height of a button
    # will be inherited by its sublists.
    c.setWidth(100)
    c.setHeight(20)
    
    cnt+=1
    
    if(i==4) :
      for(j=0j<10j+=1) :
        cnt+=1
        MultiListButton d
        d = c.add("level2"+i+""+j,250+j+1)
        d.setLabel("level2 item"+(i+1)+" "+"item"+(j+1))
        d.setColorBackground(color(64 + 18*j,(64 + 18*j)/2,0))
        d.setId(cnt)
        d.setWidth(200)
      
    
  
  
  MultiListButton cc = (MultiListButton)controlP5.getController("level21")
  cc.setHeight(40)



def controlEvent(ControlEvent theEvent) :
  println(theEvent.getController().getName()+" = "+theEvent.value())  
  # uncomment the line below to remove a multilist item when clicked.
  # theEvent.controller().remove()



def draw() :
  background(0)


def keyPressed() :
  if(controlP5.getController("level23")!=None) :
    println("removing multilist button level23.")
    controlP5.getController("level23").remove()
  

