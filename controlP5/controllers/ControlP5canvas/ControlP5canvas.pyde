"""*
 * ControlP5 Canvas
 * The ControlWindowCanvas allow you to add custom graphics to 
 * the default controlP5 renderer or a controlWindow rednerer.
 *
 * find a list of public methods available for the Canvas Controller 
 * at the bottom of this sketch's source code
 *
 * by Andreas Schlegel, 2011
 * www.sojamo.de/libraries/controlp5
 * 
 """


add_library("controlP5.*

ControlP5 cp5

ControlWindow controlWindow

Canvas cc

# MyCanvas, your Canvas render class
class MyCanvas extends Canvas :

  y
  mx = 0
  my = 0
  public def setup(PGraphics pg) :
    y = 200
    

  public def update(PApplet p) :
    mx = p.mouseX
    my = p.mouseY
  

  public def draw(PGraphics pg) :
    # renders a square with randomly changing colors
    # make changes here.
    pg.fill(100)
    pg.rect(mx-20, y-20, 240, 30)
    pg.fill(255)
    pg.text("This text is drawn by MyCanvas", mx,y)
  



def setup() :
  size(400, 400)
  frameRate(30)
  cp5 = ControlP5(this)

  # create a control window canvas and add it to
  # the previously created control window.  
  cc = MyCanvas()
  cc.pre() # use cc.post() to draw on top of existing controllers.
  cp5.addCanvas(cc) # add the canvas to cp5


def draw() :
  background(0)
  fill(60)
  rect(100, 100, 200, 200)



"""
a list of all methods available for the Canvas Controller
use ControlP5.printPublicMethodsFor(Canvas.class)
to prthe following list into the console.

You can find further details about class Canvas in the javadoc.

Format:
ClassName : returnType methodName(parameter type)


controlP5.Canvas : def moveTo(ControlWindow) 
controlP5.Canvas : def setup(PGraphics) 
controlP5.Canvas : def update(PApplet) 
java.lang.Object : String toString() 
java.lang.Object : boolean equals(Object) 

created: 2015/03/24 12:20:53

"""


