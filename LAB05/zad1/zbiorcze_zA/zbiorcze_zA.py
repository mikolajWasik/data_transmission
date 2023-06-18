from math import sin, cos, pi
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zA1 = []
zA2 = []
zA3 = []

fm = 1000
fn = 10000
kA1 = 0.5
kA2 = 7
kA3 = 120


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zA1.append((kA1 * m[i] + 1) * cos(2 * pi * fn * t[i]))
	zA2.append((kA2 * m[i] + 1) * cos(2 * pi * fn * t[i]))
	zA3.append((kA3 * m[i] + 1) * cos(2 * pi * fn * t[i]))



plt.subplot(4, 1, 1)
plt.plot(t, m)
plt.title('m(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 2)
plt.plot(t, zA1)
plt.title('zA1(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 3)
plt.plot(t, zA2)
plt.title('zA2(t)')
plt.xlabel('t[s]')
plt.ylabel('A')

plt.subplot(4, 1, 4)
plt.plot(t, zA3)
plt.title('zA3(t)')
plt.xlabel('t[s]')
plt.ylabel('A')
plt.show()
