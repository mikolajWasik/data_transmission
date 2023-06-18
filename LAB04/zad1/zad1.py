import math as m
import matplotlib.pyplot as pl
from numpy import fft
import time


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
x = []
XRe = []
XIm = []
Mx = []
Mdecx = []

f = 200
fi = 0


for i in range(0, N):

	t.append(i / fs)
	x.append(0.2 * m.log10(t[i] ** 4 + 8) * m.sin(2 * m.pi * f * t[i] ** 2 + fi) + m.cos(t[i] / 8))


fMx = open("probki_Mx'.xlsx", 'a')		#w zależności od potrzeby będę zakomentowywał tylko jedno z dwóch poleceń - tego lub tego poniżej
#fMdecx = open("probki_Mdecx'.xlsx", 'a')
startDFT = time.time()

for i in range(0, N):

	XRe_suma = 0
	XIm_suma = 0

	for j in range(0, N):
		XRe_suma += x[j] * m.cos((-2 * m.pi * i * j)/N)
		XIm_suma += x[j] * m.sin((-2 * m.pi * i * j)/N)

	XRe.append(XRe_suma)
	XIm.append(XIm_suma)
	Mx.append(m.sqrt((XRe[i])**2 + (XIm[i])**2))
	#Mdecx.append(10 * m.log10(Mx[i]))		#to samo co powyżej
	Mx[i] = Mx[i] * (2/N)

	fMx.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mx[i]) + "\n")
	#fMdecx.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdecx[i]) + "\n")

stopDFT = time.time()
fMx.close		#to samo co powyżej
#fMdecx.close


startFFT = time.time()
y = fft.fft(x)
stopFFT = time.time()
#print(y)


print("Czas obliczania DFT: ", stopDFT - startDFT, " s")
print("Czas obliczania FFT: ", stopFFT - startFFT, " s")


pl.plot(t, Mx)				#ta sama sytuacja co powyżej tyle, że do całego bloku komend dot. rysowania wykresu
pl.title('M(k)')
pl.xlabel('f[Hz]')
pl.ylabel('A')
pl.show()

#pl.plot(t, Mdecx)
#pl.title('M\'(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('dB')
#pl.show()

