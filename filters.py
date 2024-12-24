from scipy.signal import lfilter
import math

get_A = lambda dbGain: 10 ** (dbGain / 40)
get_Omega = lambda f, sr: 2 * math.pi * f / sr
sin = math.sin
cos = math.cos
get_alpha = lambda omega, Q: sin(omega) / 2 / Q


def LPF(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = (1 - cosomega) / 2
    b1 = 1 - cosomega
    b2 = (1 - cosomega) / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def HPF(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = (1 + cosomega) / 2
    b1 = -1 - cosomega
    b2 = (1 + cosomega) / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def BPFSkirt(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    sinomega = sin(omega)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = sinomega / 2
    b1 = 0
    b2 = -sinomega / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def BPF(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = alpha
    b1 = 0
    b2 = -alpha
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def Notch(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = 1
    b1 = -2 * cosomega
    b2 = 1
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def APF(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = 1 - alpha
    b1 = -2 * cosomega
    b2 = 1 + alpha
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def Bell(data, gain, freq, sr=48000, Q=1, axis=0):
    A = get_A(gain)
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega, Q)

    b0 = 1 + alpha * A
    b1 = -2 * cosomega
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2 * cosomega
    a2 = 1 - alpha / A

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)
