"""
 * This is a simple example of how to use the Keystone library.
 *
 * To use this example in the real world, you need a projector
 * and a surface you want to project your Processing sketch onto.
 *
 * Simply drag the corners of the CornerPinSurface so that they
 * match the physical surface's corners. The result will be an
 * undistorted projection, regardless of projector position or 
 * orientation.
 *
 * You can also create more than one Surface object, and project
 * onto multiple flat surfaces using a single projector.
 *
 * This extra flexbility can comes at the sacrifice of more or 
 * less pixel resolution, depending on your projector and how
 * many surfaces you want to map. 
"""

add_library('keystone')

def setup():
  global ks
  global surface
  global offscreen

# Keystone will only work with P3D or OPENGL renderers, 
  # since it relies on texture mapping to deform
  size(800, 600, P3D)

  ks = Keystone(this)
  surface = ks.createCornerPinSurface(400, 300, 20)
  
  # We need an offscreen buffer to draw the surface we
  # want projected
  # note that we're matching the resolution of the
  # CornerPinSurface.
  # (The offscreen buffer can be P2D or P3D)
  offscreen = createGraphics(400, 300, P3D)

def draw():
  # Convert the mouse coordinate into surface coordinates
  # this will allow you to use mouse events inside the 
  # surface from your screen. 
  surfaceMouse = surface.getTransformedMouse()

  # Draw the scene, offscreen
  offscreen.beginDraw()
  offscreen.background(255)
  offscreen.fill(0, 255, 0)
  offscreen.ellipse(surfaceMouse.x, surfaceMouse.y, 75, 75)
  offscreen.endDraw()

  # most likely, you'll want a black background to minimize
  # bleeding around your projection area
  background(0)
 
  # render the scene, transformed using the corner pin surface
  surface.render(offscreen)

def keyPressed():
  if  key == 'c':
    # enter/leave calibration mode, where surfaces can be warped 
    # and moved
    ks.toggleCalibration()
  elif key == 'l':
    # loads the saved layout
    ks.load()
  elif key == 's':
    # saves the layout
    ks.save()
