from math import sin, cos, pi
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zP1 = []
zP2 = []
zP3 = []

fm = 1000
fn = 10000
kP1 = 0.5
kP2 = 0.5 * pi
kP3 = 10 * pi


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zP1.append(cos(2 * pi * fn * t[i] + kP1 * m[i]))
	zP2.append(cos(2 * pi * fn * t[i] + kP2 * m[i]))
	zP3.append(cos(2 * pi * fn * t[i] + kP3 * m[i]))



plt.subplot(4, 1, 1)
plt.plot(t, m)
plt.title('m(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 2)
plt.plot(t, zP1)
plt.title('zP1(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 3)
plt.plot(t, zP2)
plt.title('zP2(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 4)
plt.plot(t, zP3)
plt.title('zP3(t)')
plt.xlabel('t[s]')
plt.ylabel('A')
plt.show()
