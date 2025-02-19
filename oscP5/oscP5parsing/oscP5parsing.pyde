"""
 * oscP5parsing by andreas schlegel
 * example shows how to parse incoming osc messages "by hand".
 * it is recommended to take a look at oscP5plug for an
 * alternative and more convenient way to parse messages.
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
  # an ip address and a port number. myRemoteLocation is used as parameter in
  # oscP5.send() when sending osc packets to another computer, device, 
  # application. usage see below. for testing purposes the listening port
  # and the port of the remote location address are the same, hence you will
  # send messages back to this sketch.
  myRemoteLocation = NetAddress("127.0.0.1", 12000)


def draw():
  background(0)  


def mousePressed():
  # create a osc message object
  myMessage = OscMessage("/test")
  
  myMessage.add(123) # add an to the osc message
  myMessage.add(12.34) # add a to the osc message
  myMessage.add("some text") # add a string to the osc message

  # send the message 
  oscP5.send(myMessage, myRemoteLocation) 


def oscEvent(theOscMessage):
  # check if theOscMessage has the address pattern we are looking for.
  
  if theOscMessage.checkAddrPattern("/test"):
    # check if the typetag is the right one.
    if theOscMessage.checkTypetag("ifs"):
      # parse theOscMessage and extract the values from the osc message arguments.
      firstValue = theOscMessage.get(0).intValue()  
      secondValue = theOscMessage.get(1).floatValue()
      thirdValue = theOscMessage.get(2).stringValue()
      print("0x0x0x received an osc message /test with typetag ifs.")
      println(" values: "+firstValue+", "+secondValue+", "+thirdValue)
      return
      
   
  println("0x0x0x received an osc message. with address pattern " + theOscMessage.addrPattern())
