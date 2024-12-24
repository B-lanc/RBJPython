import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import APF

PATH = "./audio/testaudio.wav"
FREQ = 500
Q = 1
WRITEPATH = f"./audio/testAPFf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = APF(data, FREQ, sr, Q, 0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
