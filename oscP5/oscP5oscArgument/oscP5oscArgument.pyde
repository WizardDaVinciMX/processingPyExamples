"""
 * oscP5oscArgument by andreas schlegel
 * example shows how to parse incoming osc messages "by hand".
 * it is recommended to take a look at oscP5plug for an alternative way to parse messages.
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
  myRemoteLocation = NetAddress("127.0.0.1",12000)
  # send an OSC message to this sketch
  oscP5.send("/test", [int("1"), float(2.0), "test string."], myRemoteLocation)


def draw():
  background(0)  


def oscEvent(theOscMessage):
  # check if theOscMessage has the address pattern we are looking for.
  if theOscMessage.checkAddrPattern("/test"):
    # check if the typetag is the right one.
    if theOscMessage.checkTypetag("ifs"):
      # parse theOscMessage and extract the values from the osc message arguments.
      firstValue = theOscMessage.get(0).intValue()  # get the first osc argument
      secondValue = theOscMessage.get(1).floatValue() # get the second osc argument
      thirdValue = theOscMessage.get(2).stringValue() # get the third osc argument
      print("0x0x0x received an osc message /test with typetag ifs.")
      println(" values: " + firstValue+", " + secondValue+", " + thirdValue)
      return
    
  
  println("0x0x0x received an osc message. with address pattern " +
          theOscMessage.addrPattern()+" typetag "+ theOscMessage.typetag())
