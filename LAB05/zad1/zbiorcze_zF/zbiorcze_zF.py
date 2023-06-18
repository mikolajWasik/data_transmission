from math import sin, cos, pi
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zF1 = []
zF2 = []
zF3 = []

fm = 1000
fn = 10000
kF1 = 0.5
kF2 = 0.5 * pi
kF3 = 50 * pi


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zF1.append(cos(2 * pi * fn * t[i] + (kF1/fm) * m[i]))
	zF2.append(cos(2 * pi * fn * t[i] + (kF2/fm) * m[i]))
	zF3.append(cos(2 * pi * fn * t[i] + (kF3/fm) * m[i]))



plt.subplot(4, 1, 1)
plt.plot(t, m)
plt.title('m(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 2)
plt.plot(t, zF1)
plt.title('zF1(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 3)
plt.plot(t, zF2)
plt.title('zF2(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 4)
plt.plot(t, zF3)
plt.title('zF3(t)')
plt.xlabel('t[s]')
plt.ylabel('A')
plt.show()
