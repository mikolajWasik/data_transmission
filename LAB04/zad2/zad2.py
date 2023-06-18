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
y = []
z = []
v = []
XRey = []
XImy = []
XRez = []
XImz = []
XRev = []
XImv = []
My = []
Mdecy = []
Mz = []
Mdecz = []
Mv = []
Mdecv = []

f = 200
fi = 0


for i in range(0, N):

	t.append(i / fs)
	x.append(0.2 * m.log10(t[i] ** 4 + 8) * m.sin(2 * m.pi * f * t[i] ** 2 + fi) + m.cos(t[i] / 8))
	y.append(m.sin(m.pi * t[i]) * m.sin(2 * x[i] * m.pi * t[i]))
	z.append(abs(y[i] ** (1/2) - 3 * x[i]))
	v.append(x[i] * y[i] ** 2 - z[i] * m.cos(x[i]))


fMy = open("probki_My'.xlsx", 'a')		#w zależności od potrzeby będę zakomentowywał tylko jedno z pary poleceń - tego z 'dec' lub bez
#fMdecy = open("probki_Mdecy'.xlsx", 'a')

startDFTy = time.time()

for i in range(0, N):

	XRey_suma = 0
	XImy_suma = 0

	for j in range(0, N):
		XRey_suma += y[j] * m.cos((-2 * m.pi * i * j)/N)
		XImy_suma += y[j] * m.sin((-2 * m.pi * i * j)/N)

	XRey.append(XRey_suma)
	XImy.append(XImy_suma)
	My.append(m.sqrt((XRey[i])**2 + (XImy[i])**2))
	#Mdecy.append(10 * m.log10(My[i]))		#to samo co powyżej
	My[i] = My[i] * (2/N)

	fMy.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(My[i]) + "\n")
	#fMdecy.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdecy[i]) + "\n")

stopDFTy = time.time()
fMy.close		#to samo co powyżej
#fMdecy.close


fMz = open("probki_Mz'.xlsx", 'a')
#fMdecz = open("probki_Mdecz'.xlsx", 'a')

startDFTz = time.time()

for i in range(0, N):

	XRez_suma = 0
	XImz_suma = 0

	for j in range(0, N):
		XRez_suma += z[j] * m.cos((-2 * m.pi * i * j)/N)
		XImz_suma += z[j] * m.sin((-2 * m.pi * i * j)/N)

	XRez.append(XRez_suma)
	XImz.append(XImz_suma)
	Mz.append(m.sqrt((XRez[i])**2 + (XImz[i])**2))
	#Mdecz.append(10 * m.log10(Mz[i]))		#to samo co powyżej
	Mz[i] = Mz[i] * (2/N)

	fMz.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mz[i]) + "\n")
	#fMdecz.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdecz[i]) + "\n")

stopDFTz = time.time()
fMz.close		#to samo co powyżej
#fMdecz.close


fMv = open("probki_Mv'.xlsx", 'a')
#fMdecv = open("probki_Mdecv'.xlsx", 'a')

startDFTv = time.time()

for i in range(0, N):

	XRev_suma = 0
	XImv_suma = 0

	for j in range(0, N):
		XRev_suma += v[j] * m.cos((-2 * m.pi * i * j)/N)
		XImv_suma += v[j] * m.sin((-2 * m.pi * i * j)/N)

	XRev.append(XRev_suma)
	XImv.append(XImv_suma)
	Mv.append(m.sqrt((XRev[i])**2 + (XImv[i])**2))
	#Mdecv.append(10 * m.log10(Mv[i]))		#to samo co powyżej
	Mv[i] = Mv[i] * (2/N)

	fMv.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mv[i]) + "\n")
	#fMdecv.write("czas: " + str(t[i]) + '\t' + "wynik probki: " + str(Mdecv[i]) + "\n")

stopDFTv = time.time()
fMv.close		#to samo co powyżej
#fMdecv.close


startFFTy = time.time()
a = fft.fft(y)
stopFFTy = time.time()
print(a)

print("Czas obliczania DFT dla y: ", stopDFTy - startDFTy, " s")
print("Czas obliczania FFT dla y: ", stopFFTy - startFFTy, " s")


startFFTz = time.time()
b = fft.fft(z)
stopFFTz = time.time()
print(b)

print("Czas obliczania DFT dla z: ", stopDFTz - startDFTz, " s")
print("Czas obliczania FFT dla z: ", stopFFTz - startFFTz, " s")


startFFTv = time.time()
c = fft.fft(v)
stopFFTv = time.time()
print(c)

print("Czas obliczania DFT dla v: ", stopDFTv - startDFTv, " s")
print("Czas obliczania FFT dla v: ", stopFFTv - startFFTv, " s")


pl.plot(t, My)				#ta sama sytuacja co powyżej tyle, że do całego bloku komend dot. rysowania wykresu
pl.title('M(k)')
pl.xlabel('f[Hz]')
pl.ylabel('A')
pl.show()

#pl.plot(t, Mdecy)
#pl.title('M\'(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('dB')
#pl.show()


pl.plot(t, Mz)
pl.title('M(k)')
pl.xlabel('f[Hz]')
pl.ylabel('A')
pl.show()

#pl.plot(t, Mdecz)
#pl.title('M\'(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('dB')
#pl.show()


pl.plot(t, Mv)
pl.title('M(k)')
pl.xlabel('f[Hz]')
pl.ylabel('A')
pl.show()

#pl.plot(t, Mdecv)
#pl.title('M\'(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('dB')
#pl.show()
