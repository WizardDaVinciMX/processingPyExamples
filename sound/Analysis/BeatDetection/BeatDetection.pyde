"""*
 * BeatDetection
 * by Alex Miller
 *
 * This sketch shows how to use the BeatDetector class to detect spikes
 * in sound energy that correspond to rhythmic beats. Change the sensitivity
 * value to adjust how much dampening the algorithm uses (higher values
 * make the algorithm less sensitive).
 *
 * This sketch also draws a debug view which renders the underlying energy
 * levels computed by the beat detection algorithm.
 """

add_library("sound")

def setup() :
  global sample
  global beatDetector
 
  size(400, 200)
  background(255)

  sample = SoundFile(this, "drums.wav")
  sample.loop()
  
  beatDetector = BeatDetector(this)
  beatDetector.input(sample)
  
  # The sensitivity determines how long the detector will wait after detecting
  # a beat to detect the next one.
  beatDetector.sensitivity(140)


def draw() :
  background(0)

  # Draw debug graph in the background
  drawDebug()

  # If a beat is currently detected, light up the indicator
  if (beatDetector.isBeat()) :
    fill(255)
  else :
    fill(0)
  
  
  stroke(255)
  strokeWeight(1)
  rect(20, 20, 15, 15)
  
  fill(255)
  textAlign(LEFT, TOP)
  text("BEAT DETECTED", 40, 20)


def drawDebug() :
  stroke(255)
  strokeWeight(2)  
  energyBuffer = beatDetector.getEnergyBuffer()
  cursor = beatDetector.getEnergyCursor()
  last = energyBuffer[cursor] / 100 * height
  spacing = width / (len(energyBuffer) - 1)
  for j in range(1, len(energyBuffer)) :
    index = (j + cursor) % len(energyBuffer) 
    energy = energyBuffer[index] / 100 * height
    line((j - 1) * spacing, height - last * 1, j * spacing, height - energy)
    last = energy
  

  beatBuffer = beatDetector.getBeatBuffer()
  for j in range(1, len(beatBuffer)) :
    index = (j + cursor) % len(energyBuffer)
    beat = beatBuffer[index]
    if (beat) :
      stroke(255, 255, 0)
      line(j * spacing, 0, j * spacing, height)
    
  
