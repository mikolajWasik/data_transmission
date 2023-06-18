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

print("słowo zakodowane bez zmian:")

#na razie w miejscu bitów parzystości wstawiam 0 żeby lista nie miała braków na ich miejscach, a poprawię je niżej
X = [0, 0, b[0], 0, b[1], b[2], b[3]]
X[0] = (((X[2] + X[4]) % 2) + X[6]) % 2
X[1] = (((X[2] + X[5]) % 2) + X[6]) % 2
X[3] = (((X[4] + X[5]) % 2) + X[6]) % 2

print('b: ', b)
print('X: ', X)

xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2
print("numer bitu z błędem: ", S)

print("\nsłowo zakodowane z błędem na bicie nr 6")

X = [0, 0, b[0], 0, b[1], b[2], b[3]]
X[0] = (((X[2] + X[4]) % 2) + X[6]) % 2
X[1] = (((X[2] + X[5]) % 2) + X[6]) % 2
X[3] = (((X[4] + X[5]) % 2) + X[6]) % 2

print('b: ', b)
print('X: ', X)

if X[5] == 1:
    X[5] = 0
else:
    X[5] = 1
print("X z wprowadzonym błędem: ", X)

xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2
print("numer bitu z błędem: ", S)

if S:
    if X[S - 1] == 1:
        X[S - 1] = 0
    else:
        X[S - 1] = 1

xprim0, xprim1, xprim3 = (((X[2] + X[4]) % 2) + X[6]) % 2, (((X[2] + X[5]) % 2) + X[6]) % 2, (((X[4] + X[5]) % 2) + X[6]) % 2
xkreska0, xkreska1, xkreska3 = (X[0] + xprim0) % 2, (X[1] + xprim1) % 2, (X[3] + xprim3) % 2
S = xkreska0 * 2 ** 0 + xkreska1 * 2 ** 1 + xkreska3 * 2 ** 2

if S:
    print("przynajmniej 2 bity uszkodzone; trzeba przesłać wiadomość ponownie")
else:
    print("naprawiony X: ", X)
    print("Bity znaczące (fragment wiadomości): ", X[2], X[4], X[5], X[6])
