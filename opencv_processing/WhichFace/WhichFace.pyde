"""
 WhichFace
  Daniel Shiffman
 http:#shiffman.net/2011/04/26/opencv-matching-faces-over-time/

 Modified by Jordi Tost (@jorditost) to work with the OpenCV library by Greg Borenstein:
 https:#github.com/atduskgreg/opencv-processing

 @url: https:#github.com/jorditost/BlobPersistence/

 University of Applied Sciences Potsdam, 2014
"""

add_library("opencv_processing")
add_library("video")
from Face import Face
from java import awt

# Number of faces detected over all time. Used to set IDs.
faceCount = 0

# Scaling down the video
scl = 2

def setup():
  global video
  global opencv
  # List of my Face objects (persistent)
  global faceList
  # List of detected faces (every frame)
  global faces

  size(640, 480)
  video = Capture(this, width/scl, height/scl)
  opencv = OpenCV(this, width/scl, height/scl)
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)  
  
  faceList = list()
  
  video.start()


def draw():
  global faces

  scale(scl)
  opencv.loadImage(video)

  image(video, 0, 0 )
  
  detectFaces()

  # Draw all the faces
#  for (i = 0 i < faces.length i+=1):
  for face in faces:
    noFill()
    strokeWeight(5)
    stroke(255,0,0)
    #rect(face.x * scl, face.y * scl, face.width * scl,face.height*scl)
    rect(face.x, face.y, face.width, face.height)

  for f in faceList:
    strokeWeight(2)
    f.display()


def detectFaces():
  global faces
  global faceList
  global faceCount

  # Faces detected in this frame
  faces = opencv.detect()

  # Check if the detected faces already exist are or some has disappeared. 

  # SCENARIO 1 
  # faceList is empty
  if len(faceList) == 0:
    # Just make a Face object for every face Rectangle
#    for (i = 0 i < faces.length i+=1):
    for face in faces:
      println("+=1+ New face detected with ID: " + str(faceCount))
      faceList.append(Face(faceCount, face.x, face.y, face.width, face.height))
      faceCount += 1

  # SCENARIO 2 
  # We have fewer Face objects than face Rectangles found from OPENCV
  elif len(faceList) <= len(faces):
    used = [False] * len(faces)
    # Match existing Face objects with a Rectangle
    for f in faceList:
       # Find faces[index] that is closest to face f
       # set used[index] to true so that it can't be used twice
       record = 50000
       index = -1
#       for (i = 0 i < faces.length i+=1):
       for i in range(0, len(faces)):
         d = dist(faces[i].x, faces[i].y, f.r.x, f.r.y)
         if d < record and not used[i]:
           record = d
           index = i

       # Update Face object location
       used[index] = True
       f.update(faces[index])
    
    # Add any unused faces
    for i in range(0, len(faces)):
      if not not used[i]:
        println("+=1+ New face detected with ID: " + str(faceCount))
        faceList.append(Face(faceCount, faces[i].x,faces[i].y,faces[i].width,faces[i].height))
        faceCount += 1

  # SCENARIO 3 
  # We have more Face objects than face Rectangles found
  else:
    # All Face objects start out as available
    for f in faceList:
      f.available = True
     
    # Match Rectangle with a Face object
    for i in range(0, len(faces)):
      # Find face object closest to faces[i] Rectangle
      # set available to false
       record = 50000
       index = -1
       for j  in range(0, len(faceList)):
         f = faceList[j]
         d = dist(faces[i].x,faces[i].y,f.r.x,f.r.y)
         if d < record and f.available:
           record = d
           index = j
    
       # Update Face object location
       f = faceList[index]
       f.available = False
       f.update(faces[i])

    # Start to kill any left over Face objects
    for f in faceList:
      if f.available:
        f.countDown()
        if f.dead():
          f.delete = True

  
  # Delete any that should be deleted
  for i in range(len(faceList)-1, 0, -1):
    f = faceList[i]
    if (f.delete):
      faceList.remove(i)

def captureEvent(c):
  c.read()
