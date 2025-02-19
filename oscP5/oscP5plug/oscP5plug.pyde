"""
 oscP5plug by andreas schlegel
 example shows how to use the plug service with oscP5.
 the concept of the plug service is, that you can
 register methods in your sketch to which incoming 
 osc messages will be forwareded automatically without 
 having to parse them in the oscEvent method.
 that a look at the example below to get an understanding
 of how plug works.
 oscP5 website at http:#www.sojamo.de/oscP5
"""

add_library("oscP5")
#add_library("netP5.*


def setup():
  global oscP5
  global myRemoteLocation

  size(400,400)
  frameRate(25)
  #start oscP5, listening for incoming messages at port 12000
  oscP5 = OscP5(this,12000)
  
  # myRemoteLocation is a NetAddress. a NetAddress takes 2 parameters,
  # an ip address and a port number. myRemoteLocation is used as parameter in
  # oscP5.send() when sending osc packets to another computer, device, 
  # application. usage see below. for testing purposes the listening port
  # and the port of the remote location address are the same, hence you will
  # send messages back to this sketch.
  myRemoteLocation = NetAddress("127.0.0.1",12000)
  
  # osc plug service
  # osc messages with a specific address pattern can be automatically
  # forwarded to a specific method of an object. in this example 
  # a message with address pattern /test will be forwarded to a method
  # test(). below the method test takes 2 arguments - 2 ints. therefore each
  # message with address pattern /test and typetag ii will be forwarded to
  # the method test(theA, theB)
  oscP5.plug(this,"test","/test")


def test(theA, theB):
  println("0x0x0x plug event method. received a message /test.")
  println(" 2 ints received: "+theA+", "+theB)  


def draw():
  background(0)


def mousePressed():
  # create an osc message with address pattern /test
  myMessage = OscMessage("/test")
  
  myMessage.add(123) # add an to the osc message
  myMessage.add(456) # add a second to the osc message

  # send the message
  oscP5.send(myMessage, myRemoteLocation) 


# incoming osc message are forwarded to the oscEvent method.
def oscEvent(theOscMessage):
  # with theOscMessage.isPlugged() you check if the osc message has already been
  # forwarded to a plugged method. if theOscMessage.isPlugged()==true, it has already 
  # been forwared to another method in your sketch. theOscMessage.isPlugged() can 
  # be used for double posting but is not required.
  #  
  if theOscMessage.isPlugged():
    # print the address pattern and the typetag of the received OscMessage
    println("0x0x0x received an osc message.")
    println("0x0x0x addrpattern\t" + theOscMessage.addrPattern())
    println("0x0x0x typetag\t" + theOscMessage.typetag())
