/**
 * Loop. 
 * 
 * Shows how to load and play a QuickTime movie file.  
 *
 */

load_data("processing.video.*

Movie movie

def setup() {
  size(560, 406)
  background(0)
  # Load and play the video in a loop
  movie = Movie(this, "launch2.mp4")
  movie.loop()
}

def movieEvent(Movie m) {
  m.read()
}

def draw() {
  #if (movie.available() == true) {
  #  movie.read() 
  #}
  image(movie, 0, 0, width, height)
}