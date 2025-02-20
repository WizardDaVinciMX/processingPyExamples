"""*
  * This sketch demonstrates two ways to accomplish offline (non-realtime) analysis of an audio file.<br>
  * The first method, which uses an AudioSample, is what you see running.<br>
  * The second method, which uses an AudioRecordingStream and is only available in Minim Beta 2.1.0 and beyond,<br>
  * can be viewed by looking at the offlineAnalysis.pde file.
  * <p>
  * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
  *
  """

add_library("ddf.minim.*
add_library("ddf.minim.analysis.*
add_library("ddf.minim.spi.*

Minim minim
float[][] spectra

def setup()
{
  size(512, 400, P3D)

  minim = Minim(this)
  
  # There are two ways you can do offline analysis:
  # 1. Loading audio data fully into memory using an AudioSample and then analyzing a channel
  analyzeUsingAudioSample()
  
  # 2. Loading an AudioRecordingStream and reading in a buffer at a time.
  #    This second option is available starting with Minim Beta 2.1.0
  #analyzeUsingAudioRecordingStream()


def analyzeUsingAudioSample()
{
   AudioSample jingle = minim.loadSample("jingle.mp3", 2048)
   
  # get the left channel of the audio as a array
  # getChannel is defined in the interface BuffereAudio, 
  # which also defines two constants to use as an argument
  # BufferedAudio.LEFT and BufferedAudio.RIGHT
  float[] leftChannel = jingle.getChannel(AudioSample.LEFT)
  
  # then we create an array we'll copy sample data into for the FFT object
  # this should be as large as you want your FFT to be. generally speaking, 1024 is probably fine.
  fftSize = 1024
  float[] fftSamples = float[fftSize]
  FFT fft = FFT( fftSize, jingle.sampleRate() )
  
  # now we'll analyze the samples in chunks
  totalChunks = (leftChannel.length / fftSize) + 1
  
  # allocate a 2-dimentional array that will hold all of the spectrum data for all of the chunks.
  # the second dimension if fftSize/2 because the spectrum size is always half the number of samples analyzed.
  spectra = float[totalChunks][fftSize/2]
  
  for(chunkIdx = 0 chunkIdx < totalChunks +=1chunkIdx)
 :
    chunkStartIndex = chunkIdx * fftSize
   
    # the chunk size will always be fftSize, except for the 
    # last chunk, which will be however many samples are left in source
    chunkSize = min( leftChannel.length - chunkStartIndex, fftSize )
   
    # copy first chunk into our analysis array
    System.arraycopy( leftChannel, # source of the copy
               chunkStartIndex, # index to start in the source
               fftSamples, # destination of the copy
               0, # index to copy to
               chunkSize # how many samples to copy
              )
      
    # if the chunk was smaller than the fftSize, we need to pad the analysis buffer with zeroes        
    if ( chunkSize < fftSize )
   :
      # we use a system call for this
      java.util.Arrays.fill( fftSamples, chunkSize, fftSamples.length - 1, 0.0 )
    
    
    # now analyze this buffer
    fft.forward( fftSamples )
   
    # and copy the resulting spectrum into our spectra array
    for(i = 0 i < 512 +=1i)
   :
      spectra[chunkIdx][i] = fft.getBand(i)
    
  
  
  jingle.close() 


def analyzeUsingAudioRecordingStream()
{
  fftSize = 1024
  AudioRecordingStream stream = minim.loadFileStream("jingle.mp3", fftSize, false)
  
  # tell it to "play" so we can read from it.
  stream.play()
  
  # create the fft we'll use for analysis
  FFT fft = FFT( fftSize, stream.getFormat().getSampleRate() )
  
  # create the buffer we use for reading from the stream
  MultiChannelBuffer buffer = MultiChannelBuffer(fftSize, stream.getFormat().getChannels())
  
  # figure out how many samples are in the stream so we can allocate the correct number of spectra
  totalSamples = int( (stream.getMillisecondLength() / 1000.0) * stream.getFormat().getSampleRate() )
  
  # now we'll analyze the samples in chunks
  totalChunks = (totalSamples / fftSize) + 1
  println("Analyzing " + totalSamples + " samples for total of " + totalChunks + " chunks.")
  
  # allocate a 2-dimentional array that will hold all of the spectrum data for all of the chunks.
  # the second dimension if fftSize/2 because the spectrum size is always half the number of samples analyzed.
  spectra = float[totalChunks][fftSize/2]
  
  for(chunkIdx = 0 chunkIdx < totalChunks +=1chunkIdx)
 :
    println("Chunk " + chunkIdx)
    println("  Reading...")
    stream.read( buffer )
    println("  Analyzing...")    
  
    # now analyze the left channel
    fft.forward( buffer.getChannel(0) )
    
    # and copy the resulting spectrum into our spectra array
    println("  Copying...")
    for(i = 0 i < 512 +=1i)
   :
      spectra[chunkIdx][i] = fft.getBand(i)
    
  


# how many units to step per second
cameraStep = 100
# our current z position for the camera
cameraPos = 0
# how far apart the spectra are so we can loop the camera back
spectraSpacing = 50

def draw()
{
  dt = 1.0 / frameRate
  
  cameraPos += cameraStep * dt
  
  # jump back to start position when we get to the end
  if ( cameraPos > spectra.length * spectraSpacing )
 :
    cameraPos = 0
  
  
  background(0)
  
  camNear = cameraPos - 200
  camFar  = cameraPos + 2000
  camFadeStart = lerp(camNear, camFar, 0.4f)
  
  # render the spectra going back into the screen
  for(s = 0 s < spectra.length s+=1)
 :
    z = s * spectraSpacing
    # don't draw spectra that are behind the camera or too far away
    if ( z > camNear && z < camFar )
   :
      fade = z < camFadeStart ? 1 : map(z, camFadeStart, camFar, 1, 0)
      stroke(255*fade)
      for(i = 0 i < spectra[s].length-1 +=1i )
     :
        line(-256 + i, spectra[s][i]*25, z, -256 + i + 1, spectra[s][i+1]*25, z)
      
    
  
  
  camera( 200, 100, -200 + cameraPos, 75, 50, cameraPos, 0, -1, 0 )
