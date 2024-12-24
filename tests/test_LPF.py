import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import LPF

PATH = "./audio/testaudio.wav"
FREQ = 3000
Q = 1
WRITEPATH = f"./audio/testLPFf{FREQ}q{Q}.wav"


def test_LPF():
    data, sr = read_audio(PATH)
    data = LPF(data, FREQ, sr, Q, axis=0)
    write_audio(WRITEPATH, data, sr)


test_LPF()
