# Simple vector class that holds an x,y,z position.

class Tuple {
  x, y, z

  Tuple() { }

  Tuple(x, y, z) {
    set(x, y, z)
  }

  def set(x, y, z) {
    this.x = x
    this.y = y
    this.z = z
  }
  
  def target(Tuple another, amount) {
    amount1 = 1.0 - amount
    x = x*amount1 + another.x*amount
    y = y*amount1 + another.y*amount
    z = z*amount1 + another.z*amount
  }
  
  def phil() {
    fill(x, y, z)
  }
}

