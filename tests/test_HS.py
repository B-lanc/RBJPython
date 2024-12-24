import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import HS

PATH = "./audio/testaudio.wav"
FREQ = 5000
Q = 0.5
GAIN = -12.04
WRITEPATH = f"./audio/testHSf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = HS(data, GAIN, FREQ, sr, Q, 0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
