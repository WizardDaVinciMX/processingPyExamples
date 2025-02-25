add_library("controlP5.*

String[][] s = String[3][]
ControlP5 controlP5
ListBox l

def setup() :
  size(400,400)
  controlP5 = ControlP5(this)
  l = controlP5.addListBox("myList",100,100,120,150)
  # l.actAsPulldownMenu(True)
  l.setItemHeight(23)
  
  
  s[0] = String[] :
    "a","b","c","d"
  
  s[1] = String[] :
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n"
  
  s[2] = String[] :
    "l","m","n"
  
  
  for(i=0i<s[1].lengthi+=1) :
    l.addItem(s[1][i],i)
  



def draw() :
  background(0)


def keyPressed() :

  switch(key) :
    case('1'):
    println("changing list to items of group 1")
    l.clear()
    for(i=0i<s[0].lengthi+=1) :
      # using bit shifting to store 2 values in 1 int
      n = 0
      n = n | 1 << 8  
      n = n | i << 0 
      l.addItem("1-"+s[0][i],n)
    
    break
    case('2'):
    println("changing list to items of group 2")
    l.clear()
    for(i=0i<s[1].lengthi+=1) :
      # useing bit shifting to store 2 values in 1 int
      n = 0
      n = n | 2 << 8  
      n = n | i << 0 
      l.addItem("2-"+s[1][i],n)
    
    break
  


def myList(theValue) :
  println("from myList "+theValue)



def controlEvent(ControlEvent theEvent) :
  if(theEvent.isGroup()) :
  print("> "+theEvent.getGroup().getValue())
  n = int(theEvent.getGroup().getValue())
  println("\t\t group:"+(n >> 8 & 0xff)+", item:"+(n >> 0 & 0xff))
  

