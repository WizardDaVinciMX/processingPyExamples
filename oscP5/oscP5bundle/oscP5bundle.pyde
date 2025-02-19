"""
 * oscP5bundle by andreas schlegel
 * an osc broadcast server.
 * example shows how to create and send osc bundles. 
 * oscP5 website at http:#www.sojamo.de/oscP5
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
  # * an ip address and a port number. myRemoteLocation is used as parameter in
  # * oscP5.send() when sending osc packets to another computer, device, 
  # * application. usage see below. for testing purposes the listening port
  # * and the port of the remote location address are the same, hence you will
  # * send messages back to this sketch.
  myRemoteLocation = NetAddress("127.0.0.1", 12000)


def draw():
  background(0)  


def mousePressed():
  # create an osc bundle
  myBundle = OscBundle()
  
  # create a osc message object
  myMessage = OscMessage("/test")
  myMessage.add("abc")
  
  #add an osc message to the osc bundle
  myBundle.add(myMessage)
  
  # reset and clear the myMessage object for refill.
  myMessage.clear()
  
  # refill the osc message object again
  myMessage.setAddrPattern("/test2")
  myMessage.add("defg")
  myBundle.add(myMessage)
  
  myBundle.setTimetag(myBundle.now() + 10000)
  # send the osc bundle, containing 2 osc messages, to a remote location.
  oscP5.send(myBundle, myRemoteLocation)



# incoming osc message are forwarded to the oscEvent method.
def oscEvent(theOscMessage):
  # print the address pattern and the typetag of the received OscMessage
  print("0x0x0x received an osc message.")
  print(" addrpattern: "+theOscMessage.addrPattern())
  print(" typetag: "+theOscMessage.typetag())
  println(" timetag: "+theOscMessage.timetag())
