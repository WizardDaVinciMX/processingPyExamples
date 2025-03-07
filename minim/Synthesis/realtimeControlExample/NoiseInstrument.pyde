# Every instrument must implement the Instrument interface so 
# playNote() can call the instrument's methods.

# This noise instrument uses white noise and two bandpass filters
# to make a "whistling wind" sound.  By changing using the methods which
# change the frequency and the bandwidth of the filters, the sound changes.

class NoiseInstrument implements Instrument
{
  # create all variables that must be used throughout the class
  Noise myNoise
  Multiplier multiply
  AudioOutput out
  BandPass filt1, filt2
  Summer sum 
  freq1, freq2, freq3
  bandWidth1, bandWidth2
  filterFactor
  
  # constructors for this intsrument
  NoiseInstrument( amplitude, AudioOutput output )
 :
    # equate class variables to constructor variables as necessary 
    out = output
    
    # give some initial values to the realtime control variables
    freq1 = 150.0
    bandWidth1 = 10.0
    filterFactor = 1.7
    
    # create instances of any UGen objects
    myNoise = Noise( amplitude, Noise.Tint.WHITE )
    multiply = Multiplier( 0 )
    filt1 = BandPass( freq1, bandWidth1, out.sampleRate() )
    filt2 = BandPass( freq2(), bandWidth2(), out.sampleRate() )
    sum = Summer()

    # patch everything (including the out this time)
    myNoise.patch( filt1 ).patch( sum )
    myNoise.patch( filt2 ).patch( sum )
    sum.patch( multiply )
  
  
  # every instrument must have a noteOn( ) method
  def noteOn( dur )
 :
    # set the multiply to 1 to turn on the note
    multiply.setValue( 1 )
    multiply.patch( out )
  
  
  # every instrument must have a noteOff() method
  def noteOff()
 :
    # set the multiply to 0 to turn off the note 
    multiply.setValue( 0 )
    multiply.unpatch( out )
  
  
  # this is a helper method only used internally to find the second filter
  freq2()
 :
    # calculate the second frequency based on the first
    return filterFactor*freq1
  
  
  # this is a helper method only used internally 
  # to find the bandwidth of the second filter
  bandWidth2()
 :
    # calculate the second bandwidth based on the first
    return filterFactor*bandWidth1
  
  
  # this is a method to set the center frequencies
  # of the two filters based on the CF of the first
  def setFilterCF( cf )
 :
    freq1 = cf
    filt1.setFreq( freq1 )
    filt2.setFreq( freq2() )
  
  
  # this is a method to set the bandwidths
  # of the two filters based on the BW of the first
  def setFilterBW( bw )
 :
    bandWidth1 = bw
    filt1.setBandWidth( bandWidth1 )
    filt2.setBandWidth( bandWidth2() )
  
 
  # this is a method to set the Q (inverse of bandwidth)
  # of the two filters based on the  
  def setFilterQ( q )
 :
    setFilterBW( freq1/q )
  

