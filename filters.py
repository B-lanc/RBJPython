from scipy.signal import lfilter
from math import pi, sin, cos, sqrt, sinh, log

log10 = lambda n: log(n, 10)


def get_intermediate(freq, sr, Q, gain=None, BW=None, S=None):
    omega = 2 * pi * freq / sr
    sinomega = sin(omega)
    cosomega = cos(omega)

    A = get_A(gain) if gain else None

    if Q is None:
        if BW is not None:
            alpha = sinomega * sinh(log10(2) / 2 * BW * omega / sinomega)
        else:
            alpha = sinomega / 2 * sqrt((A + 1 / A) * (1 / S - 1) + 2)
    else:
        alpha = sinomega / 2 / Q
    return omega, sinomega, cosomega, alpha, A


def LPF(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = (1 - cosomega) / 2
    b1 = 1 - cosomega
    b2 = (1 - cosomega) / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def HPF(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = (1 + cosomega) / 2
    b1 = -1 - cosomega
    b2 = (1 + cosomega) / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def BPFSkirt(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = sinomega / 2
    b1 = 0
    b2 = -sinomega / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def BPF(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = alpha
    b1 = 0
    b2 = -alpha
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def Notch(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = 1
    b1 = -2 * cosomega
    b2 = 1
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def APF(data, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, _ = get_intermediate(freq, sr, Q=Q, BW=BW)

    b0 = 1 - alpha
    b1 = -2 * cosomega
    b2 = 1 + alpha
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def Bell(data, gain, freq, sr=48000, Q=1, BW=None, axis=0):
    omega, sinomega, cosomega, alpha, A = get_intermediate(
        freq, sr, Q=Q, gain=gain, BW=BW
    )

    b0 = 1 + alpha * A
    b1 = -2 * cosomega
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2 * cosomega
    a2 = 1 - alpha / A

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def LS(data, gain, freq, sr=48000, Q=1, BW=None, S=None, axis=0):
    omega, sinomega, cosomega, alpha, A = get_intermediate(
        freq, sr, Q=Q, gain=gain, BW=BW, S=S
    )
    twosqrtaalpha = 2 * sqrt(A) * alpha

    b0 = A * ((A + 1) - (A - 1) * cosomega + twosqrtaalpha)
    b1 = 2 * A * ((A - 1) - (A + 1) * cosomega)
    b2 = A * ((A + 1) - (A - 1) * cosomega - twosqrtaalpha)
    a0 = (A + 1) + (A - 1) * cosomega + twosqrtaalpha
    a1 = -2 * ((A - 1) + (A + 1) * cosomega)
    a2 = (A + 1) + (A - 1) * cosomega - twosqrtaalpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)


def HS(data, gain, freq, sr=48000, Q=1, BW=None, S=None, axis=0):
    omega, sinomega, cosomega, alpha, A = get_intermediate(
        freq, sr, Q=Q, gain=gain, BW=BW, S=S
    )
    twosqrtaalpha = 2 * sqrt(A) * alpha

    b0 = A * ((A + 1) + (A - 1) * cosomega + twosqrtaalpha)
    b1 = -2 * A * ((A - 1) + (A + 1) * cosomega)
    b2 = A * ((A + 1) + (A - 1) * cosomega - twosqrtaalpha)
    a0 = (A + 1) - (A - 1) * cosomega + twosqrtaalpha
    a1 = 2 * ((A - 1) - (A + 1) * cosomega)
    a2 = (A + 1) - (A - 1) * cosomega - twosqrtaalpha

    b, a = (b0, b1, b2), (a0, a1, a2)
    return lfilter(b, a, data, axis)
