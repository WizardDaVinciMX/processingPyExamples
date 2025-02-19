/**
 * HSV Space
 * by Ben Fry. 
 *
 * Arrange the pixels from live video into the HSV Color Cone.
 */
 
load_data("processing.video.*
load_data("java.awt.Color

Capture video
count
boolean cheatScreen = true

static final BOX_SIZE        = 0.75
static final CONE_HEIGHT     = 1.2
static final MAX_RADIUS      = 10
static final ROT_INCREMENT   = 3.0
static final TRANS_INCREMENT = 1
static final STEP_AMOUNT     = 0.1

Tuple[] farbe
Tuple[] trans

float[] hsb = float[3]

leftRightAngle
upDownAngle
fwdBackTrans
upDownTrans
leftRightTrans
boolean motion

boolean blobby = false


def setup() {
  size(640, 480, P3D)

  # This the default video input, see the GettingStartedCapture 
  # example if it creates an error
  video = Capture(this, 160, 120)
  
  # Start capturing the images from the camera
  video.start()  
  
  count = video.width * video.height

  sphereDetail(60)

  upDownTrans = 0
  leftRightTrans = 0
  motion = false

  leftRightAngle = 101.501297
  upDownAngle = -180.098694
  fwdBackTrans = 14.800003

  farbe = Tuple[count]
  trans = Tuple[count]
  for (i = 0 i < count i++) {
    farbe[i] = Tuple()
    trans[i] = Tuple()
  }
}


def draw() {
  background(0)

  if (!blobby) {
    lights()
  }
  
  pushMatrix()
  translate(width/2, height/2)
  scale(min(width, height) / 10.0)

  translate(0, 0, -20 + fwdBackTrans)
  rotateY(radians(36 + leftRightAngle)) #, 0, 1, 0)
  rotateX(radians(-228 + upDownAngle)) #, 1, 0, 0)

  strokeWeight(0.1)
  if (blobby) {    
    stroke(0.35, 0.35, 0.25, 0.15)    
    wireCone(MAX_RADIUS, MAX_RADIUS * CONE_HEIGHT, 18, 18)
  } 
  else {
    stroke(0.35, 0.35, 0.25, 0.25)
    wireCone(MAX_RADIUS, MAX_RADIUS * CONE_HEIGHT, 180, 18)
  }

  noStroke()
  video.loadPixels()
  for (i = 0 i < count i++) {
    pixelColor = video.pixels[i]
    r = (pixelColor >> 16) & 0xff
    g = (pixelColor >> 8) & 0xff
    b = pixelColor & 0xff
    Color.RGBtoHSB(r, g, b, hsb)

    radius = hsb[1] * hsb[2]
    angle = hsb[0] * 360.0 * DEG_TO_RAD
    nx = MAX_RADIUS * radius * cos(angle)
    ny = MAX_RADIUS * radius * sin(angle)
    nz = hsb[2] * MAX_RADIUS * CONE_HEIGHT

    trans[i].set(trans[i].x - (trans[i].x - nx)*STEP_AMOUNT,
                 trans[i].y - (trans[i].y - ny)*STEP_AMOUNT,
                 trans[i].z - (trans[i].z - nz)*STEP_AMOUNT)

    farbe[i].set(farbe[i].x - (farbe[i].x - r)*STEP_AMOUNT,
                 farbe[i].y - (farbe[i].y - g)*STEP_AMOUNT,
                 farbe[i].z - (farbe[i].z - b)*STEP_AMOUNT)

    pushMatrix()
    farbe[i].phil()
    trans[i].tran()

    rotate(radians(45), 1, 1, 0)
    if (blobby) {
      sphere(BOX_SIZE * 2) #, 20, 20)
    } else {
      box(BOX_SIZE)
    }

    popMatrix()
  }
  popMatrix()

  if (motion) {
    upDownAngle--
    leftRightAngle--
  }

  if (cheatScreen) {
    image(video, 0, height - video.height)
  }
}


def captureEvent(Capture c) {
  c.read()
}


def keyPressed() {
  switch (key) {
  case 'g': 
    saveFrame() 
    break
  case 'c': 
    cheatScreen = !cheatScreen 
    break

  case 'm': 
    motion = !motion 
    break
  case '=': 
    fwdBackTrans += TRANS_INCREMENT 
    break
  case '-': 
    fwdBackTrans -= TRANS_INCREMENT 
    break
  case 'b': 
    blobby = !blobby 
    break
  }
}


def mouseDragged() {
  dX, dY

  switch (mouseButton) {
  case LEFT:  # left right up down
    dX = pmouseX - mouseX
    dY = pmouseY - mouseY
    leftRightAngle -= dX * 0.2
    upDownAngle += dY * 0.4
    break

  case CENTER:
    dX = pmouseX - mouseX
    dY = pmouseY - mouseY
    leftRightTrans -= TRANS_INCREMENT * dX
    upDownTrans -= TRANS_INCREMENT * dY
    break

  case RIGHT:  # in and out
    dY = (float) (pmouseY - mouseY)
    fwdBackTrans -= TRANS_INCREMENT * dY
    break
  }
}


def wireCone(radius, height, stepX, stepY) {
  steps = 10
  stroke(40)
  for (i = 0 i < steps i++) {
    angle = map(i, 0, steps, 0, TWO_PI)
    x = radius * cos(angle)
    y = radius * sin(angle)
    line(x, y, height, 0, 0, 0)
  }
  noFill()
  pushMatrix()
  translate(0, 0, height)
  ellipseMode(CENTER)
  ellipse(0, 0, radius, radius)
  popMatrix()
}
