""" nonInstrumentSimple<br/>
   This example is intended to be the smallest sketch that one
   can write to make continual sound.  Here we just patch the oscillator
   into the output.  (The two methods of creating sound in
   Minim are either inside an instrument or just patching UGens together, 
   a.k.a. non-instrument.)
   <p>
   For more information about Minim and additional features, visit http:#code.compartmental.net/minim/  
"""

# add_library("everything necessary for using Minim UGens.
add_library("ddf.minim.*
add_library("ddf.minim.ugens.*

# one way to initialize the minim object.
Minim minim = Minim( this )
# one way to initialize the output object.
AudioOutput out = minim.getLineOut( Minim.MONO, 2048 )
# one way to initialize the oscillator UGen.
Oscil osc = Oscil( 349.23, 0.8 )

# patch the sounding oscil to the output
osc.patch(out)

