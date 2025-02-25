
add_library("java.awt.*
add_library("java.awt.event.*
add_library("controlP5.*

private ControlP5 cp5

ControlFrame cf1, cf2

bgColor

def setup() :
  size(400, 400 ,P3D )
  """ add a controlP5 instance for the main sketch window (not required for other ControlFrames to work) """
  cp5 = ControlP5( this )
  cp5.addSlider( "s2" )


  """ Add a controlframe """

  cf1 = addControlFrame( "hello", 200, 200, 20, 20, color( 100 ) )

  # add a slider with an EventListener. When dragging the slider, 
  # variable bgColor will change accordingly. 
  cf1.control().addSlider( "s1" ).setRange( 0, 255 ).addListener( ControlListener() :
    public def controlEvent( ControlEvent ev ) :
      bgColor = color( ev.getValue() )
    
  
  )


  """ Add a second controlframe """

  cf2 = addControlFrame( "world", 200, 200, 20, 240, color( 100 ) )

  # add a button with an EventListener. When releasing the button, 
  # variable bgColor will change to color( 255 )  
  cf2.control().addButton( "b1" ).addListener( ControlListener() :
    public def controlEvent( ControlEvent ev ) :
      bgColor = color( 255 )
    
  
  )

  cf2.control().addButton( "b2" ).addListener( ControlListener() :
    public def controlEvent(ControlEvent ev) :
      bgColor = color( random( 255 ), random( 255 ), random( 255 ) )
    
  
  )


def draw() :
  background( bgColor )



""" no changes required below """


ControlFrame addControlFrame(String theName, theWidth, theHeight) :
  return addControlFrame(theName, theWidth, theHeight, 100, 100, color( 0 ) )


ControlFrame addControlFrame(String theName, theWidth, theHeight, theX, theY, theColor ) :
  final Frame f = Frame( theName )
  final ControlFrame p = ControlFrame( this, theWidth, theHeight, theColor )

  f.add( p )
  p.init()
  f.setTitle(theName)
  f.setSize( p.w, p.h )
  f.setLocation( theX, theY )
  f.addWindowListener( WindowAdapter() :
    @Override
      public def windowClosing(WindowEvent we) :
      p.dispose()
      f.dispose()
    
   
  )
  f.setResizable( False )
  f.setVisible( True )
  # sleep a little bit to allow p to call setup.
  # otherwise a Nonepointerexception might be caused.
  try :
    Thread.sleep( 100 )
   
  catch(Exception e) :
  
  return p



# the ControlFrame class extends PApplet, so we 
# are creating a processing applet inside a
# frame with a controlP5 object loaded
public class ControlFrame extends PApplet :

  w, h

  bg

  public def setup() :
    size(w, h)
    frameRate(25)
    cp5 = ControlP5( this )
  

  public def draw() :
    background( bg )
  

  private ControlFrame() :
  

  public ControlFrame(Object theParent, theWidth, theHeight, theColor) :
    parent = theParent
    w = theWidth
    h = theHeight
    bg = theColor
  


  public ControlP5 control() :
    return self.cp5
  

  ControlP5 cp5

  Object parent


