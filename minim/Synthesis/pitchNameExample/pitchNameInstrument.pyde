# The PitchNameInstrument is intended to play a tonal note
# at the pitch given by as a pitch name.

# Every instrument must implement the Instrument interface so 
# playNote() can call the instrument's methods.
class PitchNameInstrument implements Instrument
{
  # create all variables that must be used throughout the class
  Oscil sineOsc, lFOOsc
  ADSR  adsr
  
  # constructor for this instrument
  PitchNameInstrument( String note, amplitude )
 :
    # calculate the frequency frem the note name using the
    # Frequency class.
    frequency = Frequency.ofPitch( note ).asHz()

    # create instances of any UGen objects as necessary
    sineOsc = Oscil( frequency, amplitude, Waves.TRIANGLE )
    adsr = ADSR( 1.0, 0.01, 0.01, 1.0, 0.02 )

    # patch everything together up to the output
    sineOsc.patch( adsr )
  
 
  # every instrument must have a noteOn( ) method
  def noteOn( dur )
 :
    # patch the adsr all the way to the output 
    adsr.patch( out )
    # and turn it on
    adsr.noteOn()
  
  
  # every instrument must have a noteOff() method
  def noteOff()
 :
    # turn off adsr, which cause the release to begin
    adsr.noteOff()
    # after the release is over, unpatch from the out
    adsr.unpatchAfterRelease( out )
  


