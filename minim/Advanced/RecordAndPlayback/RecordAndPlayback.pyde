"""
  This sketch demonstrates how to use an AudioRecorder to record audio to disk
  and then immediately play it back by creating a FilePlayer using the AudioRecordingStream
  returned by the save method.
  <p> 
  To use this sketch you need to have something plugged into the line-in on your computer.<br/>
  Press 'r' to toggle recording on and off and the press 's' to save to disk.<br/>
  The recorded file will be placed in the main folder of the sketch.
  <p>
  For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
"""

add_library("minim")
#add_library("ddf.minim.ugens.*

minim = None

# for recording
inp = None
recorder = None
recorded = False

# for playing back
out = None
player = None

def setup():
  global inp
  global recorder

  size(512, 200, P3D)

  minim = Minim(this)
  
  # get a stereo line-in: sample buffer length of 2048
  # default sample rate is 44100, default bit depth is 16
  inp = minim.getLineIn(Minim.STEREO, 2048)
  
  # create an AudioRecorder that will record from in to the filename specified.
  # the file will be located in the sketch's main folder.
  recorder = minim.createRecorder(inp, "myrecording.wav")
  
  # get an output we can playback the recording on
  out = minim.getLineOut( Minim.STEREO )
  
  textFont(createFont("Arial", 12))


def draw():
  global inp
  global out
  global recorder

  background(0) 
  stroke(255)
  # draw the waveforms
  # the values returned by left.get() and right.get() will be between -1 and 1,
  # so we need to scale them up to see the waveform
  for i in range(0, inp.left.size()-1):
    line(i, 50 + inp.left.get(i)*50, i+1, 50 + inp.left.get(i+1)*50)
    line(i, 150 + inp.right.get(i)*50, i+1, 150 + inp.right.get(i+1)*50)

  if recorder.isRecording():
    text("Now recording, press the r key to stop recording.", 5, 15)
  elif not recorded:
    text("Press the r key to start recording.", 5, 15)
  else:
    text("Press the s key to save the recording to disk and play it back in the sketch.", 5, 15)

def keyReleased():
  global recorded
  global recorder
  global player

  if not recorded and key == 'r':
    # to indicate that you want to start or stop capturing audio data, 
    # you must callstartRecording() and stopRecording() on the AudioRecorder object. 
    # You can start and stop as many times as you like, the audio data will 
    # be appended to the end of to the end of the file. 
    if recorder.isRecording():
      recorder.endRecord()
      recorded = True
    else:
      recorder.beginRecord()

  if recorded and key == 's':
    # we've filled the file out buffer, 
    # now write it to a file of the type we specified in setup
    # in the case of buffered recording, 
    # this will appear to freeze the sketch for sometime, if the buffer is large
    # in the case of streamed recording, 
    # it will not freeze as the data is already in the file and all that is being done
    # is closing the file.
    # save returns the recorded audio in an AudioRecordingStream, 
    # which we can then play with a FilePlayer
    if player != None:
        player.unpatch( out )
        player.close()
    
    player = FilePlayer( recorder.save() )
    player.patch( out )
    player.play()
  
