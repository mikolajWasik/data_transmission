import math as m
import matplotlib.pyplot as pl


fs = 1000 #podanie częstotliwości w Hz
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

A1 = 1.0
A2 = 0.5
f1 = 25
f2 = 66
fi1 = 0
fi2 = 0


fs1 = open("probki_s1.xlsx", 'a')
fs2 = open("probki_s2.xlsx", 'a')
fx = open("probki_x.xlsx", 'a')

for i in range(0, N):

	t.append(i / fs)
	s1.append(A1 * m.sin(2 * m.pi * f1 * t[i] + fi1))
	s2.append(A2 * m.sin(2 * m.pi * f2 * t[i] + fi2))
	x.append(s1[i] + s2[i])

	fs1.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(s1[i]) + "\n")
	fs2.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(s2[i]) + "\n")
	fx.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(x[i]) + "\n")

fs1.close
fs2.close
fx.close


fXRe = open("probki_XRe.xlsx", 'a')
fXIm = open("probki_XIm.xlsx", 'a')
fM = open("probki_M.xlsx", 'a')

for i in range(0, N):

	XRe_suma = 0
	XIm_suma = 0

	for j in range(0, N):
		XRe_suma += x[j] * m.cos((-2 * m.pi * i * j)/N)
		XIm_suma += x[j] * m.sin((-2 * m.pi * i * j)/N)

	XRe.append(XRe_suma)
	XIm.append(XIm_suma)
	M.append(m.sqrt((XRe[i])**2 + (XIm[i])**2) * (2/N))

	fXRe.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(XRe[i]) + "\n")
	fXIm.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(XIm[i]) + "\n")
	fM.write("czas: " + str(t[i]) + '\t' + "wynik próbki: " + str(M[i]) + "\n")

fXRe.close
fXIm.close
fM.close


pl.plot(t, s1)
pl.title('s1[t]')
pl.xlabel('t[s]')
pl.ylabel('A')
pl.show()

pl.plot(t, s2)
pl.title('s2[t]')
pl.xlabel('t[s]')
pl.ylabel('A')
pl.show()

pl.plot(t, x)
pl.title('x[t] = s1[t] + s2[t]')
pl.xlabel('t[s]')
pl.ylabel('A')
pl.show()

pl.plot(t, M)
pl.title('M[k] = XRe[k] + XIm[k]')
pl.xlabel('f[HZ]')
pl.ylabel('A')
pl.show()
