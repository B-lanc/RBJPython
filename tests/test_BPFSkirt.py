import sys
import os

sys.path.insert(0, os.getcwd())
from utils import read_audio, write_audio
from filters import BPFSkirt

PATH = "./audio/testaudio.wav"
FREQ = 1000
Q = 2
WRITEPATH = f"./audio/testBPFSkirtf{FREQ}q{Q}.wav"


def test_HPF():
    data, sr = read_audio(PATH)
    data = BPFSkirt(data, FREQ, sr, Q, 0)
    write_audio(WRITEPATH, data, sr)


test_HPF()
