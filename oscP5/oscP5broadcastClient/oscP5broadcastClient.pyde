"""
 oscP5broadcastClient by andreas schlegel
 an osc broadcast client.
 an example for broadcast server is located in the oscP5broadcaster exmaple.
 oscP5 website at http:#www.sojamo.de/oscP5
"""

add_library("oscP5")
#add_library("netP5")


def setup():
  global oscP5

  # a NetAddress contains the ip address and port number of a remote location in the network.
  global myBroadcastLocation 

  size(400,400)
  frameRate(25)
  
  """ 
   create a instance of oscP5. 
   12000 is the port number you are listening for incoming osc messages.
   """
  oscP5 = OscP5(this, 12000)
  
  """ 
   create a NetAddress. a NetAddress is used when sending osc messages
   with the oscP5.send method.
  """
  
  """ 
    the address of the osc broadcast server
  """
  myBroadcastLocation = NetAddress("127.0.0.1",32000)



def draw():
  background(0)



def mousePressed():
  # create a OscMessage with an address pattern, in this case /test.
  myOscMessage = OscMessage("/test")
  # add a value (an integer) to the OscMessage
  myOscMessage.add(100)
  # send the OscMessage to a remote location specified in myNetAddress
  oscP5.send(myOscMessage, myBroadcastLocation)


def keyPressed():
  global m

  if   key == 'c':
      # connect to the broadcaster
      m = OscMessage("/server/connect", [0])
      oscP5.flush(m,myBroadcastLocation)
  elif key == 'd':
      # disconnect from the broadcaster
      m = OscMessage("/server/disconnect", [0])
      oscP5.flush(m,myBroadcastLocation)


# incoming osc message are forwarded to the oscEvent method.
def oscEvent(theOscMessage):
  # get and prthe address pattern and the typetag of the received OscMessage """
  println("0x0x0x received an osc message with addrpattern "+theOscMessage.addrPattern()+" and typetag "+theOscMessage.typetag())
  theOscMessage.print()
