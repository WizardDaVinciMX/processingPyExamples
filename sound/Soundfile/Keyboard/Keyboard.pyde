"""*
 * This example shows how to make a simple keyboard-triggered sampler with the Sound
 * library. In this sketch 5 different short samples are loaded and played back at
 * different speeds, which also changes their perceived pitch by one or two octaves.
 """

add_library("sound")

# Define the number of samples 
numsounds = 5

# Define a variable to store the randomly generated background color in
backgroundColor = [255, 255, 255]

def setup():
  global file

  size(640, 360)

  # Create a Sound renderer and an array of empty soundfiles
  file = [0] * numsounds

  # Load 5 soundfiles from a folder in a for loop. By naming
  # the files 1.aif, 2.aif, 3.aif, ..., n.aif it is easy to iterate
  # through the folder and load all files in one line of code.
  for i in range(0, numsounds):
    file[i] = SoundFile(this, str(i+1) + ".aif")
  


def draw() :
  background(backgroundColor[0], backgroundColor[1], backgroundColor[2])


def keyPressed() :
  # We use a boolean helper variable to determine whether one of the branches
  # of the switch-statement was activated or not
  validKey = True

  if key == 'a':
    file[0].play(0.5, 1.0)
  elif key == 's':
    file[1].play(0.5, 1.0)
  elif key == 'd':
    file[2].play(0.5, 1.0)
  elif key == 'f':
    file[3].play(0.5, 1.0)
  elif key == 'g':
    file[4].play(0.5, 1.0)
  elif key == 'h':
    file[0].play(1.0, 1.0)
  elif key == 'j':
    file[1].play(1.0, 1.0)
  elif key == 'k':
    file[2].play(1.0, 1.0)
  elif key == 'l':
    file[3].play(1.0, 1.0)
  elif key == '':
    file[4].play(1.0, 1.0)
  elif key == '\'':
    file[0].play(2.0, 1.0)
  elif key == 'q':
    file[1].play(2.0, 1.0)
  elif key == 'w':
    file[2].play(2.0, 1.0)
  elif key == 'e':
    file[3].play(2.0, 1.0)
  elif key == 'r':
    file[4].play(2.0, 1.0)
  elif key == 't':
    file[0].play(3.0, 1.0)
  elif key == 'y':
    file[1].play(3.0, 1.0)
  elif key == 'u':
    file[2].play(3.0, 1.0)
  elif key == 'i':
    file[3].play(3.0, 1.0)
  elif key == 'o':
    file[4].play(3.0, 1.0)
  elif key == 'p':
    file[0].play(4.0, 1.0)
  elif key == '[':
    file[1].play(4.0, 1.0)
    # no valid key was pressed, store that information
  else:
    validKey = False
  

  # If a sample playback was triggered, change the background color
  if validKey:
    for i in range(0, 3):
      backgroundColor[i] = int(random(255))
    
  
