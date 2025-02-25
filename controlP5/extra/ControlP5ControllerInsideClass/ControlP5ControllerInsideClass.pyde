add_library("controlP5.*

ControlP5 cp5
Test t
def setup() :
  size(400,400)
  cp5 = ControlP5( this )
  t = Test( "test" )


def draw() :
  background(20)
  println( t.value )


class Test :

  value

  Test( String thePrefix ) :
    cp5.addSlider( "value-"+thePrefix )
       .setRange( 0, 255 )
       .plugTo( this, "setValue" )
       .setValue( 127 )
       .setLabel("value")
       
  

  def setValue(theValue) :
    value = theValue
  


