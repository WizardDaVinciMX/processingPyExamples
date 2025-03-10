
"""*
 * ControlP5 MenuList
 * 
 * A custom Controller, a scrollable Menu List, using a PGraphics buffer.
 * Allows custom designs for List Item.
 *
 * by Andreas Schlegel, 2013
 * www.sojamo.de/libraries/controlp5
 *
 """
 
add_library("controlP5.*
add_library("static controlP5.ControlP5.*
add_library("java.util.*
add_library("java.util.Map.Entry


ControlP5 cp5

PFont f1, f2
def setup() :
  size(800, 500, P3D )
  f1 = createFont("Helvetica", 20)
  f2 = createFont("Helvetica", 12)

  cp5 = ControlP5( this )
  
  
  """ create a custom MenuList with name menu, notice that function 
   * menu will be called when a menu item has been clicked.
   """
  MenuList m = MenuList( cp5, "menu", 200, 368 )
  
  m.setPosition(40, 40)
  # add some items to our menuList
  for (i=0i<100i+=1) :
    m.addItem(makeItem("headline-"+i, "subline", "some copy lorem ipsum ", createImage(50, 50, RGB)))
  


""" a convenience function to build a map that contains our key-value pairs which we will 
 * then use to render each item of the menuList.
 """
Map<String, Object> makeItem(String theHeadline, String theSubline, String theCopy, PImage theImage) :
  Map m = HashMap<String, Object>()
  m.put("headline", theHeadline)
  m.put("subline", theSubline)
  m.put("copy", theCopy)
  m.put("image", theImage)
  return m


def menu(i) :
  println("got some menu event from item with index "+i)


public def controlEvent(ControlEvent theEvent) :
  if(theEvent.isFrom("menu")):
    Map m = ((MenuList)theEvent.getController()).getItem(int(theEvent.getValue()))
    println("got a menu event from item : "+m)
  


def draw() :
  background( 40 )



""" A custom Controller that implements a scrollable menuList. Here the controller 
 * uses a PGraphics element to render customizable list items. The menuList can be scrolled
 * using the scroll-wheel, touchpad, or mouse-drag. Items are triggered by a click. clicking 
 * the scrollbar to the right makes the list scroll to the item correspoinding to the 
 * click-location. 
 """ 
class MenuList extends Controller<MenuList> :

  pos, npos
  itemHeight = 100
  scrollerLength = 40
  List< Map<String, Object>> items = ArrayList< Map<String, Object>>()
  PGraphics menu
  boolean updateMenu

  MenuList(ControlP5 c, String theName, theWidth, theHeight) :
    super( c, theName, 0, 0, theWidth, theHeight )
    c.register( this )
    menu = createGraphics(getWidth(), getHeight() )

    setView(ControllerView<MenuList>() :

      public def display(PGraphics pg, MenuList t ) :
        if (updateMenu) :
          updateMenu()
        
        if (inside() ) :
          menu.beginDraw()
          len = -(itemHeight * items.size()) + getHeight()
          ty = int(map(pos, len, 0, getHeight() - scrollerLength - 2, 2 ) )
          menu.fill(255 )
          menu.rect(getWidth()-4, ty, 4, scrollerLength )
          menu.endDraw()
        
        pg.image(menu, 0, 0)
      
    
    )
    updateMenu()
  

  """ only update the image buffer when necessary - to save some resources """
  def updateMenu() :
    len = -(itemHeight * items.size()) + getHeight()
    npos = constrain(npos, len, 0)
    pos += (npos - pos) * 0.1
    menu.beginDraw()
    menu.noStroke()
    menu.background(255, 64 )
    menu.textFont(cp5.getFont().getFont())
    menu.pushMatrix()
    menu.translate( 0, pos )
    menu.pushMatrix()

    i0 = PApplet.max( 0, int(map(-pos, 0, itemHeight * items.size(), 0, items.size())))
    range = ceil((float(getHeight())/float(itemHeight))+1)
    i1 = PApplet.min( items.size(), i0 + range )

    menu.translate(0, i0*itemHeight)

    for (i=i0i<i1i+=1) :
      Map m = items.get(i)
      menu.fill(255, 100)
      menu.rect(0, 0, getWidth(), itemHeight-1 )
      menu.fill(255)
      menu.textFont(f1)
      menu.text(m.get("headline").toString(), 10, 20 )
      menu.textFont(f2)
      menu.textLeading(12)
      menu.text(m.get("subline").toString(), 10, 35 )
      menu.text(m.get("copy").toString(), 10, 50, 120, 50 )
      menu.image(((PImage)m.get("image")), 140, 10, 50, 50 )
      menu.translate( 0, itemHeight )
    
    menu.popMatrix()
    menu.popMatrix()
    menu.endDraw()
    updateMenu = abs(npos-pos)>0.01 ? True:False
  
  
  """ when detecting a click, check if the click happend to the far right, if yes, scroll to that position, 
   * otherwise do whatever this item of the list is supposed to do.
   """
  public def onClick() :
    if (getPointer().x()>getWidth()-10) :
      npos= -map(getPointer().y(), 0, getHeight(), 0, items.size()*itemHeight)
      updateMenu = True
     
    else :
      len = itemHeight * items.size()
      index = int( map( getPointer().y() - pos, 0, len, 0, items.size() ) ) 
      setValue(index)
    
  
  
  public def onMove() :
  

  public def onDrag() :
    npos += getPointer().dy() * 2
    updateMenu = True
   

  public def onScroll(n) :
    npos += ( n * 4 )
    updateMenu = True
  

  def addItem(Map<String, Object> m) :
    items.add(m)
    updateMenu = True
  
  
  Map<String,Object> getItem(theIndex) :
    return items.get(theIndex)
  


