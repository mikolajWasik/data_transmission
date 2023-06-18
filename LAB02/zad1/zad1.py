import math as m
import matplotlib.pyplot
#zadanie 1 - wzór 3


fs = 10000 #podanie częstotliwości w Hz
Ts = 1 / fs
Tc = 4 #podanie okresu w s

N = round(Tc / Ts)

x = []
t = []

f = 200
fi = 0

fx = open("probki_x.txt", 'a')

for i in range(0, N):

	t.append(i / fs)
	x.append(0.2 * m.log10(t[i] ** 4 + 8) * m.sin(2 * m.pi * f * t[i] ** 2 + fi) + m.cos(t[i] / 8))
	fx.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(x[i]) + "\n")

fx.close

matplotlib.pyplot.plot(t, x)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('x(t)')
matplotlib.pyplot.show()
