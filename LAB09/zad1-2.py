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
S_Bprim = []
zA, zP, zF = [], [], []
xzA, xzP, x1zF, x2zF = [], [], [], []
pzA, pzP, p1zF, p2zF = [], [], [], []
czA, czP, czF = [], [], []


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
    

for i in range(10):
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

for i in range(len(S_Bprim)):
    xzA.append(zA[i] * (5 * sin(2 * pi * fn * t[i]))) #5 jako średnia amplituda sygnału wejściowego, bo w ASK są dwie amplitudy
    xzP.append(zP[i] * (1 * sin(2 * pi * fn * t[i])))
    x1zF.append(zF[i] * (1 * sin(2 * pi * fn1 * t[i])))
    x2zF.append(zF[i] * (1 * sin(2 * pi * fn2 * t[i])))


for i in range(10):
    ASKsuma = 0
    PSKsuma = 0
    FSK1suma = 0
    FSK2suma = 0
    for j in range(100):
        ASKsuma += xzA[i * 100 + j] * (1/1000)
        PSKsuma += xzP[i * 100 + j] * (1/1000)
        FSK1suma += x1zF[i * 100 + j] * (1/1000)
        FSK2suma += x2zF[i * 100 + j] * (1/1000)

        pzA.append(ASKsuma)
        pzP.append(PSKsuma)
        p1zF.append(FSK1suma)
        p2zF.append(FSK2suma)


        if pzA[i * 100 + j] > 0.5:
            czA.append(1)
        else:
            czA.append(0)

        if pzP[i * 100 + j] < 0:
            czP.append(1)
        else:
            czP.append(0)

        if p2zF[i * 100 + j] - p1zF[i * 100 + j] > 0:
            czF.append(1)
        else:
            czF.append(0)


plt.subplot(2, 2, 1)
plt.plot(t, zA)
plt.title("ASK")
plt.ylabel("zA(t)")

plt.subplot(2, 2, 3)
plt.plot(t, xzA)
plt.title("xASK")
plt.xlabel("t[s]")
plt.ylabel("x(t)")

plt.subplot(2, 2, 2)
plt.plot(t, pzA)
plt.title("pASK")
plt.ylabel("p(t)")

plt.subplot(2, 2, 4)
plt.plot(t, czA)
plt.title("cASK")
plt.xlabel("t[s]")
plt.ylabel("c(t)")
plt.show()


plt.subplot(2, 2, 1)
plt.plot(t, zP)
plt.title("PSK")
plt.ylabel("zP(t)")

plt.subplot(2, 2, 3)
plt.plot(t, xzP)
plt.title("xPSK")
plt.xlabel("t[s]")
plt.ylabel("x(t)")

plt.subplot(2, 2, 2)
plt.plot(t, pzP)
plt.title("pPSK")
plt.ylabel("p(t)")

plt.subplot(2, 2, 4)
plt.plot(t, czP)
plt.title("cPSK")
plt.xlabel("t[s]")
plt.ylabel("c(t)")
plt.show()


plt.subplot(3, 2, 1)
plt.plot(t, zF)
plt.title("FSK")
plt.ylabel("zF(t)")

plt.subplot(3, 2, 3)
plt.plot(t, x1zF)
plt.title("x1FSK")
plt.ylabel("x1(t)")

plt.subplot(3, 2, 5)
plt.plot(t, x2zF)
plt.title("x2FSK")
plt.xlabel("t[s]")
plt.ylabel("x2(t)")

plt.subplot(3, 2, 2)
plt.plot(t, p1zF)
plt.title("p1FSK")
plt.ylabel("p1(t)")

plt.subplot(3, 2, 4)
plt.plot(t, p2zF)
plt.title("p2FSK")
plt.ylabel("p2(t)")

plt.subplot(3, 2, 6)
plt.plot(t, czF)
plt.title("cFSK")
plt.xlabel("t[s]")
plt.ylabel("c(t)")
plt.show()
