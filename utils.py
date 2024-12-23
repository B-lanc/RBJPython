import soundfile as sf


def read_audio(path):
    data, sr = sf.read(path)
    return data, sr


def write_audio(path, data, sr):
    sf.write(path, data, sr)
