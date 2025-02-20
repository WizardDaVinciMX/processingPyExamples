add_library("minim")
# add_library("ddf.minim.analysis.*
 

# Variables qui définissent les "zones" du spectre
# Par exemple, pour les basses, on prend seulement les premières 4% du spectre total
specLow = 0.03 # 3%
specMid = 0.125  # 12.5%
specHi = 0.20   # 20%

# Il reste donc 64% du spectre possible qui ne sera pas utilisé. 
# Ces valeurs sont généralement trop hautes pour l'oreille humaine de toute facon.

# Valeurs de score pour chaque zone
scoreLow = 0
scoreMid = 0
scoreHi = 0

# Valeur précédentes, pour adoucir la reduction
oldScoreLow = scoreLow
oldScoreMid = scoreMid
oldScoreHi = scoreHi

# Valeur d'adoucissement
scoreDecreaseRate = 25


#Lignes qui apparaissent sur les cotés
nbMurs = 500
 
def setup():
  global minim
  global song
  global fft
  # Cubes qui apparaissent dans l'espace
  global nbCubes
  global cubes
  global murs

  #Faire afficher en 3D sur tout l'écran
  fullScreen(P3D)
 
  #Charger la librairie minim
  minim = Minim(this)
 
  #Charger la chanson
  song = minim.loadFile("song.mp3")
  
  #Créer l'objet FFT pour analyser la chanson
  fft = FFT(song.bufferSize(), song.sampleRate())
  
  #Un cube par bande de fréquence
  nbCubes = (int)(fft.specSize()*specHi)
  
  #Créer tous les objets
  #Créer les objets cubes
#  for i in range(0, nbCubes):
#   cubes[i] = Cube() 
  cubes = [Cube()] * nbCubes
  
  #Autant de murs qu'on veux
  murs = [0] * nbMurs

#Créer les objets murs
  #Murs gauches
  for i in range(0, nbMurs, 4):
   murs[i] = Mur(0, height/2, 10, height)
  
  #Murs droits
  for i in range(1, nbMurs, 4):
   murs[i] = Mur(width, height/2, 10, height) 

  #Murs bas
  for i in range(2, nbMurs, 4):
   murs[i] = Mur(width/2, height, width, 10) 

  #Murs haut
  for i in range(3, nbMurs, 4):
   murs[i] = Mur(width/2, 0, width, 10) 

  #Fond noir
  background(0)
  
  #Commencer la chanson
  song.play(0)

 
