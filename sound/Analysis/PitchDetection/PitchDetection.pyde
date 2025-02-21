"""*
 * This sketch shows how to use the PitchDetector class to detect the pitch 
 * (also known as the 'fundamental frequency') of a sound signal. For complex 
 * signals this is not a trivial task, so the analyzer not only returns the pitch 
 * (measured in Hertz, or 'Hz') but also a 'confidence level' in that measurement.
 """

add_library("sound")

i = 0

def setup() :
  global pitchDetector
  global i

  size(640, 320)
  background(0)

  pitchDetector = PitchDetector(this)
  # capture audio input
  pitchDetector.input(AudioIn(this, 3))


def draw() :
  global pitchDetector
  global i

  # clear column
  noStroke()
  fill(color(0))
  rect(i, 0, 1, height)

  # the array version of analyze() returns the detected pitch as well
  # as the confidence level in the correctness of that pitch
  pitchAndConfidence = [0, 0]
  pitchDetector.analyze(pitchAndConfidence)

  # don't draw measurements when there is absolutely 0 confidence in them
  if pitchAndConfidence[1] > 0 :
    # draw all others: map the range of a human whistle (~40 - 2000Hz) to the height
    # of the sketch, and color the dot according to the confidence in this measurement
    fill(lerpColor(color(255, 0, 0), color(0, 255, 0), pitchAndConfidence[1]))

    circle(i, int(map(pitchAndConfidence[0], 2000, 40, 0, height)), 2)
  

  i = (i+1) % width
