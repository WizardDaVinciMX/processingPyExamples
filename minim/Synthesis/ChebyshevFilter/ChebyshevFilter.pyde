"""*
 * This sketch demonstrates how to use a Chebyshev Filter. A Chebyshev Filter is used to 
 * separate one band of frequencies from another. It can either be a Low Pass filter or 
 * a High Pass filter. This type, along with three other attributes are used to determine 
 * the coefficients used for processing a signal. The other three attributes are the cutoff frequency, 
 * the passband ripple percentage, and the number of poles.
 * <p>
 * The cutoff frequency is the frequency that defines the breakpobetween the filter's passband
 * and stopband. If the ChebFilter is set to be a low pass filter and the cutoff frequency is 500 Hz, 
 * Then all frequencies in a signal below 500 Hz will be allowed through the filter and the frequencies 
 * above 500 Hz will removed. So 0 to 500 Hz is the passband and 500 Hz to one-half of the sampling rate 
 * (22050 Hz if you are sampling at 44100 Hz, which is typical) is the stopband.
 * <p>
 * The passband ripple percentage is how much "ripple" there is in the passband. The thing to know is that 
 * a higher ripple percentage results in a faster transition between the passband and the stopband. However, 
 * large ripple can distort the signal somewhat.
 * <p>
 * The number of poles refer to the poles of an IIR, or recursive, digital filter. The thing to know is 
 * that a larger number of poles usually makes for a better filter. The ChebFilter has some limitations 
 * on the number of poles used. The number of poles must be even and between 2 and 20.
 * The filter will report an error if either of those conditions are not met. However, it should also be 
 * mentioned that depending on the current cutoff frequency of the filter, the 
 * number of poles that will result in a <i>stable</i> filter, can be as few as 4.
 * The filter will not report an error in the case of the number of requested 
 * poles resulting in an unstable filter. Generally, you probably won't need to use more than 6 poles. 
 * For reference, here is a table of the maximum number of poles possible according to cutoff frequency:
 * <p>
 * <table>
 *   <tr>
 *     <td>Cutoff Frequency<br />(expressed as a fraction of the sampling rate)</td>
 *     <td>0.02</td>
 *     <td>0.05</td>
 *     <td>0.10</td>
 *     <td>0.25</td>
 *     <td>0.40</td>
 *     <td>0.45</td>
 *     <td>0.48</td>
 *   </tr>
 *   <tr>
 *     <td>Maximum poles</td>
 *     <td>4</td>
 *     <td>6</td>
 *     <td>10</td>
 *     <td>20</td>
 *     <td>10</td>
 *     <td>6</td>
 *     <td>4</td>
 *   </tr>
 * </table> 
 * <p>
 * For more information about Minim and additional features, visit http:#code.compartmental.net/minim/
 """