def draw():
  global song
  global scoreLow
  global scoreMid
  global scoreHi

  #Faire avancer la chanson. On draw() pour chaque "frame" de la chanson...
  fft.forward(song.mix)
  
  #Calcul des "scores" (puissance) pour trois catégories de son
  #D'abord, sauvgarder les anciennes valeurs
  oldScoreLow = scoreLow
  oldScoreMid = scoreMid
  oldScoreHi = scoreHi
  global specLow
  
  #Réinitialiser les valeurs
  scoreLow = 0
  scoreMid = 0
  scoreHi = 0
 
  #Calculer les nouveaux "scores"
  for i in range(0, int(fft.specSize()*specLow)):
    scoreLow += fft.getBand(i)
  
  
  for i in range(int(fft.specSize()*specLow), int(fft.specSize()*specMid)):
    scoreMid += fft.getBand(i)
  
  
  for i in range(int(fft.specSize()*specMid), int(fft.specSize()*specHi)):
    scoreHi += fft.getBand(i)
  
  
  #Faire ralentir la descente.
  if oldScoreLow > scoreLow:
    scoreLow = oldScoreLow - scoreDecreaseRate
  
  
  if oldScoreMid > scoreMid:
    scoreMid = oldScoreMid - scoreDecreaseRate
  
  
  if oldScoreHi > scoreHi:
    scoreHi = oldScoreHi - scoreDecreaseRate
  
  
  #Volume pour toutes les fréquences à ce moment, avec les sons plus haut plus importants.
  #Cela permet à l'animation d'aller plus vite pour les sons plus aigus, qu'on remarque plus
  scoreGlobal = 0.66*scoreLow + 0.8*scoreMid + 1*scoreHi
  
  #Couleur subtile de background
  background(scoreLow/100, scoreMid/100, scoreHi/100)
   
  #Cube pour chaque bande de fréquence
  for i in range(0, nbCubes):
    #Valeur de la bande de fréquence
    bandValue = fft.getBand(i)
    
    #La couleur est représentée ainsi: rouge pour les basses, vert pour les sons moyens et bleu pour les hautes. 
    #L'opacité est déterminée par le volume de la bande et le volume global.
    cubes[i].display(scoreLow, scoreMid, scoreHi, bandValue, scoreGlobal)
  
  
  #Murs lignes, ici il faut garder la valeur de la bande précédent et la suivante pour les connecter ensemble
  previousBandValue = fft.getBand(0)
  
  #Distance entre chaque pode ligne, négatif car sur la dimension z
  dist = -25
  
  #Multiplier la hauteur par cette constante
  heightMult = 2
  
  #Pour chaque bande
  for i in range(1, fft.specSize()):
    #Valeur de la bande de fréquence, on multiplie les bandes plus loins pour qu'elles soient plus visibles.
    bandValue = fft.getBand(i)*(1 + (i/50))
    
    #Selection de la couleur en fonction des forces des différents types de sons
    stroke(100+scoreLow, 100+scoreMid, 100+scoreHi, 255-i)
    strokeWeight(1 + (scoreGlobal/100))
    
    #ligne inferieure gauche
    line(0, height-(previousBandValue*heightMult), dist*(i-1), 0, height-(bandValue*heightMult), dist*i)
    line((previousBandValue*heightMult), height, dist*(i-1), (bandValue*heightMult), height, dist*i)
    line(0, height-(previousBandValue*heightMult), dist*(i-1), (bandValue*heightMult), height, dist*i)
    
    #ligne superieure gauche
    line(0, (previousBandValue*heightMult), dist*(i-1), 0, (bandValue*heightMult), dist*i)
    line((previousBandValue*heightMult), 0, dist*(i-1), (bandValue*heightMult), 0, dist*i)
    line(0, (previousBandValue*heightMult), dist*(i-1), (bandValue*heightMult), 0, dist*i)
    
    #ligne inferieure droite
    line(width, height-(previousBandValue*heightMult), dist*(i-1), width, height-(bandValue*heightMult), dist*i)
    line(width-(previousBandValue*heightMult), height, dist*(i-1), width-(bandValue*heightMult), height, dist*i)
    line(width, height-(previousBandValue*heightMult), dist*(i-1), width-(bandValue*heightMult), height, dist*i)
    
    #ligne superieure droite
    line(width, (previousBandValue*heightMult), dist*(i-1), width, (bandValue*heightMult), dist*i)
    line(width-(previousBandValue*heightMult), 0, dist*(i-1), width-(bandValue*heightMult), 0, dist*i)
    line(width, (previousBandValue*heightMult), dist*(i-1), width-(bandValue*heightMult), 0, dist*i)
    
    #Sauvegarder la valeur pour le prochain tour de boucle
    previousBandValue = bandValue
  
  
  #Murs rectangles
  for i in range(0, nbMurs):
    #On assigne à chaque mur une bande, et on lui envoie sa force.
    intensity = fft.getBand(i%((int)(fft.specSize()*specHi)))
    murs[i].display(scoreLow, scoreMid, scoreHi, intensity, scoreGlobal)
  


