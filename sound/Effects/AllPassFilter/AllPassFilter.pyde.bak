add_library("sound")

def setup() :
  global saw
  global allPass

  size(512,360)
  background(255)
  
  # Create a sawtooth wave and an AllPass filter
  saw = SawOsc(this)
  saw.freq(200)
  allPass = AllPass(this)
  
  # Start the saw wave and push it through the allpass
  saw.play()
  allPass.process(saw)


def draw() :
  global saw
  global allPass

  background(0)
  
  # Set the drive of the allPass with the mouse
  g = map(mouseX, 0, width, 0., 1)
  allPass.gain(g)
  
  # Draw some visuals for intuition
  a = 50
  strokeWeight(4)
  for i in range(0, width, 3) :
    # Draw a wave
    stroke(255, 0, 0)
    point(i, sin(i) * a + width/2)
    # Draw that wave again after being driven by g
    stroke(0, 255, 0)
    point(i + g * TWO_PI, a * sin(i) + width/2)
  
