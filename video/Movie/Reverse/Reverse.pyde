/**
 * Reverse playback example.
 *
 * The Movie.speed() method allows to change the playback speed. 
 * Use negative values for backwards playback. Note that not all 
 * video formats support backwards playback. This depends on the 
 * underlying gstreamer plugins used by gsvideo. For example, the 
 * theora codec does support backward playback, but not so the H264 
 * codec, at least in its current version.
 * 
 */

load_data("processing.video.*

Movie mov
boolean speedSet = false
boolean once = true

def setup() {
  size(560, 406)
  background(0)
  mov = Movie(this, "launch2.mp4")
  mov.play()
}

def movieEvent(Movie m) {
  m.read()  
  if (speedSet == true) {
    speedSet = false
  }
}

def draw() {
  if (speedSet == false && once == true) {
    # Setting the speed should be done only once,
    # this is the reason for the if statement.
    speedSet = true
    once = false
    mov.jump(mov.duration())
    # -1 means backward playback at normal speed.
    mov.speed(-1.0)
    # Setting to play again, since the movie stop
    # playback once it reached the end.
    mov.play()
  }
  image(mov, 0, 0, width, height)
}