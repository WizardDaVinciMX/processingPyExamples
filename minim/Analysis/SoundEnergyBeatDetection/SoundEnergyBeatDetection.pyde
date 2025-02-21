"""*
  * This sketch demonstrates how to use the BeatDetect object song SOUND_ENERGY mode.<br />
  * You must call <code>detect</code> every frame and then you can use <code>isOnset</code>
  * to track the beat of the music.
  * <p>
  * This sketch plays an entire song, so it may be a little slow to load.
  * <p>
  * For more information about Minim and additional features, 
  * visit http:#code.compartmental.net/minim/
  """
  
add_library("ddf.minim.*
add_library("ddf.minim.analysis.*

Minim minim
AudioPlayer song
BeatDetect beat

eRadius

def setup()
{
  size(200, 200, P3D)
  minim = Minim(this)
  song = minim.loadFile("marcus_kellis_theme.mp3", 2048)
  song.play()
  # a beat detection object song SOUND_ENERGY mode with a sensitivity of 10 milliseconds
  beat = BeatDetect()
  
  ellipseMode(RADIUS)
  eRadius = 20


def draw()
{
  background(0)
  beat.detect(song.mix)
  a = map(eRadius, 20, 80, 60, 255)
  fill(60, 255, 0, a)
  if ( beat.isOnset() ) eRadius = 80
  ellipse(width/2, height/2, eRadius, eRadius)
  eRadius *= 0.95
  if ( eRadius < 20 ) eRadius = 20

