"""
 oscP5tcp by andreas schlegel
 example shows how to use the TCP protocol with oscP5.
 what is TCP? http:#en.wikipedia.org/wiki/Transmission_Control_Protocol
 in this example both, a server and a client are used. typically 
 this doesnt make sense as you usually wouldnt communicate with yourself
 over a network. therefore this example is only to make it easier to 
 explain the concept of using tcp with oscP5.
 oscP5 website at http:#www.sojamo.de/oscP5
"""

add_library("oscP5")
#add_library("netP5.*


def setup():
  global oscP5tcpServer
  global oscP5tcpClient
  global myServerAddress

  # create  an oscP5 instance using TCP listening @ port 11000
  oscP5tcpServer = OscP5(this, 11000, OscP5.TCP)
  
  # create an oscP5 instance using TCP. 
  # the remote address is 127.0.0.1 @ port 11000 = the server from above
  oscP5tcpClient = OscP5(this, "127.0.0.1", 11000, OscP5.TCP)


def draw():
  background(0)  


def mousePressed():
  # the tcp client sends a message to the server it is connected to.
  oscP5tcpClient.send("/test", [int(1)])


def keyPressed():
  # check how many clients are connected to the server.
  println(oscP5tcpServer.tcpServer().getClients().length)


def oscEvent(theMessage):
  # in this example, both the server and the client share this oscEvent method
  System.out.println("0x0x0x got a message " + theMessage)
  if theMessage.checkAddrPattern("/test"):
    # message was send from the tcp client
    m = OscMessage("/response")
    m.add("server response: got it")
    # server responds to the client's message
    oscP5tcpServer.send(m,theMessage.tcpConnection())
