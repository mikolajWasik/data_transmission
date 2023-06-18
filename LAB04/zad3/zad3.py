import math as m
import matplotlib.pyplot as pl
from numpy import fft
import time


#numery wybranych z lab02 wzorów:
#zad1 - 3
#zad2 - 7
#zad3 - 3
#zad4 - 4


fs = 2000 #podanie czestotliwosci w Hz
Ts = 1 / fs
Tc = 3.1 #podanie okresu w s

N = round(Tc / Ts)

t = []
u = []
XRe = []
XIm = []
Mu = []
Mdecu = []


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


fMu = open("probki_Mu'.xlsx", 'a')		#w zależności od potrzeby będę zakomentowywał tylko jedno z pary poleceń - tego z 'dec' lub bez
#fMdecu = open("probki_Mdecu'.xlsx", 'a')

startDFT = time.time()

for i in range(0, N):

	XRe_suma = 0
	XIm_suma = 0

	for j in range(0, N):
		XRe_suma += u[j] * m.cos((-2 * m.pi * i * j)/N)
		XIm_suma += u[j] * m.sin((-2 * m.pi * i * j)/N)

	XRe.append(XRe_suma)
	XIm.append(XIm_suma)
	Mu.append(m.sqrt((XRe[i])**2 + (XIm[i])**2))
	#Mdecu.append(10 * m.log10(Mu[i]))		#to samo co powyżej
	Mu[i] = Mu[i] * (2/N)

	fMu.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mu[i]) + "\n")
	#fMdecu.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdecu[i]) + "\n")

stopDFT = time.time()
fMu.close		#to samo co powyżej
#fMdecu.close


startFFT = time.time()
a = fft.fft(u)
stopFFT = time.time()
print(a)

print("Czas obliczania DFT: ", stopDFT - startDFT, " s")
print("Czas obliczania FFT: ", stopFFT - startFFT, " s")


pl.plot(t, Mu)				#ta sama sytuacja co powyżej tyle, że do całego bloku komend dot. rysowania wykresu
pl.title('M(k)')
pl.xlabel('f[Hz]')
pl.ylabel('A')
pl.show()

#pl.plot(t, Mdecu)
#pl.title('M\'(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('dB')
#pl.show()
