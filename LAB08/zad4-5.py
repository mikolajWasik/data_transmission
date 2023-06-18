from math import sin, cos, pi, sqrt, log10, ceil
import matplotlib.pyplot as plt
from numpy.fft import fft
import cmath



fs = 300000 #częstotliwośc próbkowania w kHz
Ts = 1 / fs
Bprim = 420 #liczba znaków w ciągu bitowym
Tb = 0.005 #okres trwania jednego znaku ciągu bitowego w sekundach
Tc = Tb * Bprim #okres całkowity w s
Tc = round(Tc)
W = 100
fn = W * (1/Tb)
fn1 = (W + 1)/Tb
fn2 = (W + 2)/Tb
A1 = 2
A2 = 8

N = Tc * fs
t = []
S_Bprim = []
zA = []
zP = []
zF = []
MzA = []
MzP = []
MzF = []
MdBzA = []
MdBzP = []
MdBzF = []
B3dB = []
B6dB = []
B12dB = []


def S2BS(napis):
    napisBinarnie = []
    strumienBitowy = []

    for i in napis:
        znakDziesietnie = ord(i)
        znakBinarnie = bin(znakDziesietnie)
        znakBinarnieLista = list(znakBinarnie)
        for j in range(100):
            if len(znakBinarnieLista) > 7:
                znakBinarnieLista.pop(0)
            elif len(znakBinarnieLista) < 7:
                znakBinarnieLista.insert(0, '0')
            else:
                break
        znakBinarnieLista = ''.join(str(cyfra) for cyfra in znakBinarnieLista)
        napisBinarnie.append(znakBinarnieLista)
    napisBinarnie = ''.join(znak for znak in napisBinarnie)
    strumienBitowy = [int(znak) for znak in napisBinarnie]

    return list(strumienBitowy)


b = S2BS('probujenapisacstringodlugosciszescdziesiatznakowalesieniezmieszczewiecobetne')
    

for i in range(60):
    TMP_Tb = 0
    for j in range(fs):
        if TMP_Tb == Tb:
            break
        elif TMP_Tb < Tb:
            S_Bprim.append(b[i])
            TMP_Tb += 1/fs
    

for i in range(len(S_Bprim)):
    t.append(i / fs)
    if S_Bprim[i] == 0:
        zA.append(A1 * sin(2 * pi * fn * t[i]))
        zP.append(sin(2 * pi * fn * t[i]))
        zF.append(sin(2 * pi * fn1 * t[i]))
    elif S_Bprim[i] == 1:
        zA.append(A2 * sin(2 * pi * fn * t[i]))
        zP.append(sin(2 * pi * fn * t[i] + pi))
        zF.append(sin(2 * pi * fn2 * t[i]))


zAfft = fft(zA)
zPfft = fft(zP)
zFfft = fft(zF)


for i in range(len(S_Bprim)):
    MzA.append(sqrt((zAfft[i].real * zAfft[i].real) + (zAfft[i].imag * zAfft[i].imag)))
    MdBzA.append(10 * log10(MzA[i]))

    MzP.append(sqrt((zPfft[i].real * zPfft[i].real) + (zPfft[i].imag * zPfft[i].imag)))
    MdBzP.append(10 * log10(MzP[i]))

    MzF.append(sqrt((zFfft[i].real * zFfft[i].real) + (zFfft[i].imag * zFfft[i].imag)))
    MdBzF.append(10 * log10(MzF[i]))

    B3dB.append(3)
    B6dB.append(6)
    B12dB.append(12)


plt.subplot(3, 1, 1)
plt.plot(t, MdBzA)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title("M\' dla ASK")
plt.xlabel("f[Hz]")
plt.ylabel("dB")

plt.subplot(3, 1, 2)
plt.plot(t, MdBzP)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title("M\' dla PSK")
plt.xlabel("f[Hz]")
plt.ylabel("dB")

plt.subplot(3, 1, 3)
plt.plot(t, MdBzF)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title("M\' dla FSK")
plt.xlabel("f[Hz]")
plt.ylabel("dB")
plt.show()
