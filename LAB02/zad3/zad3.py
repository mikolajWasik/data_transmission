import math as m
import matplotlib.pyplot
#zadanie 3 - wzór 3


fs = 10000 #podanie częstotliwości w Hz
Ts = 1 / fs
Tc = 3.1 #podanie okresu w s

N = round(Tc / Ts)

t = []
u = []


fu = open("probki_u.txt", 'a')


for i in range(0, N):

	t.append(i / fs)

	if 0 <= t[i] < 1.2:
		u.append((-t[i] ** 2 + 0.5) * m.sin(30 * m.pi * t[i]) * m.log2(t[i] ** 2 + 1))
	elif 1.2 <= t[i] < 2:
		u.append((1/t[i]) * 0.8 * m.sin(24 * m.pi * t[i]) - 0.1 * t[i])
	elif 2 <= t[i] < 2.4:
		u.append((abs(m.sin(2 * m.pi * t[i] ** 2))) ** 0.8)
	else:
		u.append(0.23 * m.sin(20 * m.pi * t[i]) * m.sin(12 * m.pi * t[i]))

	fu.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(u[i]) + "\n")

fu.close


matplotlib.pyplot.plot(t, u)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('u(t)')
matplotlib.pyplot.show()
