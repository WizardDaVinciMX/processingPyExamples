"""
 oscP5sendreceive by andreas schlegel
 example shows how to send and receive osc messages.
 oscP5 website at http:#www.sojamo.de/oscP5
"""
 
add_library("oscP5")
#add_library("netP5.*
  

def setup():
  global oscP5
  global myRemoteLocation

  size(400,400)
  frameRate(25)
  # start oscP5, listening for incoming messages at port 12000
  oscP5 = OscP5(this,12000)
  
  # myRemoteLocation is a NetAddress. a NetAddress takes 2 parameters,
  # an ip address and a port number. myRemoteLocation is used as parameter in
  # oscP5.send() when sending osc packets to another computer, device, 
  # application. usage see below. for testing purposes the listening port
  # and the port of the remote location address are the same, hence you will
  # send messages back to this sketch.
  myRemoteLocation = NetAddress("127.0.0.1",12000)


def draw():
  background(0)  


def mousePressed():
  # in the following different ways of creating osc messages are shown by example
  myMessage = OscMessage("/test")
  
  myMessage.add(123) # add an to the osc message

  # send the message
  oscP5.send(myMessage, myRemoteLocation) 



# incoming osc message are forwarded to the oscEvent method.
def oscEvent(theOscMessage):
  # print the address pattern and the typetag of the received OscMessage
  print("0x0x0x received an osc message.")
  print(" addrpattern: "  +theOscMessage.addrPattern())
  println(" typetag: " + theOscMessage.typetag())
