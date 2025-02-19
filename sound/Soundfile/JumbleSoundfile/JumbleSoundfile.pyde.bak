"""*
 * First load a sample sound file from disk, then start manipulating it using the
 * low-level data access functions provided by AudioSample.
 * With every mouseclick, two random 1 second chunks of the sample are swapped around
 * in their position. The sample always stays the same length and it keeps on looping,
 * but the more often you do random swaps, the more the original soundfile gets cut up
 * into smaller and smaller portions that seem to be resampled at random.
 """

add_library("sound")


def setup():
  global file

  size(640, 360)
  background(255)

  # Load a soundfile and start playing it on loop
  file = SoundFile(this, "beat.aiff")
  file.loop()
      


def draw():
  pass

def mousePressed() :
  global file

  # Every time the mouse is pressed, take two random 1 second chunks of the sample
  # and swap them around.

  partOneStart = int(random(file.frames()))
  partTwoOffset = int(random(file.frames() - file.sampleRate()))
  # Offset part two by at least one second
  partTwoStart = partOneStart + file.sampleRate() + partTwoOffset
  # Make sure the start of the second sample part is not past the end of the file.
  partTwoStart = partTwoStart % file.frames()

  # Read one second worth of frames from each position
  partOne = [0.0] * file.sampleRate()
  partTwo = [0.0] * file.sampleRate()
  file.read(partOneStart, partOne, 0, len(partOne))
  file.read(partTwoStart, partTwo, 0, len(partTwo))
  # And write them back the other way around
  file.write(partOneStart, partTwo, 0, len(partTwo))
  file.write(partTwoStart, partOne, 0, len(partOne))
