"""
 Which Face Is Which
 Daniel Shiffman
 http:#shiffman.net/2011/04/26/opencv-matching-faces-over-time/

 Modified by Jordi Tost (call the constructor specifying an ID)
 updated: 01/10/2014
"""
from java.awt import Rectangle

class Face:
  # Make me
  def __init__(self, newID, x, y, w, h):
    self.r = Rectangle(x,y,w,h)
    self.available = True
    self.delete = False
    self.id = newID
    # Am I available to be matched?
    self.available = False
    
    # How long should I live if I have disappeared?
    self.timer = 127

  # Show me
  def display(self):
    fill(0,0,255,self.timer)
    stroke(0,0,255)
    rect(self.r.x, self.r.y, self.r.width, self.r.height)
    #rect(r.x*scl,r.y*scl,r.width*scl, r.height*scl)
    fill(255, self.timer * 2)
    text("" + str(self.id), self.r.x + 10, self.r.y + 30)
    #text(""+id,r.x*scl+10,r.y*scl+30)
    #text(""+id,r.x*scl+10,r.y*scl+30)


  # Give me a location / size
  # Oooh, it would be nice to lerp here!
  def update(self, newR):
    self.r = newR.clone()

  # Count me down, I am gone
  def countDown(self):
    self.timer-= 1


  # I am deed, delete me
  def dead(self):
    if self.timer < 0:
     return True
    return False
