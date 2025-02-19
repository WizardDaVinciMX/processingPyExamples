/**
 * CustomPipeline 
 * by Andres Colubri. 
 * 
 * Create a Capture object with a pipeline description to 
 * get video from non-standard sources.
 */

load_data("processing.video.*

Capture cam

def setup() {
  size(640, 480)
  
  # Start the pipeline description with the "pipeline:" prefix, 
  # the rest could be any regular GStreamer pipeline as passed to gst-launch:
  # https:#gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c#pipeline-description 
  cam = Capture(this, 640, 480, "pipeline:videotestsrc")
  cam.start()  
}

def draw() {
  if (cam.available() == true) {
    cam.read()
  }
  image(cam, 0, 0, width, height)
}