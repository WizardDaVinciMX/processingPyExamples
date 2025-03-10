"""*
 * This sketch demonstrates very simply how you might use the inverse FFT to modify an audio signal.<br />
 * Press 'f' to perform the forward FFT, then press 's' to set one of the frequency bands to 150.<br />
 * Now press 'd' to take the inverse FFT. You will see that the wave form now looks like two sine waves that have
 * been added together. In fact, this is exactly the case. The sine wave that has been added has the 
 * same frequency as the frequency band that we artificially changed the value of.<br />
 * <br />
 * You might wonder what the actual frequency added to the spectrum is.
 * That frequency is a fraction of the sampling rate, which can be found with the formula <b>f = i/N</b>
 * where <b>f</b> is the fraction of the sampling rate, <b>i</b> is the index of the frequency band, 
 * and <b>N</b> is the time-domain size of the FFT. In this case we have a 512 poFFT and we are 
 * changing the frequency band at index 20. So in our case <b>f = 20/512 = 0.0390625</b>
 * Our sampling rate is 44100 Hz, a value passed in the Sine constructor,
 * so the frequency in Hz that is being added to the spectrum is <b>44100 * 0.0390625 = 1722.65625 Hz</b>
 * <p>
 * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
 """

add_library("ddf.minim.analysis.*
add_library("ddf.minim.signals.*

FFT fft
SineWave sine
float[] buffer
bsize = 512

def setup()
{
  size(512, 300, P3D)
  # create an FFT with a time-domain size the same as the size of buffer
  # it is required that these two values be the same
  # and also that the value is a power of two
  fft = FFT(bsize, 44100)
  sine = SineWave(600, 1, 44100)
  buffer = float[bsize]
  # fill the buffer with a sine wave
  sine.generate(buffer)


def draw()
{
  background(0)
  noStroke()
  fill(255, 128)
  # draw the waveform
  for(i = 0 i < buffer.length i+=1)
 :
    ellipse(i, 50 + buffer[i]*10, 2, 2)
  
  noFill()
  stroke(255)
  # draw the spectrum
  for(i = 0 i < fft.specSize() i+=1)
 :
    line(i, height, i, height - fft.getBand(i))
  
  stroke(255, 0, 0)
  line(width/2, height, width/2, 0)



def keyReleased()
{
  if ( key == 'f' ) 
 :
    println("Performing a Forward FFT on buffer.")
    fft.forward(buffer)
  
  if ( key == 'd' ) 
 :
    println("Performing an Inverse FFT and putting the result in buffer.")
    fft.inverse(buffer)
  
  if ( key == 's' )
 :
    # by setting frequency band 20 to a high value, we are basically mixing in a sine wave at that frequency
    # after setting the frequency band and then taking the inverse FFT, you will see the waveform change
    println("Setting frequency band 20 to 150.")
    fft.setBand(20, 150)
  

