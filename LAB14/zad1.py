from math import sin, cos, pi
import matplotlib.pyplot as plt



#zmienne do modulacji i demodulacji:
fs = 1000    #częstotliwośc próbkowania w Hz
Tb = 0.1 #okres trwania jednego znaku ciągu bitowego w sekundach
W = 2
fn = W * (1/Tb)
fn1 = (W + 1)/Tb
fn2 = (W + 2)/Tb
A1 = 1
A2 = 0.5

t = []


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


def modulator(c, modulacja):
    x = []
    cDlugi = []

    for i in range(len(c)): #zwielokrotniamy bity ze strumienia c żeby pozbyć się przekłamań przy demodulacji
        TMP_Tb = 0
        for j in range(fs):
            if TMP_Tb == Tb:
                break
            elif TMP_Tb < Tb:
                cDlugi.append(c[i])
                TMP_Tb += 1/fs

    for i in range(len(cDlugi)):
        t.append(i / fs)
        if modulacja == "ASK":
            if cDlugi[i] == 0:
                x.append(A1 * sin(2 * pi * fn * t[i]))
            elif cDlugi[i] == 1:
                x.append(A2 * sin(2 * pi * fn * t[i]))
        elif modulacja == "PSK":
            if cDlugi[i] == 0:
                x.append(sin(2 * pi * fn * t[i]))
            elif cDlugi[i] == 1:
                x.append(sin(2 * pi * fn * t[i] + pi))
        elif modulacja == "FSK":
            if cDlugi[i] == 0:
                x.append(sin(2 * pi * fn1 * t[i]))
            elif cDlugi[i] == 1:
                x.append(sin(2 * pi * fn2 * t[i]))

    return x


def demodulator(y, modulacja):  #demodulacja musi być taka sama jak modulacja
    yX1 = []
    yX2 = []
    for i in range(len(y)):
        if modulacja == "ASK":
            yX1.append(y[i] * (0.75 * sin(2 * pi * fn * t[i]))) #0.75 jako średnia amplituda sygnału wejściowego, bo w ASK są dwie amplitudy
        elif modulacja == "PSK":
            yX1.append(y[i] * (1 * sin(2 * pi * fn * t[i])))
        elif modulacja == "FSK":
            yX1.append(y[i] * (1 * sin(2 * pi * fn1 * t[i])))
            yX2.append(y[i] * (1 * sin(2 * pi * fn2 * t[i])))

    yCalka1 = []
    yCalka2 = []
    yDemod = []
    for i in range(int(len(y)/100)):
        ySuma1 = 0
        ySuma2 = 0
        for j in range(int(len(y)/(len(y) / 100))):
            if modulacja == "ASK":
                ySuma1 += yX1[i * int(len(y)/(len(y) / 100)) + j] * (1/len(y))
            elif modulacja == "PSK":
                ySuma1 += yX1[i * int(len(y)/(len(y) / 100)) + j] * (1/len(y))
            elif modulacja == "FSK":
                ySuma1 += yX1[i * int(len(y)/(len(y) / 100)) + j] * (1/len(y))
                ySuma2 += yX2[i * int(len(y)/(len(y) / 100)) + j] * (1/len(y))

            if modulacja == "ASK":
                yCalka1.append(ySuma1)
            elif modulacja == "PSK":
                yCalka1.append(ySuma1)
            elif modulacja == "FSK":
                yCalka1.append(ySuma1)
                yCalka2.append(ySuma2)

            if modulacja == "ASK":
                if yCalka1[i * int(len(y)/(len(y) / 100)) + j] > 0.5:
                    yDemod.append(1)
                else:
                    yDemod.append(0)

            elif modulacja == "PSK":
                if yCalka1[i * int(len(y)/(len(y) / 100)) + j] < 0:
                    yDemod.append(1)
                else:
                    yDemod.append(0)

            elif modulacja == "FSK":
                if yCalka2[i * int(len(y)/(len(y) / 100)) + j] - yCalka1[i * int(len(y)/(len(y) / 100)) + j] > 0:
                    yDemod.append(1)
                else:
                    yDemod.append(0)

    zwrot = []      #naprawienie zakłamań
    for i in range(int((len(y) / 100))):
        waga = 0
        for j in range(int(len(y)/(len(y) / 100))):
            waga += yDemod[i * int(len(y)/len(y) * 0.01) + j]

        if waga > 50:
            for k in range(int(len(y)/(len(y) / 100))):
                zwrot.append(1)
        else:
            for k in range(int(len(y)/(len(y) / 100))):
                zwrot.append(0)

    ostateczny = []     #ponowne skrócenie ciągu bitowego do oryginalne długości
    for i in range(int(len(zwrot) * 0.01)):
        ostateczny.append(zwrot[i * 100])

    return ostateczny


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


#zad1
msg = 'kozaczek'
print("Napis wejściowy:", msg)
b = S2BS(msg)
print("\nNapis przekształcony na strumień bitowy:\n", b)
c = koder_Hamming_74(b)
print("\nStrumień bitowy zakodowany koderem Hamminga (7, 4):\n", c)
x = modulator(c, "ASK")
print("\nZakodowany strumień po modulacji:\n", x)
cprim = demodulator(x, "ASK")
print("\nZmodulowany strumień po demodulacji:\n", cprim)
bprim = dekoder_Hamming_74(cprim)
print("\nZdemodulowany strumień po dekodowaniu:\n", bprim)
msgprim = BS2S(bprim)
print("\nZdekodowany strumień zamieniony na napis wyjściowy: ", msgprim)
