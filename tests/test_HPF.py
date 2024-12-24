import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import HPF

PATH = "./audio/testaudio.wav"
FREQ = 300
Q = 0.5
WRITEPATH = f"./audio/testHPFf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = HPF(data, FREQ, sr, Q, axis=0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
