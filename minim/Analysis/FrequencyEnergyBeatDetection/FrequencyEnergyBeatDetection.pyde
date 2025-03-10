"""*
  * This sketch demonstrates how to use the BeatDetect object in FREQ_ENERGY mode.<br />
  * You can use <code>isKick</code>, <code>isSnare</code>, </code>isHat</code>, <code>isRange</code>, 
  * and <code>isOnset(int)</code> to track whatever kind of beats you are looking to track, they will report 
  * true or false based on the state of the analysis. To "tick" the analysis you must call <code>detect</code> 
  * with successive buffers of audio. You can do this inside of <code>draw</code>, but you are likely to miss some 
  * audio buffers if you do self. The sketch implements an <code>AudioListener</code> called <code>BeatListener</code> 
  * so that it can call <code>detect</code> on every buffer of audio processed by the system without repeating a buffer 
  * or missing one.
  * <p>
  * This sketch plays an entire song so it may be a little slow to load.
  * <p>
  * For more information about Minim and additional features, 
  * visit http:#code.compartmental.net/minim/
  """

add_library("ddf.minim.*
add_library("ddf.minim.analysis.*

Minim minim
AudioPlayer song
BeatDetect beat
BeatListener bl

kickSize, snareSize, hatSize

class BeatListener implements AudioListener
{
  private BeatDetect beat
  private AudioPlayer source
  
  BeatListener(BeatDetect beat, AudioPlayer source)
 :
    self.source = source
    self.source.addListener(this)
    self.beat = beat
  
  
  def samples(float[] samps)
 :
    beat.detect(source.mix)
  
  
  def samples(float[] sampsL, float[] sampsR)
 :
    beat.detect(source.mix)
  


def setup()
{
  size(512, 200, P3D)
  
  minim = Minim(this)
  
  song = minim.loadFile("marcus_kellis_theme.mp3", 1024)
  song.play()
  # a beat detection object that is FREQ_ENERGY mode that 
  # expects buffers the length of song's buffer size
  # and samples captured at songs's sample rate
  beat = BeatDetect(song.bufferSize(), song.sampleRate())
  # set the sensitivity to 300 milliseconds
  # After a beat has been detected, the algorithm will wait for 300 milliseconds 
  # before allowing another beat to be reported. You can use this to dampen the 
  # algorithm if it is giving too many false-positives. The default value is 10, 
  # which is essentially no damping. If you try to set the sensitivity to a negative value, 
  # an error will be reported and it will be set to 10 instead. 
  # note that what sensitivity you choose will depend a lot on what kind of audio 
  # you are analyzing. in this example, we use the same BeatDetect object for 
  # detecting kick, snare, and hat, but that this sensitivity is not especially great
  # for detecting snare reliably (though it's also possible that the range of frequencies
  # used by the isSnare method are not appropriate for the song).
  beat.setSensitivity(300)  
  kickSize = snareSize = hatSize = 16
  # make a beat listener, so that we won't miss any buffers for the analysis
  bl = BeatListener(beat, song)  
  textFont(createFont("Helvetica", 16))
  textAlign(CENTER)


def draw()
{
  background(0)
  
  # draw a green rectangle for every detect band
  # that had an onset this frame
  rectW = width / beat.detectSize()
  for(i = 0 i < beat.detectSize() +=1i)
 :
    # test one frequency band for an onset
    if ( beat.isOnset(i) )
   :
      fill(0,200,0)
      rect( i*rectW, 0, rectW, height)
    
  
  
  # draw an orange rectangle over the bands in 
  # the range we are querying
  lowBand = 5
  highBand = 15
  # at least this many bands must have an onset 
  # for isRange to return true
  numberOfOnsetsThreshold = 4
  if ( beat.isRange(lowBand, highBand, numberOfOnsetsThreshold) )
 :
    fill(232,179,2,200)
    rect(rectW*lowBand, 0, (highBand-lowBand)*rectW, height)
  
  
  if ( beat.isKick() ) kickSize = 32
  if ( beat.isSnare() ) snareSize = 32
  if ( beat.isHat() ) hatSize = 32
  
  fill(255)
    
  textSize(kickSize)
  text("KICK", width/4, height/2)
  
  textSize(snareSize)
  text("SNARE", width/2, height/2)
  
  textSize(hatSize)
  text("HAT", 3*width/4, height/2)
  
  kickSize = constrain(kickSize * 0.95, 16, 32)
  snareSize = constrain(snareSize * 0.95, 16, 32)
  hatSize = constrain(hatSize * 0.95, 16, 32)
