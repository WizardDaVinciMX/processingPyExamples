/**
 * Boogie creates a more complicated set of patterns running in parallel.
 *
 * This example combines the visual pattern rendering of the ColorBars example,
 * and MIDI rendering from SimpleMIDI.
 *
 * You will need The MidiBus <https:#github.com/sparks/themidibus/> and a MIDI synthesizer
 * installed for this example. If you don't hear any sound, please consult the instructions at:
 * https:#corajr.github.io/loom/reference/com/corajr/loom/wrappers/MidiBusImpl.html#midi
 */

load_data("java.util.Map

load_data("com.corajr.loom.*
load_data("com.corajr.loom.wrappers.*
load_data("com.corajr.loom.time.*
load_data("com.corajr.loom.transforms.*
load_data("static com.corajr.loom.LEvent.*

load_data("themidibus.*

MidiBus myBus

# The seed for random number generation.
seed = 2

# If recording, output will be saved to a MIDI file.
boolean recording = false

Loom loom
NonRealTimeScheduler scheduler

desiredFPS = 30

millis = 0
millisPerFrame = 1000.0 / desiredFPS

Interval singleInterval = Interval(0, 1)
HashMap<Integer, Pattern> vertical, horizontal

# How many times to repeat the random pattern.
repeats = 2

# How many pixels wide each "road" is.
roadWidth = 12

# mean and standard deviation of the musical event durations.
mu = 0.0
sd = 1.2

# Create the random events for one of the bars.
LEvent[] makeEvents() {
  numEvents = 8
  int[] durations = int[numEvents]
  totalDuration = 0.0

  for (i = 0 i < numEvents i++) {
    duration = int(exp(mu + (sd * randomGaussian())) + 1.0)
    durations[i] = duration
    totalDuration += duration
  }

  LEvent[] events = LEvent[numEvents]

  for (i = 0 i < numEvents i++) {
    duration = durations[i] / totalDuration
    value = duration > 0.2 ? 0.0 : round(random(1, 3)) / 4.0 
    events[i] = evt(duration, value)
  }

  return seq(events)
}

def setup() {
  size(720, 720)
  noSmooth()

  scheduler = NonRealTimeScheduler()

  if (recording) {
    loom = Loom(this, scheduler)
    loom.recordMidi("boogie.mid")
  } else {
    loom = Loom(this)
  }

  loom.setPeriod(7500)

  vertical = HashMap<Integer, Pattern>()
  horizontal = HashMap<Integer, Pattern>()

  randomSeed(seed)

  # This is the basic pattern, which gives a consistent color and
  # MIDI velocity across all the "roads."
  Pattern proto = Pattern(loom, EventCollection())
  proto.asColor(#FFD300, #DDDDDD, #00499A, #CA0000, #005C35).asMidiData2(0, 80)

  for (i = 0 i < 10 i++) {
    # each road goes up by one octave (12 semitones), cycling through octaves 3-8.
    octave = ((i % 5) + 3) * 12

    Pattern verticalPat = proto.clone()
    verticalPat.extend(makeEvents()).repeat(repeats)

    # special additional pattern (to spell out LOOM)
    if (i != 0 && i != 8)
      verticalPat.after(repeats, seq(rest(0.3), evt(0.3, 1.0)))

    # set to channel 0 and use the harp
    verticalPat.asMidiChannel(0).asMidiInstrument("ORCHESTRAL_HARP")

    # pitch classes 0, 4, 7, 0
    verticalPat.asMidiNote(-127, 0, 4, 7, 0).transpose(octave).asMidiMessage(verticalPat)

    vertical.put(i * (width/10), verticalPat)

    Pattern horizontalPat = proto.clone()
    horizontalPat.extend(makeEvents()).repeat(repeats)

    # special additional pattern (to spell out LOOM)
    if (i == 1)
      horizontalPat.after(repeats, seq(rest(0.2), rest(0.3), evt(0.1, 1.0), rest(0.1), evt(0.1, 1.0), rest(0.1), evt(0.2, 1.0)))
    else if (i == 4)
      horizontalPat.after(repeats, seq(rest(0.2), rest(0.1), evt(0.1, 1.0), rest(0.1), evt(0.1, 1.0), rest(0.1), evt(0.1, 1.0)))

    horizontalPat.asColor(#FFD300, #DDDDDD, #00499A, #CA0000, #005C35)
    horizontalPat.asMidiChannel(1).asMidiInstrument("ORCHESTRAL_HARP")
    # pitch classes 2, 9, 11, 9
    horizontalPat.asMidiNote(-127, 2, 9, 11, 9).transpose(octave).asMidiMessage(horizontalPat)

    horizontal.put(i * (height/10), horizontalPat)
  }

  if (!recording) {
    # List valid MIDI devices.
    # MidiBus.list()

    # Initialize the MIDI bus and add it to the Loom.
    myBus = MidiBus(this, -1, "Bus 1")
    loom.setMidiBus(myBus)
    loom.play()
  }
}

def draw() {
  background(255)

  for (Map.Entry me : horizontal.entrySet ()) {
    Pattern pat = (Pattern) me.getValue()

    # The key of each pattern in the map is its horizontal position in pixels
    pat.rect(0, ((Integer) me.getKey()).intValue(), width, roadWidth, singleInterval)
  }

  rotate(HALF_PI)
  translate(0, -width)

  for (Map.Entry me : vertical.entrySet ()) {
    Pattern pat = (Pattern) me.getValue()
    pat.rect(0, ((Integer) me.getKey()).intValue(), height, roadWidth, singleInterval)
  }

  if (recording) {
    # in non-realtime mode, we calculate how many milliseconds have passed
    # and automatically execute any events (e.g. note on/off) that should have occurred
    # since the last frame.
    millis += millisPerFrame
    scheduler.setElapsedMillis((long) millis)

    saveFrame("####.png")

    if (millis > loom.getPeriod() * (repeats + 1.3))
      exit()
  }
}

def exit() {
  loom.dispose() # needed to save MIDI file
  super.exit()
}