#Classe pour les cubes qui flottent dans l'espace
class Cube:
  
  #Constructeur
  def __init__(self):
    #Position Z de "spawn" et position Z maximale
    self.startingZ = -10000
    self.maxZ = 1000
  
    #Faire apparaitre le cube à un endroit aléatoire
    self.x = random(0, width)
    self.y = random(0, height)
    self.z = random(self.startingZ, self.maxZ)
    
    #Donner au cube une rotation aléatoire
    self.rotX = random(0, 1)
    self.rotY = random(0, 1)
    self.rotZ = random(0, 1)
    self.sumRotX = 0
    self.sumRotY = 0
    self.sumRotZ = 0
  
  def display(self, scoreLow, scoreMid, scoreHi, intensity, scoreGlobal):
    #Sélection de la couleur, opacité déterminée par l'intensité (volume de la bande)
    displayColor = color(scoreLow * 0.67, scoreMid * 0.67, scoreHi * 0.67, intensity * 5)
    fill(displayColor, 255)
    
    #Couleur lignes, elles disparaissent avec l'intensité individuelle du cube
    strokeColor = color(255, 150-(20*intensity))
    stroke(strokeColor)
    strokeWeight(1 + (scoreGlobal/300))
    
    #Création d'une matrice de transformation pour effectuer des rotations, agrandissements
    pushMatrix()
    
    #Déplacement
    translate(self.x, self.y, self.z)
    
    #Calcul de la rotation en fonction de l'intensité pour le cube
    self.sumRotX += intensity*(self.rotX/1000)
    self.sumRotY += intensity*(self.rotY/1000)
    self.sumRotZ += intensity*(self.rotZ/1000)
    
    #Application de la rotation
    rotateX(self.sumRotX)
    rotateY(self.sumRotY)
    rotateZ(self.sumRotZ)
    
    #Création de la boite, taille variable en fonction de l'intensité pour le cube
    box(100+(intensity/2))
    
    #Application de la matrice
    popMatrix()
    
    #Déplacement Z
    self.z+= (1+(intensity/5)+(pow((scoreGlobal/150), 2)))
    
    #Replacer la boite à l'arrière lorsqu'elle n'est plus visible
    if self.z >= self.maxZ:
      self.x = random(0, width)
      self.y = random(0, height)
      self.z = self.startingZ


#Classe pour afficher les lignes sur les cotés
class Mur:
    
  #Constructeur
  def __init__(self, x, y, sizeX, sizeY):
    #Position minimale et maximale Z
    self.startingZ = -10000
    self.maxZ = 50
    #Faire apparaitre la ligne à l'endroit spécifié
    self.x = x
    self.y = y
    #Profondeur aléatoire
    self.z = random(self.startingZ, self.maxZ)  
    
    #On détermine la taille car les murs au planchers ont une taille différente que ceux sur les côtés
    self.sizeX = sizeX
    self.sizeY = sizeY

  #Fonction d'affichage
  def display(self, scoreLow, scoreMid, scoreHi, intensity, scoreGlobal):
    #Couleur déterminée par les sons bas, moyens et élevé
    #Opacité déterminé par le volume global
    displayColor = color(scoreLow*0.67, scoreMid*0.67, scoreHi*0.67, scoreGlobal)
    
    #Faire disparaitre les lignes au loin pour donner une illusion de brouillard
    fill(displayColor, ((scoreGlobal-5)/1000)*(255+(self.z/25)))
    noStroke()
    
    #Première bande, celle qui bouge en fonction de la force
    #Matrice de transformation
    pushMatrix()
    
    #Déplacement
    translate(self.x, self.y, self.z)
    
    #Agrandissement
    if intensity > 100:
        intensity = 100
    scale(self.sizeX*(intensity/100), self.sizeY*(intensity/100), 20)
    
    #Création de la "boite"
    box(1)
    popMatrix()
    
    #Deuxième bande, celle qui est toujours de la même taille
    displayColor = color(scoreLow*0.5, scoreMid*0.5, scoreHi*0.5, scoreGlobal)
    fill(displayColor, (scoreGlobal/5000)*(255+(self.z/25)))
    #Matrice de transformation
    pushMatrix()
    
    #Déplacement
    translate(self.x, self.y, self.z)
    
    #Agrandissement
    scale(self.sizeX, self.sizeY, 10)
    
    #Création de la "boite"
    box(1)
    popMatrix()
    
    #Déplacement Z
    self.z += pow((scoreGlobal/150), 2)
    if self.z >= self.maxZ:
      self.z = self.startingZ
