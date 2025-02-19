"""*
 * WhichFace
 * Daniel Shiffman
 * http:#shiffman.net/2011/04/26/opencv-matching-faces-over-time/
 *
 * Modified by Jordi Tost (@jorditost) to work with the OpenCV library by Greg Borenstein:
 * https:#github.com/atduskgreg/opencv-processing
 *
 * @url: https:#github.com/jorditost/BlobPersistence/
 *
 * University of Applied Sciences Potsdam, 2014
 """

add_library("gab.opencv.*
add_library("processing.video.*
add_library("java.awt.*

Capture video
OpenCV opencv

# List of my Face objects (persistent)
ArrayList<Face> faceList

# List of detected faces (every frame)
Rectangle[] faces

# Number of faces detected over all time. Used to set IDs.
faceCount = 0

# Scaling down the video
scl = 2

def setup():
  size(640, 480)
  video = Capture(this, width/scl, height/scl)
  opencv = OpenCV(this, width/scl, height/scl)
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE)  
  
  faceList = ArrayList<Face>()
  
  video.start()


def draw():
  scale(scl)
  opencv.loadImage(video)

  image(video, 0, 0 )
  
  detectFaces()

  # Draw all the faces
  for (i = 0 i < faces.length i+=1):
    noFill()
    strokeWeight(5)
    stroke(255,0,0)
    #rect(faces[i].x*scl,faces[i].y*scl,faces[i].width*scl,faces[i].height*scl)
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height)
  
  
  for (Face f : faceList):
    strokeWeight(2)
    f.display()
  


def detectFaces():
  
  # Faces detected in this frame
  faces = opencv.detect()
  
  # Check if the detected faces already exist are or some has disappeared. 
  
  # SCENARIO 1 
  # faceList is empty
  if (faceList.isEmpty()):
    # Just make a Face object for every face Rectangle
    for (i = 0 i < faces.length i+=1):
      println("+=1+ New face detected with ID: " + faceCount)
      faceList.add(Face(faceCount, faces[i].x,faces[i].y,faces[i].width,faces[i].height))
      faceCount+=1
    
  
  # SCENARIO 2 
  # We have fewer Face objects than face Rectangles found from OPENCV
   else if (faceList.size() <= faces.length):
    boolean[] used = boolean[faces.length]
    # Match existing Face objects with a Rectangle
    for (Face f : faceList):
       # Find faces[index] that is closest to face f
       # set used[index] to true so that it can't be used twice
       record = 50000
       index = -1
       for (i = 0 i < faces.length i+=1):
         d = dist(faces[i].x,faces[i].y,f.r.x,f.r.y)
         if (d < record && !used[i]):
           record = d
           index = i
          
       
       # Update Face object location
       used[index] = true
       f.update(faces[index])
    
    # Add any unused faces
    for (i = 0 i < faces.length i+=1):
      if (!used[i]):
        println("+=1+ New face detected with ID: " + faceCount)
        faceList.add(Face(faceCount, faces[i].x,faces[i].y,faces[i].width,faces[i].height))
        faceCount+=1
      
    
  
  # SCENARIO 3 
  # We have more Face objects than face Rectangles found
   else:
    # All Face objects start out as available
    for (Face f : faceList):
      f.available = true
     
    # Match Rectangle with a Face object
    for (i = 0 i < faces.length i+=1):
      # Find face object closest to faces[i] Rectangle
      # set available to false
       record = 50000
       index = -1
       for (j = 0 j < faceList.size() j+=1):
         Face f = faceList.get(j)
         d = dist(faces[i].x,faces[i].y,f.r.x,f.r.y)
         if (d < record && f.available):
           record = d
           index = j
          
       
       # Update Face object location
       Face f = faceList.get(index)
       f.available = false
       f.update(faces[i])
     
    # Start to kill any left over Face objects
    for (Face f : faceList):
      if (f.available):
        f.countDown()
        if (f.dead()):
          f.delete = true
         
      
     
  
  
  # Delete any that should be deleted
  for (i = faceList.size()-1 i >= 0 i--):
    Face f = faceList.get(i)
    if (f.delete):
      faceList.remove(i)
     
  


def captureEvent(Capture c):
  c.read()

