import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import Notch

PATH = "./audio/testaudio.wav"
FREQ = 2000
Q = 2
WRITEPATH = f"./audio/testNotchf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = Notch(data, FREQ, sr, Q, axis=0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
