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
add_library('video')
add_library('keystone')

isPlaying = False

def setup() :
  global ks
  global surface
  global mov
  global isPlaying
  global offscreen

  # Keystone will only work with P3D or OPENGL renderers, 
  # since it relies on texture mapping to deform
  size(800, 600, P3D)

  ks =  Keystone(this) # init the keystoen object
  surface = ks.createCornerPinSurface(500, 500, 20) # create the surface
  mov =  Movie(this, "cube-inset-h264.mov" ) # load the video
  mov.frameRate(25) # set the framerate
  # We need an offscreen buffer to draw the surface we
  # want projected
  # note that we're matching the resolution of the
  # CornerPinSurface.
  # (The offscreen buffer can be P2D or P3D)
  offscreen = createGraphics(500, 500, P3D)
  mov.play()# we need to start the movie once
  mov.jump(0)# go to the first frame
  mov.pause() # and hold it until we hit p


def draw() :
  global isPlaying
  # Draw the scene, offscreen
  offscreen.beginDraw() # start writing into the buffer
  offscreen.background(255)
  offscreen.image(mov, 0, 0) # <-- here we add the current frame to the buffer
  offscreen.endDraw() # we are done 'recording'

  # most likely, you'll want a black background to minimize
  # bleeding around your projection area
  background(0)
  # this is for resetting the video after it was played. 
  if mov.time() == mov.duration():
    mov.jump(0)
  
  surface.render(offscreen)# add everything to the surface


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
