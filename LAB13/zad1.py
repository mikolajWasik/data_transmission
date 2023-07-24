from math import sin, cos, pi, sqrt, log10, ceil
import matplotlib.pyplot as plt
import binascii



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


def koder_Hamming_74(b):
    c = []
    for i in range(int(len(b)/4)):
        X = [0, 0, b[0], 0, b[1], b[2], b[3]]
        X[0] = (((X[2] + X[4]) % 2) + X[6]) % 2
        X[1] = (((X[2] + X[5]) % 2) + X[6]) % 2
        X[3] = (((X[4] + X[5]) % 2) + X[6]) % 2

        xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
        xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
        S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2
        if S:
            if X[S - 1] == 1:
                X[S - 1] = 0

                xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
                xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
                S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2

                if S:
                    print("przynajmniej 2 bity uszkodzone; trzeba przesłać wiadomość ponownie")
                    break
            else:
                X[S - 1] = 1

                xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
                xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
                S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2

                if S:
                    print("przynajmniej 2 bity uszkodzone; trzeba przesłać wiadomość ponownie")
                    break

        for bit in range(7):
            c.append(X[bit])

        for iterat in range(4):
            b.pop(0)

    return c


def modulator(c, modulacja):        #ogarnąć niezbędne do modulacji i demodulacji zmienne
    #t.append(i / fs)
    for bit in c:
        if modulacja == ASK:
            if bit == 0:
                x.append(A1 * sin(2 * pi * fn * t[i]))
            elif bit == 1:
                x.append(A2 * sin(2 * pi * fn * t[i]))
        elif modulacja == PSK:
            if bit == 0:
                x.append(sin(2 * pi * fn * t[i]))
            elif bit == 1:
                x.append(sin(2 * pi * fn * t[i] + pi))
        elif modulacja == FSK:
            if bit == 0:
                x.append(sin(2 * pi * fn1 * t[i]))
            elif bit == 1:
                x.append(sin(2 * pi * fn2 * t[i]))

    return x


def demodulator(y, modulacja):
    pass


def dekoder_Hamming_74(cprim):
    bprim = []
    for fragment in range(int(len(cprim)/7)):
        bprim.append(cprim[2])
        bprim.append(cprim[4])
        bprim.append(cprim[5])
        bprim.append(cprim[6])

        for i in range(7):
            cprim.pop(0)

    return bprim


def BS2S(bprim):
    msgchar = []
    for litera in range(int(len(bprim)/7)):
        temp = []
        for i in range(7):
            temp.append(bprim[i])
        literaint = int(''.join(str(x) for x in temp), base=2)
        msgchar.append(chr(literaint))

        for i in range(7):
            bprim.pop(0)

    msg = ""
    for znak in msgchar:
        msg += znak

    return msg


msg = 'kozaczek'

b = S2BS(msg)

c = koder_Hamming_74(b)

x = modulator(c, ASK)

cprim = demodulator(x, ASK)

bprim = dekoder_Hamming_74(cprim)

msgprim = BS2S(bprim)
