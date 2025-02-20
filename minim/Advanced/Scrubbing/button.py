class Button(object):
  def __init__(self, s, x, y, hw, hh):
    self.song = s
    self.x = x
    self.y = y
    self.hw = hw
    self.hh = hh

  def pressed(self):
    return mouseX > self.x - self.hw and \
           mouseX < self.x + self.hw and \
           mouseY > self.y - self.hh and \
           mouseY < self.y + self.hh

  def mousePressed(self):
      pass

  def mouseReleased(self):
      pass

  def update(self):
      pass

  def draw(self):
      pass

class Play(Button):  
  def __init__(self, s, x, y, hw, hh): 
    super(Play, self).__init__(s, x, y, hw, hh)
    self.play = True
    self.invert = False
  
  # code to handle playing and pausing the file
  def mousePressed(self):
    if self.pressed():
      self.invert = True
      if self.song.isPlaying():
        self.song.pause()
        play = True
      else:
        self.song.loop()
        play = False

  def mouseReleased(self):
    self.invert = False

  # play is a boolean value used to determine what to draw on the button
  def update(self):
    if self.song.isPlaying():
        self.play = False
    else:
        self.play = True
  
  def draw(self):
    if self.invert:
      fill(255)
      stroke(0)
    else:
      noFill()
      stroke(255)
    
    rect(self.x - self.hw, self.y - self.hh, self.hw*2, self.hh*2)
    if self.invert:
      fill(0)
      stroke(255)    
    else:
      fill(255)
      noStroke()

    if self.play:
      triangle(self.x - self.hw/3, \
               self.y - self.hh/2, \
               self.x - self.hw/3, \
               self.y + self.hh/2, \
               self.x + self.hw/2, \
               self.y)
    else:
      rect(self.x - self.hw/3, \
           self.y - self.hh/2, \
           self.hw/4, \
           self.hh)
      rect(self.x + self.hw/8, \
           self.y - self.hh/2, \
           self.hw/4, \
           self.hh)

class Rewind(Button):  
  def __init__(self, s, x, y, hw, hh):
    super(Rewind, self).__init__(s, x, y, hw, hh)
    self.invert = False

  # code used to scrub backward in the file
  def update(self):
    # if the rewind button is currently being pressed
    if self.pressed():
      # get the current song position
      pos = self.song.position()
      # if it greater than 200 milliseconds
      if pos > 200:
        # rewind the song by 200 milliseconds
        self.song.skip(-200)      
      else:
        # if the song hasn't played more than 100 milliseconds
        # just rewind to the beginning
        self.song.rewind()

  def mousePressed(self):
    if self.pressed():
      self.invert = True
      # if the song isn't currently playing, rewind it to the beginning
      if not self.song.isPlaying():
        self.song.rewind()      

  def mouseReleased(self):
    self.invert = False

  def draw(self):
    if self.invert:
      fill(255)
      stroke(0)    
    else:
      noFill()
      stroke(255)

    rect(self.x - self.hw, \
         self.y - self.hh, \
         self.hw*2, \
         self.hh*2)
    if self.invert:
      fill(0)
      stroke(255)
    else:
      fill(255)
      noStroke()
    
    triangle(self.x - self.hw/2, \
             self.y, \
             self.x, \
             self.y - self.hh/2, \
             self.x, \
             self.y + self.hh/2)
    triangle(self.x, \
             self.y, \
             self.x + self.hw/2, \
             self.y - self.hh/2, \
             self.x + self.hw/2, \
             self.y + self.hh/2)    

class Forward(Button):  
  def __init__(self, s, x, y, hw, hh):
    super(Forward, self).__init__(s, x, y, hw, hh)
    self.invert = False
  
  def update(self):
    # if the forward button is currently being pressed
    if self.pressed():
      # get the current position of the song
      pos = self.song.position()
      # if the song's position is more than 40 milliseconds from the end of the song
      if pos < self.song.length() - 40:
        # forward the song by 40 milliseconds
        self.song.skip(40)
      else:
        # otherwise, cue the song at the end of the song
        self.song.cue( song.length() )
      
      # start the song playing
      self.song.play()

  def mousePressed(self):
    if self.pressed():
      invert = True     

  def mouseReleased(self):
    self.invert = False

  def draw(self):
    if self.invert:
      fill(255)
      stroke(0)
    else:
      noFill()
      stroke(255)
    
    rect(self.x - self.hw, \
         self.y - self.hh, \
         self.hw*2, \
         self.hh*2)
    if self.invert:
      fill(0)
      stroke(255)
    else:
      fill(255)
      noStroke()
    
    triangle(self.x, \
             self.y, \
             self.x - self.hw/2, \
             self.y - self.hh/2, \
             self.x - self.hw/2, \
             self.y + self.hh/2)
    triangle(self.x, \
             self.y - self.hh/2, \
             self.x, \
             self.y + self.hh/2, \
             self.x + self.hw/2, \
             self.y)    
