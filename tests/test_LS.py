import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import LS

PATH = "./audio/testaudio.wav"
FREQ = 300
Q = 0.5
GAIN = -12.04
WRITEPATH = f"./audio/testLSf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = LS(data, GAIN, FREQ, sr, Q, 0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