add_library("ddf.minim.*
add_library("ddf.minim.effects.*
add_library("ddf.minim.ugens.*

Minim minim
AudioOutput output
FilePlayer groove
ChebFilter cbf

cutoffFreq = 4410
ripplePercent = 2

ArrayList<PolesButton> buttons = ArrayList<PolesButton>()
ArrayList<Knob> knobs = ArrayList<Knob>()

def setup()
{
  size(512, 512, P3D)
  
  minim = Minim(this)
  output = minim.getLineOut()
  groove = FilePlayer( minim.loadFileStream("groove.mp3") )
  # make a two pole low pass filter with a cutoff frequency of 4410 Hz and a ripple percentages of 2%
  # the final argument is the sample rate of audio that will be filetered
  # it is required to correctly compute values used by the filter
  cbf = ChebFilter(cutoffFreq, ChebFilter.LP, ripplePercent, 2, output.sampleRate())
  cbf.printCoeff()
  groove.patch( cbf ).patch( output )
  
  groove.loop()
  
  textAlign(LEFT, TOP)
  
  buttonX = 4*width/6
  buttonY = 200
  buttonSpacing = 20
  buttons.add( PolesButton("two", buttonX, buttonY, 2) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("four", buttonX, buttonY, 4) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("six", buttonX, buttonY, 6) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("eight", buttonX, buttonY, 8) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("ten", buttonX, buttonY, 10) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("twelve", buttonX, buttonY, 12) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("fourteen", buttonX, buttonY, 14) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("sixteen", buttonX, buttonY, 16) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("eighteen", buttonX, buttonY, 18) )
  buttonY += buttonSpacing
  buttons.add( PolesButton("twenty", buttonX, buttonY, 20) )
  
  knobs.add( Knob("cutoff", 50, 250, cutoffFreq, 200, 21000) )
  knobs.add( Knob("ripple", 150, 250, ripplePercent, 1, 20) )


def draw()
{
  if ( cbf.frequency() != cutoffFreq ) cbf.setFreq(cutoffFreq)
  if ( cbf.getRipple() != ripplePercent ) cbf.setRipple(ripplePercent)
  
  background(0)
  
  for(i = 0 i < buttons.size() +=1i)
 :
    buttons.get(i).draw()
  
  
  for(i = 0 i < knobs.size() +=1i)
 :
    knobs.get(i).draw()
  
  
  stroke(255)
  # draw the waveforms
  # the values returned by left.get() and right.get() will be between -1 and 1,
  # so we need to scale them up to see the waveform
  for(i = 0 i < output.bufferSize() - 1 i+=1)
 :
    x1 = map(i, 0, output.bufferSize(), 0, width)
    x2 = map(i+1, 0, output.bufferSize(), 0, width)
    line(x1, 50 - output.left.get(i)*50, x2, 50 - output.left.get(i+1)*50)
    line(x1, 150 - output.right.get(i)*50, x2, 150 - output.right.get(i+1)*50)
  


def knobTwiddled(String knobName, newValue)
{
  #println(knobName + ": " + newValue)
  if ( knobName == "cutoff" )
 :
    cutoffFreq = newValue
  
  else if ( knobName == "ripple" )
 :
    ripplePercent = newValue
  


def mousePressed()
{
  for(i = 0 i < buttons.size() +=1i)
 :
    buttons.get(i).mousePressed()
  
  
  for(i = 0 i < knobs.size() +=1i)
 :
    knobs.get(i).mousePressed()
  


def mouseDragged()
{
  for(i = 0 i < knobs.size() +=1i)
 :
    knobs.get(i).mouseMoved()
  


def mouseReleased()
{
  for(i = 0 i < knobs.size() +=1i)
 :
    knobs.get(i).mouseReleased()
  


class PolesButton 
{
  String label
  x, y, w, h
  numPoles
  
  public PolesButton(String _label, _x, _y, _poles)
 :
    label = _label
    x = _x
    y = _y
    w = 65
    h = 15
    numPoles = _poles
  
  
  public def draw()
 :
    if ( cbf.getPoles() == numPoles )
   :
      stroke(255)
      fill( 0, 128, 0 )
    
    else
   :
      noStroke()
      fill( 128 )
    
    
    rect(x,y,w,h)
    
    fill( 255 )
    textAlign(LEFT, TOP)
    text( label, x+5, y )
  
  
  public def mousePressed()
 :
    if( mouseX >= x && mouseX <= x+w && mouseY >= y && mouseY <= y+h )
   :
      if ( cbf.getPoles() != numPoles )
     :
        cbf.setPoles(numPoles)
      
    
  


class Knob
{
  String label
  x, y, r
  min, max
  pct
  
  public Knob(String _label, _x, _y, initialValue, _min, _max)
 :
    label = _label
    x = _x
    y = _y
    r = 25
    min = _min
    max = _max
    pct = map(initialValue, min, max, 0, 1)
  
  
  public def draw()
 :
    stroke(255)
    fill(128)
    ellipseMode(RADIUS)
    ellipse(x,y,r,r)
    
    angle = radians(lerp(360-35, 35, pct))
    line(x, y, x+sin(angle)*r, y+cos(angle)*r)
    
    textAlign(CENTER, TOP)
    text(label, x, y+r+5)
  
  
  boolean trackMouse
  
  public def mousePressed()
 :
    if ( dist(x,y,mouseX,mouseY) < r )
   :
      trackMouse = true
    
  
  
  public def mouseReleased()
 :
    trackMouse = false
  
  
  public def mouseMoved()
 :
    if ( trackMouse )
   :
      delta = pmouseY - mouseY
      pct = constrain(pct + delta * 0.01f, 0, 1)
      knobTwiddled(label, lerp(min, max, pct))
    
  
