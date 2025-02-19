add_library("gab.opencv.*
add_library("processing.video.*
add_library("java.awt.*

Capture video
OpenCV opencv

def setup():
  size(640, 480)
  video = Capture(this, "pipeline:autovideosrc")
  opencv = OpenCV(this, 640, 480)
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)  

  video.start()


def draw():
  opencv.loadImage(video)

  image(video, 0, 0 )

  noFill()
  stroke(0, 255, 0)
  strokeWeight(3)
  Rectangle[] faces = opencv.detect()
  println(faces.length)

  for (i = 0 i < faces.length i+=1):
    println(faces[i].x + "," + faces[i].y)
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height)
  


def captureEvent(Capture c):
  c.read()

