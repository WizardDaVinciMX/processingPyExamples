add_library("opencv_processing")
add_library("video")

def setup():
  global video
  global opencv

  size(720, 480)
  video = Movie(this, "street.mov")
  opencv = OpenCV(this, 720, 480)

  opencv.startBackgroundSubtraction(5, 3, 0.5)

  video.loop()
  video.play()


def draw():
  image(video, 0, 0)

  if video.width == 0 or video.height == 0:
    return

  opencv.loadImage(video)
  opencv.updateBackground()

  opencv.dilate()
  opencv.erode()

  noFill()
  stroke(255, 0, 0)
  strokeWeight(3)
  for contour in opencv.findContours():
    contour.draw()
  


def movieEvent(m):
  m.read()
