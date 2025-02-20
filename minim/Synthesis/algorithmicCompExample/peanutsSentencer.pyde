# The PeanutsSentencer is intended to construct simulated speech sentences.
# To play the sentences, PeanutsSentencer calls playNote for each syllable
# which needs to be played

class PeanutsSentencer
{
  # create all variables that will need to be used throughout the class 
  startTime
  fundFreq
  balanceVal
  AudioOutput out
  Wavetable baseWave = Waves.saw(50)

  # create many constants which affect the sound of the syllables
  syllAmp = 0.6                      # amplitude
  syllFadeTime = 0.03                # fade time
  syllLenMin = 0.14                  # min length
  syllLenMax = 0.31                  # max length
  syllAmpModMin = 0.95               # min ampl 
  syllAmpModMax = 1.05               # max ampl 
  syllFreqModMin = 0.96              # min freq 
  syllFreqModMax = 1.02              # max freq 
  syllFadeTimeModMin = 0.90          # min fade time
  syllFadeTimeModMax = 1.10          # max fade time
  boolean lastSyllFixedFreqMod = true      # change freq of last syllable?
  questionChance = 0.14              # chance of a raised last syllable?
  float[] lastSyllFreqMod =: 0.89, 1.11  # amount to change last syllable
  boolean lastSyllLong = true              # last syllable always long?

  # this costructor only speficies the audioOutput.  everything else will be set later.
  PeanutsSentencer( AudioOutput out )
 :
    self.out = out
  
  
  # this constructor specifies the start time, fundamental freq, stereo position, and
  # audioOutput.
  PeanutsSentencer( startTime, fundFreq, balanceVal, AudioOutput out )
 :
    self.startTime = startTime
    self.fundFreq = fundFreq 
    self.balanceVal = balanceVal
    self.out = out
  
  
  # setParameters allows one to change the parameters for syllable generation.
  def setParameters ( startTime, fundFreq, balanceVal )
 :
    self.startTime = startTime
    self.fundFreq = fundFreq 
    self.balanceVal = balanceVal
  
  
  # saySentence actually generates the playNote calls for the sentence
  saySentence()
 :
    # the number of syllables will be an odd number between 3 and 13
    nSylls = 3 + 2*(int)( 6.0*(float)Math.random() )
    
    # create arrays to store all the lengths, ampls, freqs, and fade times
    syllLens[] = float[ nSylls ]
    syllAmps[] = float[ nSylls ]
    syllFreqs[] = float[ nSylls ]
    syllFadeTimes[] = float[ nSylls ]
    
    # generate all of the lengths, ampls, freqs, and fade times for the sentence
    for ( iSyll = 0 iSyll < nSylls iSyll+=1 )
   :
      syllLens[ iSyll ] = (float)Math.random()*( syllLenMax - syllLenMin ) + syllLenMin
      syllAmps[ iSyll ] = syllAmp*( (float)Math.random()*( syllAmpModMax - syllAmpModMin ) + syllAmpModMin )
      syllFreqs[ iSyll ] = fundFreq*
          ( (float)Math.random()*( syllFreqModMax - syllFreqModMin ) + syllFreqModMin )
      syllFadeTimes[ iSyll ] = syllFadeTime*
          ( (float)Math.random()*( syllFadeTimeModMax - syllFadeTimeModMin ) + syllFadeTimeModMin )      
    
    
    # set the freq of the last syllable if necessary
    if ( lastSyllFixedFreqMod )
   :
      iPhraseType = 0
      if ( Math.random() < questionChance )
     :
        iPhraseType = 1
      
      syllFreqs[ nSylls - 1 ] = fundFreq * lastSyllFreqMod[ iPhraseType ]
    
    
    # set the length of the last syllable if necessary
    if ( lastSyllLong )
   :
      syllLens[ nSylls - 1 ] = syllLenMax
    
 
    # because this is here, each sentence is guaranteed to have good timing
    out.pauseNotes()
    
    # make the appropriate calls to out.playNote()
    fadeLast = 0.0
    lenSum = 0.0
    for ( iSyll = 0 iSyll < nSylls iSyll+=1 )
   :
      thisStart = startTime + lenSum + fadeLast
      out.playNote( thisStart, syllLens[ iSyll ], 
          PeanutsSyllableInstrument( syllAmps[ iSyll ], syllFreqs[ iSyll ], 
              syllFadeTimes[ iSyll ], balanceVal, baseWave, out ) )
      lenSum += syllLens[ iSyll ] + fadeLast        
      fadeLast = syllFadeTimes[ iSyll ]
    
    # resume time for adding notes after each sentence
    out.resumeNotes()

    # return the length of this sentence
    return lenSum + fadeLast
  

