# This NumberInstrument just plays a single sine wave, but takes in an integer to
# be able to prwhich instrument it is.  Just for giggles, it also prints the
# frequency and amplitude of the note as it starts.

# Every instrument must implement the Instrument interface so 
# playNote() can call the instrument's methods.
class NumberInstrument implements Instrument
{
  # create all variables that must be used throughout the class
  Oscil sineOsc, lFOOsc
  Multiplier  multiply
  AudioOutput out
  iNote
  amp
  freq
  
  # constructor for this instrument
  NumberInstrument(frequency, amplitude, iN, AudioOutput output)
 :
    # equate class variables to constructor variables as necessary
    out = output
    iNote = iN
    amp = amplitude
    freq = frequency
    
    # create instances of any UGen objects as necessary
    sineOsc = Oscil(frequency, amplitude, Waves.SINE)
    multiply = Multiplier(0)

    # patch everything together up to the final output
    sineOsc.patch(multiply)
  
  
  # every instrument must have a noteOn( ) method
  def noteOn(dur)
 :
    # want to prinformation about this instrument
    println("Instron number " + iNote + "   amp = " + amp + "   freq = " + freq )
    # turn on the gain
    multiply.setValue(1.0)
    # and patch to the output
    multiply.patch(out)
  
  
  # every instrument must have a noteOff method
  def noteOff()
 :
    # prthat we're turning this off
    println("Instroff number " + iNote )
    # turn the gain to 0
    multiply.setValue(0)
    # and unpatch it
    multiply.unpatch( out )
  

