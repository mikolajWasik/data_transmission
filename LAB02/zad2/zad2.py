import math as m
import matplotlib.pyplot
#zadanie 2 - wzór 7


fs = 10000 #podanie częstotliwości w Hz
Ts = 1 / fs
Tc = 4 #podanie okresu w s

N = round(Tc / Ts)

t = []
x = []
y = []
z = []
v = []

f = 200
fi = 0

fx = open("probki_x.txt", 'a')
fy = open("probki_y.txt", 'a')
fz = open("probki_z.txt", 'a')
fv = open("probki_v.txt", 'a')

for i in range(0, N):

	t.append(i / fs)
	x.append(0.2 * m.log10(t[i] ** 4 + 8) * m.sin(2 * m.pi * f * t[i] ** 2 + fi) + m.cos(t[i] / 8))
	y.append(m.sin(m.pi * t[i]) * m.sin(2 * x[i] * m.pi * t[i]))
	z.append(abs(y[i] ** (1/2) - 3 * x[i]))
	v.append(x[i] * y[i] ** 2 - z[i] * m.cos(x[i]))
	fy.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(y[i]) + "\n")
	fz.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(z[i]) + "\n")
	fv.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(v[i]) + "\n")

fx.close
fy.close
fz.close
fv.close

matplotlib.pyplot.plot(t, y)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('y(t)')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(t, z)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('z(t)')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(t, v)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('v(t)')
matplotlib.pyplot.show()
