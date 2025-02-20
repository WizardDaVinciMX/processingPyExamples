#add_library("opengl")


"""
  This sketch is a more involved use of AudioSamples to create a simple drum machine. 
  Click on the buttons to toggle them on and off. The buttons that are on will trigger 
  samples when the beat marker passes over their column. You can change the tempo by 
  clicking in the BPM box and dragging the mouse up and down.
  <p>
  We achieve the timing by using AudioOutput's playNote method and a cleverly written Instrument.
  <p>
  For more information about Minim and additional features, 
  visit http:#code.compartmental.net/minim/
"""

add_library("minim")
#add_library("ddf.minim.ugens.*

minim = None
out = None

kick = None
snare = None
hat = None

hatRow = [False] * 16
snrRow = [False] * 16
kikRow = [False] * 16

buttons = list()

bpm = 120

beat = 0  # which beat we're on

# here's an Instrument implementation that we use 
# to trigger Samplers every sixteenth note. 
# Notice how we get away with using only one instance
# of this class to have endless beat making by 
# having the class schedule itself to be played
# at the end of its noteOff method. 
class Tick(Instrument):
  def noteOn(self, dur ):
    global hatRow
    global snrRow
    global kikRow
    global snare

    if hatRow[beat]:
        hat.trigger()
    if snrRow[beat]:
        snare.trigger()
    if kikRow[beat]:
        kick.trigger()

  def noteOff(self):
    global beat

    # next beat
    beat = (beat+1)%16
    # set the tempo
    out.setTempo( bpm )
    # play this again right now, with a sixteenth note duration
    out.playNote( 0, 0.25, self)

# simple class for drawing the gui
class Rect:
  def __init__(self, _x, _y, _steps, _id):
    self.x = _x
    self.y = _y
    self.w = 14
    self.h = 30
    self.steps = _steps
    self.stepId = _id

  def draw(self):
    if self.steps[self.stepId]:
      fill(0,255,0)
    else:
      fill(255,0,0)

    rect(self.x, self.y, self.w, self.h)
    
  def mousePressed(self):
    if mouseX >= self.x and \
        mouseX <= self.x + self.w and \
        mouseY >= self.y and \
        mouseY <= self.y + self.h :
      self.steps[self.stepId] = not self.steps[self.stepId]

def setup():
  global minim
  global out
  global buttons
  global kick
  global snare
  global hat

  size(395, 200)
  minim = Minim(this)
  out   = minim.getLineOut()
  
  # load all of our samples, using 4 voices for each.
  # this will help ensure we have enough voices to handle even
  # very fast tempos.
  kick  = Sampler( "BD.wav", 4, minim )
  snare = Sampler( "SD.wav", 4, minim )
  hat   = Sampler( "CHH.wav", 4, minim )
  
  # patch samplers to the output
  kick.patch( out )
  snare.patch( out )
  hat.patch( out )
  
  for i in range(0, 16):
    buttons.append( Rect(10+i*24, 50, hatRow, i ) )
    buttons.append( Rect(10+i*24, 100, snrRow, i ) )
    buttons.append( Rect(10+i*24, 150, kikRow, i ) )

  beat = 0
  
  # start the sequencer
  out.setTempo( bpm )
  out.playNote( 0, 0.25, Tick() )

def draw():
  global buttons
  global beat

  background(0)
  fill(255)
  #text(frameRate, width - 60, 20)
  
  for i in range(0, len(buttons)):
    buttons[i].draw()

  stroke(128)
  if beat % 4 == 0:
    fill(200, 0, 0)
  else:
    fill(0, 200, 0)

  # beat marker    
  rect(10+beat*24, 35, 14, 9)

def mousePressed():
  for i in range(0, len(buttons)):
    buttons[i].mousePressed()
