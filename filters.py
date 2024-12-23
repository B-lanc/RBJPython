from scipy.signal import lfilter
import math

get_A = lambda dbGain: 10 ** (dbGain / 40)
get_Omega = lambda f, sr: 2 * math.pi * f / sr
sin = math.sin
cos = math.cos
get_alpha = lambda omega, Q: sin(omega) / 2 / Q


def formCoefficients(b0, b1, b2, a0, a1, a2):
    return (b0 / a0, b1 / a0, b2 / a0), (a1 / a0, a2 / a0)


def LPF(data, freq, sr=48000, Q=1, axis=0):
    omega = get_Omega(freq, sr)
    cosomega = cos(omega)
    alpha = get_alpha(omega0, Q)
    b0 = (1 - cosomega) / 2
    b1 = 1 - cosomega
    b2 = (1 - cosomega) / 2
    a0 = 1 + alpha
    a1 = -2 * cosomega
    a2 = 1 - alpha

    b, a = formCoefficients(b0, b1, b2, a0, a1, a2)

    return lfilter(b, a, daat, axis)
