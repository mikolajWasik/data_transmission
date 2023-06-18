import numpy as np

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

b = S2BS('msg')
print("Oryginalny ciąg bitów: ", b, "\n")

for i in range(len(b) - 11):
    if len(b) > 11:
        b.pop(-1)
print("Ciąg bitów przycięty do pierwszych 11: ", b)

I = np.eye(11)
P = np.array([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1],
     [1, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]])
G = np.hstack((P, I))

c = b @ G
c %= 2

print("Słowo zakodowane bez błędu:", c)

Ih = np.eye(4)
H = np.hstack((Ih, P.T))

s = c @ H.T
s %= 2
S = s[0] * 2 ** 0 + s[1] * 2 ** 1 + s[2] * 2 ** 2 + s[3] * 2 ** 3

if S == 0:
    print("\nNie wykryto błędu")
    print("Zdekodowane słowo: ", c[4:])
