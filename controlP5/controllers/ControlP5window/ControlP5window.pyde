"""*
 * ControlP5 ControlWindow
 * by andreas schlegel, 2012
 """

add_library("controlP5.*

ControlP5 cp5

myColorBackground = color(0, 0, 0)

ControlWindow controlWindow

public sliderValue = 40

def setup() :
  size(700, 400)  

  cp5 = ControlP5(this)


# PLEASE READ
# 
# With controlP5 2.0 the ControlWindow has been removed, 
# please see the changelog.txt for details. 
# Instead, see the extra/ControlP5frame example for 
# a ControlWindow alternative.











#  controlWindow = cp5.addControlWindow("controlP5window", 100, 100, 400, 200)
#    .hideCoordinates()
#    .setBackground(color(40))
#    

  cp5.addSlider("sliderValue")
     .setRange(0, 255)
     .setPosition(40, 40)
     .setSize(200, 29)
     #.moveTo(controlWindow)
     



def draw() :
  background(sliderValue)


def myTextfield(String theValue) :
  println(theValue)


def myWindowTextfield(String theValue) :
  println("from controlWindow: "+theValue)


def keyPressed() :
  # if (key==',') cp5.window("controlP5window").hide()
  # if (key=='.') cp5.window("controlP5window").show()
  # controlWindow = controlP5.addControlWindow("controlP5window2",600,100,400,200)
  # controlP5.controller("sliderValue1").moveTo(controlWindow)

  # if (key=='d') :
  #   if (controlWindow.isUndecorated()) :
  #     controlWindow.setUndecorated(False)
  #    else :
  #     controlWindow.setUndecorated(True)
  #   
  # 
  # if (key=='t') :
  #   controlWindow.toggleUndecorated()
  # 


