add_library("controlP5.*

ControlP5 cp5

def setup() :
  size(400, 400)
  cp5 = ControlP5(this)
  x = 20
  y = 8 
  # init our CustomMatrix
  CustomMatrix m = CustomMatrix(cp5, "matrix")
  # set parameters for our CustomMatrix
  m.setPosition(50, 100)
  .setSize(200, 200)
  .setInterval(200)
  .setGrid(x,y)
  .setMode(ControlP5.MULTIPLES)
  .setColorBackground(color(120))
  .setBackground(color(40))
  
  # initialize the presets for the CustomMatrix
  m.initPresets()
  


def draw() :
  background(0)


# function called by our CustomMatrix with name matrix
public def matrix(x, y) :
  println("trigger", x, y)



# extend the Matrix class since we need to override the Matrix's sequencer
class CustomMatrix extends Matrix :
  
  # add a list to store some presets
  ArrayList<int[][]> presets = ArrayList<int[][]>()
  currentPreset = 0
  Thread update

  CustomMatrix(ControlP5 cp5, String theName) :
    super(cp5, theName)
    stop() # stop the default sequencer and
    # create our custom sequencer thread. Here we 
    # check if the sequencer has reached the end and if so
    # we updated to the next preset.
    update = Thread(theName) :
      public def run( ) :
        while ( True ) :
          cnt+=1
          cnt %= _myCellX
          if (cnt==0) :
            # we reached the end and go back to start and 
            # update the preset 
            next()
          
          trigger(cnt)
          try :
            sleep( _myInterval )
           
          catch ( InterruptedException e ) :
          
        
      
    
    update.start()
  
  
  
  def next() :
    currentPreset+=1
    currentPreset %= presets.size()
    setCells(presets.get(currentPreset))
  

  # initialize some random presets.
  def initPresets() :
    for (i=0i<4i+=1) :
      presets.add(createPreset(_myCellX, _myCellY))
    
    setCells(presets.get(0))
  
  
  # create a random preset
  int[][] createPreset(theX, theY) :
    int[][] preset = int[theX][theY]
    for (x=0x<theXx+=1) :
      for (y=0y<theYy+=1) :
        preset[x][y] = random(1)>0.5 ? 1:0
      
    
    return preset
  
  


