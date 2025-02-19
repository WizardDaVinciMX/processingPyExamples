add_library("gab.opencv.*

OpenCV opencv

def setup():
  opencv = OpenCV(this, "test.jpg")
  size(1080, 720)


def draw():
  image(opencv.getOutput(), 0, 0)
