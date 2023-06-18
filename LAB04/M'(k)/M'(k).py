import math as m
import matplotlib.pyplot as pl


#numery wybranych z lab02 wzorów:
#zad1 - 3
#zad2 - 7
#zad3 - 3
#zad4 - 4


fs = 1000 #podanie czestotliwosci w Hz
Ts = 1 / fs
Tc = 1 #podanie okresu w s

N = round(Tc / Ts)

t = []
s1 = []
s2 = []
x = []
XRe = []
XIm = []
M = []
Mdec = []

A1 = 1.0
A2 = 0.5
f1 = 25
f2 = 66
fi1 = 0
fi2 = 0


for i in range(0, N):

	t.append(i / fs)
	s1.append(A1 * m.sin(2 * m.pi * f1 * t[i] + fi1))
	s2.append(A2 * m.sin(2 * m.pi * f2 * t[i] + fi2))
	x.append(s1[i] + s2[i])


fMdec = open("probki_M'.xlsx", 'a')

for i in range(0, N):

	XRe_suma = 0
	XIm_suma = 0

	for j in range(0, N):
		XRe_suma += x[j] * m.cos((-2 * m.pi * i * j)/N)
		XIm_suma += x[j] * m.sin((-2 * m.pi * i * j)/N)

	XRe.append(XRe_suma)
	XIm.append(XIm_suma)
	M.append(m.sqrt((XRe[i])**2 + (XIm[i])**2))
	Mdec.append(10 * m.log10(M[i]))
	M[i] = M[i] * (2/N)

	fMdec.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdec[i]) + "\n")


fMdec.close


pl.plot(t, Mdec)
pl.title('M\'[k]')
pl.xlabel('f[Hz]')
pl.ylabel('dB')
pl.show()
