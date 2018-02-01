import pydub
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("test.wav")

play(song)