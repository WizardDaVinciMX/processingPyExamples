"""*
 * This example shows how to make a simple sampler and sequencer with the Sound library.
 * Five different samples are loaded and played back at different pitches, in this
 * case 5 different octaves. The sequencer randomly triggers an event every
 * 200-1000 mSecs. Each time a sound is played a colored rect with a random color is
 * displayed.
 """

add_library("sound")

# Define the number of samples 
numsounds = 5

# Create an array of values which represent the octaves. 1.0 is playback at normal speed, 0.5 is half and 
# therefore one octave down. 2.0 is double so one octave up.
octave = [0.25, 0.5, 1.0, 2.0, 4.0]

# The playSound array is defining how many samples will be played at each trigger event
playSound = [1, 1, 1, 1, 1]

# The trigger is an integer number in milliseconds so we can schedule events in the draw loop
trigger = 0

# This array holds the pixel positions of the rectangles which are drawn each event
posx = [0, 128, 256, 384, 512]


def setup():
  global file
  global trigger

  size(640, 360)
  background(255)

  # Create an array of empty soundfiles
  file = [0]* numsounds

  # Load 5 soundfiles from a folder in a for loop. By naming the files 1., 2., 3., n.aif it is easy to iterate
  # through the folder and load all files in one line of code.
  for i in range(0, numsounds):
    file[i] = SoundFile(this, str(i+1) + ".aif")
  

  # Create a trigger which will be the basis for our random sequencer. 
  trigger = millis()


def draw() :
  global millis
  global trigger

  # If the determined trigger moment in time matches up with the computer clock events get triggered.
  if millis() > trigger:
    # Redraw the background every time to erase old rects
    background(255)

    # By iterating through the playSound array we check for 1 or 0, 1 plays a sound and draws a rect,
    # for 0 nothing happens.

    for i in range(0, numsounds):      
      # Check which indexes are 1 and 0.
      if playSound[i] == 1:
        # Choose a random color and get set to noStroke()
        fill(int(random(255)), int(random(255)), int(random(255)))
        noStroke()
        # Draw the rect in the positions we defined earlier in posx
        rect(posx[i], 50, 128, 260)
        # Choose a random index of the octave array
        rate = octave[int(random(0, 5))]
        # Play the soundfile from the array with the respective rate and loop set to false
        file[i].play(rate, 1.0)
      

      # Rethe indexes of playSound so that at the next event the order is different and randomized.
      playSound[i] = int(random(0, 2))
    

    # Create a triggertime in the future, with a random offset between 200 and 1000 milliseconds
    trigger = millis() + int(random(200, 1000))
  
