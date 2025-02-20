# The SlideInstrument is intended to slide between two pitches
# specified in frequency.  This only plays out of one channel
# (ostensibly the rightt ).

# Every instrument must implement the Instrument interface so 
# playNote() can call the instrument's methods.
class SlideInstrument implements Instrument
{
  # create all variables that must be used throughout the class
  Multiplier  gate
  Line  freqControl
  
  # constructor for this instrument
  SlideInstrument(begFreq, endFreq, amp)
 :
    # create instances of the UGens necessary
    gate = Multiplier( 0 )
    Oscil tone = Oscil( begFreq, amp, Waves.TRIANGLE )
    freqControl = Line( 1.0, begFreq, endFreq )
    Balance right = Balance( 1 )

    # and patch everything together up to the final output
    freqControl.patch( tone.frequency )
    tone.patch( right ).patch( gate )
  
  
  # every instrument must have a noteOn( ) method
  def noteOn( dur )
 :
    # set the time for the line with the duration of the note
    freqControl.setLineTime( dur )
    # activate the line
    freqControl.activate()
    # set the gate on
    gate.setValue( 1 )
    # and patch it to the output
    gate.patch( out )
  
  
  # every instrument must have a noteOff() method
  def noteOff()
 :
    # turn off the gain
    gate.setValue( 0 )
    # and unpatch the output 
    # this causes the entire instrument to stop calculating sampleframes
    # which is good when the instrument is no longer generating sound.
    gate.unpatch( out )
  


