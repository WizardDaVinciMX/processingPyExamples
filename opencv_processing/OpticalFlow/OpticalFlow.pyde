add_library("opencv_processing")
add_library("video")


def setup():
  global opencv
  global video

  size(1136, 320)
  video = Movie(this, "sample1.mov")
  opencv = OpenCV(this, 568, 320)
  video.loop()
  video.play()


def draw():
  background(0)

  if video.width == 0 or video.height == 0:
    return

  opencv.loadImage(video)
  opencv.calculateOpticalFlow()

  image(video, 0, 0)
  translate(video.width, 0)
  stroke(255, 0, 0)
  opencv.drawOpticalFlow()

  aveFlow = opencv.getAverageFlow()
  flowScale = 50

  stroke(255)
  strokeWeight(2)
  line(video.width/2, video.height/2, video.width/2 + aveFlow.x*flowScale, video.height/2 + aveFlow.y*flowScale)


def movieEvent(m):
  m.read()
