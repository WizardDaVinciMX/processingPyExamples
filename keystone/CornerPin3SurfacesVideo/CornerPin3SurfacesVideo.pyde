"""
*
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
add_library("video")
add_library('keystone')

isPlaying = False

# this is just for having something on the surfaces
x = 0
y = 150

def setup():
  global ks
  global surfaceOne
  global surfaceTwo
  global surfaceThree
  global offscreenOne
  global offscreenTwo
  global offscreenThree
  global mov

  # Keystone will only work with P3D or OPENGL renderers, 
  # since it relies on texture mapping to deform
  #size(800, 600, P3D)
  fullScreen(P3D)

  ks = Keystone(this) # init the Keystone library
  surfaceOne = ks.createCornerPinSurface(400, 300, 20) # create the first surface
  surfaceTwo = ks.createCornerPinSurface(400, 300, 20) # and the second
  surfaceThree = ks.createCornerPinSurface(400, 300, 20) # and the second
  mov =  Movie(this, "cube-inset-h264.mov" ) # load the video
  mov.frameRate(25) # set the framerate
  # We need an offscreen buffer to draw the surface we
  # want projected
  # note that we're matching the resolution of the
  # CornerPinSurface.
  # (The offscreen buffer can be P2D or P3D)
  offscreenOne = createGraphics(400, 300, P3D) 
  offscreenTwo = createGraphics(400, 300, P3D)
  offscreenThree = createGraphics(400,300, P3D)
  mov.play()# we need to start the movie once
  mov.jump(0)# go to the first frame
  mov.pause() # and hold it until we hit p

def draw():
  global x
  global y
  global mov
  # Draw the scene, on offscreen buffer one
  offscreenOne.beginDraw()
  offscreenOne.background(255)
  offscreenOne.fill(0, 255, 0)
  offscreenOne.ellipse(x, y, 20, 20)
  offscreenOne.endDraw()
  # Draw the scene, on offscreen buffer two
  offscreenTwo.beginDraw()
  offscreenTwo.background(255)
  offscreenTwo.fill(0, 255, 0)
  offscreenTwo.ellipse(x - 400, y, 20, 20)
  offscreenTwo.endDraw()
  offscreenThree.beginDraw() # start writing into the buffer
  offscreenThree.background(255)
  offscreenThree.image(mov, 0, 0) # <-- here we add the current frame to the buffer
  offscreenThree.endDraw() # we are done 'recording'

  # most likely, you'll want a black background to minimize
  # bleeding around your projection area
  background(0)
  
  if mov.time() == mov.duration():
    mov.jump(0)

  # render the scene, transformed using the corner pin surface
  surfaceOne.render(offscreenOne)
  surfaceTwo.render(offscreenTwo)
  surfaceThree.render(offscreenThree)
  # this is just for having the ellipse wander over the surfaces
  x += 1
  if x >= 800:
    x = 0

def keyPressed():
  global isPlaying
  if key == 'c':
    # enter/leave calibration mode, where surfaces can be warped 
    # and moved
    ks.toggleCalibration()
  elif key == 'l':
    # loads the saved layout
    ks.load()
  elif key == 's':
    # saves the layout
    ks.save()
  elif key == 'p':
    # play/pause the movie on keypress
    if isPlaying == False:
      mov.play()
      isPlaying = True
  else :
    mov.pause()
    isPlaying = False
    
def movieEvent(m):
  m.read()
