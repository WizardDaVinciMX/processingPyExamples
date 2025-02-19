"""
 * oscP5broadcaster by andreas schlegel
 * an osc broadcast server.
 * osc clients can connect to the server by sending a connect and
 * disconnect osc message as defined below to the server.
 * incoming messages at the server will then be broadcasted to
 * all connected clients. 
 * an example for a client is located in the oscP5broadcastClient exmaple.
 * oscP5 website at http:#www.sojamo.de/oscP5
"""
 
add_library("oscP5")
#add_library("netP5.*

myNetAddressList = NetAddressList()

# listeningPort is the port the server is listening for incoming messages
myListeningPort = 32000
# the broadcast port is the port the clients should listen for incoming messages from the server
myBroadcastPort = 12000

myConnectPattern = "/server/connect"
myDisconnectPattern = "/server/disconnect"

def setup():
  global oscP5

  oscP5 = OscP5(this, myListeningPort)
  frameRate(25)


def draw():
  background(0)


def oscEvent(theOscMessage):
  # check if the address pattern fits any of our patterns
  if   theOscMessage.addrPattern().equals(myConnectPattern):
    connect(theOscMessage.netAddress().address())
  elif theOscMessage.addrPattern().equals(myDisconnectPattern):
    disconnect(theOscMessage.netAddress().address())
  # * if pattern matching was not successful, then broadcast the incoming
  # * message to all addresses in the netAddresList.
  else:
    oscP5.send(theOscMessage, myNetAddressList)


def connect(theIPaddress):
  if !myNetAddressList.contains(theIPaddress, myBroadcastPort):
    myNetAddressList.add(NetAddress(theIPaddress, myBroadcastPort))
    println("0x0x0x adding "+theIPaddress+" to the list.")
  else:
    println("0x0x0x "+theIPaddress+" is already connected.")
     
    println("0x0x0x currently there are "+myNetAddressList.list().size()+" remote locations connected.")


def disconnect(theIPaddress):
  if myNetAddressList.contains(theIPaddress, myBroadcastPort):
    myNetAddressList.remove(theIPaddress, myBroadcastPort)
    println("0x0x0x removing "+theIPaddress+" from the list.")
  else:
    println("0x0x0x "+theIPaddress+" is not connected.")
     
  println("0x0x0x currently there are "+myNetAddressList.list().size())
 
