from math import sin, cos, pi
import matplotlib.pyplot as plt



fs = 200000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.01 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zAsuche = []
zA = []
zPsuche = []
zP = []
zFsuche = []
zF = []

fm = 100
fn = 200
kA = 1


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zAsuche.append(cos(2 * pi * fn * t[i]))
	zA.append((kA * m[i] + 1) * cos(2 * pi * fn * t[i]))


plt.subplot(3, 1, 1)
plt.plot(t, m)
plt.title('m(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(3, 1, 2)
plt.plot(t, zAsuche)
plt.title('zA(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(3, 1, 3)
plt.plot(t, zA)
plt.title('zA(t) zmodulowane')
plt.xlabel('t[s]')
plt.ylabel('A')
plt.show()
