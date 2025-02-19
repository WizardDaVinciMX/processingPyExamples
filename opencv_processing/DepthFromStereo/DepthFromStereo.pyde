add_library("opencv_processing")
from org.opencv.core import Mat
from org.opencv.calib3d import StereoBM
from org.opencv.core import CvType
from org.opencv.calib3d import StereoSGBM


def setup():
  global ocvL, ocvR
  global  imgL, imgR, depth1, depth2

  imgL = loadImage("scene_l.jpg")
  imgR = loadImage("scene_r.jpg")
  ocvL = OpenCV(this, imgL)

  ocvR = OpenCV(this, imgR)

  size(768, 576)
  
  ocvL.gray()
  ocvR.gray()
  left = ocvL.getGray()
  right = ocvR.getGray()

  disparity = OpenCV.imitate(left)

  stereo = StereoSGBM.create(0, 32, 3, 128, 256, 20, 16, 1, 100, 20, 1)
  stereo.compute(left, right, disparity )

  depthMat = OpenCV.imitate(left)
  disparity.convertTo(depthMat, depthMat.type())

  depth1 = createImage(depthMat.width(), depthMat.height(), RGB)
  ocvL.toPImage(depthMat, depth1)

  stereo2 = StereoBM.create()
  stereo2.compute(left, right, disparity )
  disparity.convertTo(depthMat, depthMat.type())


  depth2 = createImage(depthMat.width(), depthMat.height(), RGB)
  ocvL.toPImage(depthMat, depth2)


def draw():
  image(imgL, 0, 0)
  image(imgR, imgL.width, 0)

  image(depth1, 0, imgL.height)
  image(depth2, imgL.width, imgL.height)

  fill(255, 0, 0)
  text("left", 10, 20)
  text("right", 10 + imgL.width, 20)
  text("stereo SGBM", 10, imgL.height + 20)
  text("stereo BM", 10 + imgL.width, imgL.height+ 20)
