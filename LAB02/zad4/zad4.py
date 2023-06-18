import math as m
import matplotlib.pyplot
#zadanie 4 - wzór 4


fs = 22050 #podanie częstotliwości w Hz
Ts = 1 / fs
Tc = 1 #podanie okresu w s

N = round(Tc / Ts)

t1 = []
t2 = []
t3 = []
b1 = []
b2 = []
b3 = []


fb1 = open("probki_b1.txt", 'a')

for i in range(0, N):
	b1_suma = 0

	t1.append(i / fs)

	for h in range(1,3):
		b1_suma = b1_suma + ((m.sin(6 * m.pi * t1[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t1[i])))

	b1.append(b1_suma)

	fb1.write("czas: " + str(t1[i]) + '\t' + "wynik próbki: " + str(b1[i]) + "\n")

fb1.close


fb2 = open("probki_b2.txt", 'a')

for i in range(0, N):
	b2_suma = 0

	t2.append(i / fs)

	for h in range(1,7):
		b2_suma = b2_suma + ((m.sin(6 * m.pi * t2[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t2[i])))

	b2.append(b2_suma)

	fb2.write("czas: " + str(t2[i]) + '\t' + "wynik próbki: " + str(b2[i]) + "\n")

fb2.close


fb3 = open("probki_b3.txt", 'a')

for i in range(0, N):
	b3_suma = 0

	t3.append(i / fs)

	for h in range(1,27):
		b3_suma = b3_suma + ((m.sin(6 * m.pi * t3[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t3[i])))

	b3.append(b3_suma)

	fb3.write("czas: " + str(t3[i]) + '\t' + "wynik próbki: " + str(b3[i]) + "\n")

fb3.close


matplotlib.pyplot.plot(t1, b1)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('b1(t)')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(t2, b2)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('b2(t)')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(t3, b3)
matplotlib.pyplot.xlabel('t[s]')
matplotlib.pyplot.ylabel('b3(t)')
matplotlib.pyplot.show()
