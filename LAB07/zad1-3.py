from math import sin, cos, pi, sqrt, log10, ceil
import matplotlib.pyplot as plt



fs = 1000 #częstotliwośc próbkowania w kHz
Ts = 1 / fs
Bprim = 10 #liczba znaków w ciągu bitowym
Tb = 1/10 #okres trwania jednego znaku ciągu bitowego w sekundach
Tc = Tb * Bprim #okres całkowity w s
Tc = round(Tc)
W = 2
fn = W * (1/Tb)
fn1 = (W + 1)/Tb
fn2 = (W + 2)/Tb
A1 = 2
A2 = 8

N = Tc * fs
t = []
S_B = []
S_Bprim = []
zA = []
zP = []
zF = []


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


b = S2BS('abc')
#B = len(b)
#for i in range(B):
#    TMP_Tb = 0
#    for j in range(fs):
#        if TMP_Tb == Tb:
#            break
#        elif TMP_Tb < Tb:
#            S_B.append(b[i])
#            TMP_Tb += 1/fs     #tu sobie zrobiłem test dla ogólnego B a niżej dla B = 10 z zad3
    

for i in range(10):
    TMP_Tb = 0
    for j in range(fs):
        if TMP_Tb == Tb:
            break
        elif TMP_Tb < Tb:
            S_Bprim.append(b[i])
            TMP_Tb += 1/fs
    

for i in range(0, len(S_Bprim)):
    t.append(i / fs)
    if S_Bprim[i] == 0:
	    zA.append(A1 * sin(2 * pi * fn * t[i]))
	    zP.append(sin(2 * pi * fn * t[i]))
	    zF.append(sin(2 * pi * fn1 * t[i]))
    elif S_Bprim[i] == 1:
	    zA.append(A2 * sin(2 * pi * fn * t[i]))
	    zP.append(sin(2 * pi * fn * t[i] + pi))
	    zF.append(sin(2 * pi * fn2 * t[i]))



plt.subplot(4, 1, 1)
plt.plot(t, S_Bprim)
plt.title("Strumień binarny")
plt.xlabel("t[s]")

plt.subplot(4, 1, 2)
plt.plot(t, zA)
plt.title("ASK")
plt.xlabel("t[s]")
plt.ylabel("zA(t)")

plt.subplot(4, 1, 3)
plt.plot(t, zP)
plt.title("PSK")
plt.xlabel("t[s]")
plt.ylabel("zP(t)")

plt.subplot(4, 1, 4)
plt.plot(t, zF)
plt.title("FSK")
plt.xlabel("t[s]")
plt.ylabel("zF(t)")
plt.show()
