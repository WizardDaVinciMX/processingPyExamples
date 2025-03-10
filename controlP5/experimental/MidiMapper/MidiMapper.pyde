

"""*
 * ControlP5 MidiMapper
 * 
 * Maps midi input to controlP5 controllers. 
 * This will eventually result in a library. 
 *
 * by Andreas Schlegel, 2013
 * www.sojamo.de/libraries/controlp5
 *
 """
 
add_library("java.util.HashMap
add_library("java.util.Map
add_library("controlP5.*
add_library("javax.sound.midi.Receiver
add_library("javax.sound.midi.MidiMessage

ControlP5 cp5

Map<String, String> midimapper = HashMap<String, String>()

def setup() :

  size( 600, 400 )
  
  cp5 = ControlP5( this )

  cp5.begin(cp5.addTab("a"))
  cp5.addSlider("a-1").setPosition(20, 120).setSize(200, 20)
  cp5.addSlider("a-2").setPosition(20, 160).setSize(200, 20)
  cp5.addSlider("a-3").setPosition(20, 200).setSize(200, 20)
  cp5.addToggle("a-4").setPosition(280, 120).setSize(100, 20)
  cp5.addButton("a-5").setPosition(280, 160).setSize(100, 20)
  cp5.addBang("a-6").setPosition(280, 200).setSize(100, 20)
  cp5.end()
  
  cp5.begin(cp5.addTab("b"))
  cp5.addSlider("b-1").setPosition(20, 120).setSize(200, 20)
  cp5.addSlider("b-2").setPosition(20, 160).setSize(200, 20)
  cp5.addSlider("b-3").setPosition(20, 200).setSize(200, 20)
  cp5.end()
  
  final String device = "SLIDER/KNOB"
  
  #midimapper.clear()
  
  midimapper.put( ref( device, 0 ), "a-1" )
  midimapper.put( ref( device, 1 ), "a-2" )
  midimapper.put( ref( device, 2 ), "a-3" )
  midimapper.put( ref( device, 32 ), "a-4" )
  midimapper.put( ref( device, 48 ), "a-5" )
  midimapper.put( ref( device, 64 ), "a-6" )

  midimapper.put( ref( device, 16 ), "b-1" )
  midimapper.put( ref( device, 17 ), "b-2" )
  midimapper.put( ref( device, 18 ), "b-3" )

  boolean DEBUG = False

  if (DEBUG) :
    MidiSimple( device )
   
  else :
    MidiSimple( device , Receiver() :

      @Override public def send( MidiMessage msg, long timeStamp ) :

        byte[] b = msg.getMessage()

        if ( b[ 0 ] != -48 ) :

          Object index = ( midimapper.get( ref( device , b[ 1 ] ) ) )

          if ( index != None ) :

            Controller c = cp5.getController(index.toString())
            if (c instanceof Slider ) :  
              min = c.getMin()
              max = c.getMax()
              c.setValue(map(b[ 2 ], 0, 127, min, max) )
              else if ( c instanceof Button ) :
              if ( b[ 2 ] > 0 ) :
                c.setValue( c.getValue( ) )
                c.setColorBackground( 0xff08a2cf )
               else :
                c.setColorBackground( 0xff003652 )
              
             else if ( c instanceof Bang ) :
              if ( b[ 2 ] > 0 ) :
                c.setValue( c.getValue( ) )
                c.setColorForeground( 0xff08a2cf )
               else :
                c.setColorForeground( 0xff00698c )
              
             else if ( c instanceof Toggle ) :
              if ( b[ 2 ] > 0 ) :
                ( ( Toggle ) c ).toggle( )
              
            
          
        
      

      @Override public def close( ) :
      
    
    )
  



String ref(String theDevice, theIndex) :
  return theDevice+"-"+theIndex



def draw() :
  background( 0 )



