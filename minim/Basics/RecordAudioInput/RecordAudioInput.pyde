"""*
  * This sketch demonstrates how to an <code>AudioRecorder</code> to record audio to disk. 
  * To use this sketch you need to have something plugged into the line-in on your computer, 
  * or else be working on a laptop with an active built-in microphone. 
  * <p>
  * Press 'r' to toggle recording on and off and the press 's' to save to disk. 
  * The recorded file will be placed in the sketch folder of the sketch.
  * <p>
  * For more information about Minim and additional features, 
  * visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*

Minim minim
AudioInput in
AudioRecorder recorder

def setup()
{
  size(512, 200, P3D)
  
  minim = Minim(this)

  in = minim.getLineIn()
  # create a recorder that will record from the input to the filename specified
  # the file will be located in the sketch's root folder.
  recorder = minim.createRecorder(in, "myrecording.wav")
  
  textFont(createFont("Arial", 12))


def draw()
{
  background(0) 
  stroke(255)
  # draw the waveforms
  # the values returned by left.get() and right.get() will be between -1 and 1,
  # so we need to scale them up to see the waveform
  for(i = 0 i < in.bufferSize() - 1 i+=1)
 :
    line(i, 50 + in.left.get(i)*50, i+1, 50 + in.left.get(i+1)*50)
    line(i, 150 + in.right.get(i)*50, i+1, 150 + in.right.get(i+1)*50)
  
  
  if ( recorder.isRecording() )
 :
    text("Currently recording...", 5, 15)
  
  else
 :
    text("Not recording.", 5, 15)
  


def keyReleased()
{
  if ( key == 'r' ) 
 :
    # to indicate that you want to start or stop capturing audio data, you must call
    # beginRecord() and endRecord() on the AudioRecorder object. You can start and stop
    # as many times as you like, the audio data will be appended to the end of the buffer 
    # (in the case of buffered recording) or to the end of the file (in the case of streamed recording). 
    if ( recorder.isRecording() ) 
   :
      recorder.endRecord()
    
    else 
   :
      recorder.beginRecord()
    
  
  if ( key == 's' )
 :
    # we've filled the file out buffer, 
    # now write it to the file we specified in createRecorder
    # in the case of buffered recording, if the buffer is large, 
    # this will appear to freeze the sketch for sometime
    # in the case of streamed recording, 
    # it will not freeze as the data is already in the file and all that is being done
    # is closing the file.
    # the method returns the recorded audio as an AudioRecording, 
    # see the example  AudioRecorder >> RecordAndPlayback for more about that
    recorder.save()
    println("Done saving.")
  

