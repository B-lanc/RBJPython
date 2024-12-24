import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import Bell

PATH = "./audio/testaudio.wav"
FREQ = 800
Q = 1
GAIN = -12.04
WRITEPATH = f"./audio/testBellf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = Bell(data, GAIN, FREQ, sr, Q, 0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
