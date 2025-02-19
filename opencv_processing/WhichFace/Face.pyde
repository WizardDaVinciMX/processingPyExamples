"""*
 * Which Face Is Which
 * Daniel Shiffman
 * http:#shiffman.net/2011/04/26/opencv-matching-faces-over-time/
 *
 * Modified by Jordi Tost (call the constructor specifying an ID)
 * @updated: 01/10/2014
 """

class Face:
  
  # A Rectangle
  Rectangle r
  
  # Am I available to be matched?
  boolean available
  
  # Should I be deleted?
  boolean delete
  
  # How long should I live if I have disappeared?
  timer = 127
  
  # Assign a number to each face
  id
  
  # Make me
  Face(newID, x, y, w, h):
    r = Rectangle(x,y,w,h)
    available = true
    delete = false
    id = newID
  

  # Show me
  def display():
    fill(0,0,255,timer)
    stroke(0,0,255)
    rect(r.x,r.y,r.width, r.height)
    #rect(r.x*scl,r.y*scl,r.width*scl, r.height*scl)
    fill(255,timer*2)
    text(""+id,r.x+10,r.y+30)
    #text(""+id,r.x*scl+10,r.y*scl+30)
    #text(""+id,r.x*scl+10,r.y*scl+30)
  

  # Give me a location / size
  # Oooh, it would be nice to lerp here!
  def update(Rectangle newR):
    r = (Rectangle) newR.clone()
  

  # Count me down, I am gone
  def countDown():
    timer--
  

  # I am deed, delete me
  boolean dead():
    if (timer < 0) return true
    return false
  

