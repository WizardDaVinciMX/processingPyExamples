"""
 * This sketch shows how to use envelopes and oscillators. Envelopes are pre-defined
 * amplitude distributions over time. The sound library provides an ASR envelope which
 * stands for attack, sustain, release. The amplitude first rises, then sustains at the
 * maximum level and decays slowly, all depending on the pre-defined length of the three
 * time segments.
 *
 *      .________
 *     .          ---
 *    .              --- 
 *   .                  ---
 *   A       S        R 
"""

add_library("sound")

# Times and levels for the ASR envelope
attackTime = 0.001
sustainTime = 0.004
sustainLevel = 0.3
releaseTime = 0.2

# This is an octave in MIDI notes.
midiSequence =  [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]  

# Play a note every 200ms
duration = 200

# This variable stores the poin time when the next note should be triggered
trigger = millis() 

# An index to count up the notes
note = 0 

def setup():
  global triOsc
  global env

  size(640, 360)
  background(255)

  # Create triangle wave and start it
  triOsc = TriOsc(this)

  # Create the envelope 
  env = Env(this)


def draw():
  global trigger
  global note

  # If the determined trigger moment in time matches up with the computer clock and
  # the sequence of notes hasn't been finished yet, the next note gets played.
  if (millis() > trigger) and (note < len(midiSequence)):

    # midiToFreq transforms the MIDI value into a frequency in Hz which we use to
    # control the triangle oscillator with an amplitute of 0.5
    triOsc.play(midiToFreq(midiSequence[note]), 0.5)

    # The envelope gets triggered with the oscillator as input and the times and
    # levels we defined earlier
    env.play(triOsc, attackTime, sustainTime, sustainLevel, releaseTime)

    # Create the trigger according to predefined duration
    trigger = millis() + duration

    # Advance by one note in the midiSequence
    note += 1

    # Loop the sequence, notice the jitter
    if note == 12: 
      note = 0
    
  
 

# This helper function calculates the respective frequency of a MIDI note
def midiToFreq(note):
  return (pow(2, ((note-69)/12.0))) * 440
