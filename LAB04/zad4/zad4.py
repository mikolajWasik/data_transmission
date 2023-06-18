import math as m
import matplotlib.pyplot as pl
from numpy import fft
import time


#numery wybranych z lab02 wzorów:
#zad1 - 3
#zad2 - 7
#zad3 - 3
#zad4 - 4


fs = 10000 #podanie czestotliwosci w Hz
Ts = 1 / fs
Tc = 1 #podanie okresu w s

N = round(Tc / Ts)

t1 = []
t2 = []
t3 = []
b1 = []
b2 = []
b3 = []
XReb1 = []
XImb1 = []
XReb2 = []
XImb2 = []
XReb3 = []
XImb3 = []
Mb1 = []
Mdecb1 = []
Mb2 = []
Mdecb2 = []
Mb3 = []
Mdecb3 = []


for i in range(0, N):
	b1_suma = 0

	t1.append(i / fs)

	for h in range(1,3):
		b1_suma = b1_suma + ((m.sin(6 * m.pi * t1[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t1[i])))

	b1.append(b1_suma)

for i in range(0, N):
	b2_suma = 0

	t2.append(i / fs)

	for h in range(1,7):
		b2_suma = b2_suma + ((m.sin(6 * m.pi * t2[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t2[i])))

	b2.append(b2_suma)

for i in range(0, N):
	b3_suma = 0

	t3.append(i / fs)

	for h in range(1,27):
		b3_suma = b3_suma + ((m.sin(6 * m.pi * t3[i] * h ** 2))/((2 * h + 1) ** 2 + m.sin(12 * m.pi * t3[i])))

	b3.append(b3_suma)


#fMb1 = open("probki_Mb1'.xlsx", 'a')		#w zależności od potrzeby będę zakomentowywał tylko jedno z pary poleceń - tego z 'dec' lub bez
fMdecb1 = open("probki_Mdecb1'.xlsx", 'a')

startDFTb1 = time.time()

for i in range(0, N):

	XReb1_suma = 0
	XImb1_suma = 0

	for j in range(0, N):
		XReb1_suma += b1[j] * m.cos((-2 * m.pi * i * j)/N)
		XImb1_suma += b1[j] * m.sin((-2 * m.pi * i * j)/N)

	XReb1.append(XReb1_suma)
	XImb1.append(XImb1_suma)
	Mb1.append(m.sqrt((XReb1[i])**2 + (XImb1[i])**2))
	Mdecb1.append(10 * m.log10(Mb1[i]))		#to samo co powyżej
	#Mb1[i] = Mb1[i] * (2/N)

	#fMb1.write("czas: " + str(t1[i]) + '\t' + "wynik probki: " + str(Mb1[i]) + "\n")
	fMdecb1.write("czas: " + str(t1[i]) + '\t' + "wynik probki: " + str(Mdecb1[i]) + "\n")

stopDFTb1 = time.time()
#fMb1.close		#to samo co powyżej
fMdecb1.close


#fMb2 = open("probki_Mb2'.xlsx", 'a')
fMdecb2 = open("probki_Mdecb2'.xlsx", 'a')

startDFTb2 = time.time()

for i in range(0, N):

	XReb2_suma = 0
	XImb2_suma = 0

	for j in range(0, N):
		XReb2_suma += b2[j] * m.cos((-2 * m.pi * i * j)/N)
		XImb2_suma += b2[j] * m.sin((-2 * m.pi * i * j)/N)

	XReb2.append(XReb2_suma)
	XImb2.append(XImb2_suma)
	Mb2.append(m.sqrt((XReb2[i])**2 + (XImb2[i])**2))
	Mdecb2.append(10 * m.log10(Mb2[i]))		#to samo co powyżej
	#Mb2[i] = Mb2[i] * (2/N)

	#fMb2.write("czas: " + str(t2[i]) + '\t' + "wynik probki: " + str(Mb2[i]) + "\n")
	fMdecb2.write("czas: " + str(t2[i]) + '\t' + "wynik probki: " + str(Mdecb2[i]) + "\n")

stopDFTb2 = time.time()
#fMb2.close		#to samo co powyżej
fMdecb2.close


#fMb3 = open("probki_Mb3'.xlsx", 'a')
fMdecb3 = open("probki_Mdecb3'.xlsx", 'a')

startDFTb3 = time.time()

for i in range(0, N):

	XReb3_suma = 0
	XImb3_suma = 0

	for j in range(0, N):
		XReb3_suma += b3[j] * m.cos((-2 * m.pi * i * j)/N)
		XImb3_suma += b3[j] * m.sin((-2 * m.pi * i * j)/N)

	XReb3.append(XReb3_suma)
	XImb3.append(XImb3_suma)
	Mb3.append(m.sqrt((XReb3[i])**2 + (XImb3[i])**2))
	Mdecb3.append(10 * m.log10(Mb3[i]))		#to samo co powyżej
	#Mb3[i] = Mb3[i] * (2/N)

	#fMb3.write("czas: " + str(t3[i]) + '\t' + "wynik probki: " + str(Mb3[i]) + "\n")
	fMdecb3.write("czas: " + str(t3[i]) + '\t' + "wynik probki: " + str(Mdecb3[i]) + "\n")

stopDFTb3 = time.time()
#fMb3.close		#to samo co powyżej
fMdecb3.close


startFFTb1 = time.time()
a = fft.fft(b1)
stopFFTb1 = time.time()
print(a)

print("Czas obliczania DFT dla b1: ", stopDFTb1 - startDFTb1, " s")
print("Czas obliczania FFT dla b1: ", stopFFTb1 - startFFTb1, " s")


startFFTb2 = time.time()
b = fft.fft(b2)
stopFFTb2 = time.time()
print(b)

print("Czas obliczania DFT dla b2: ", stopDFTb2 - startDFTb2, " s")
print("Czas obliczania FFT dla b2: ", stopFFTb2 - startFFTb2, " s")


startFFTb3 = time.time()
c = fft.fft(b3)
stopFFTb3 = time.time()
print(c)

print("Czas obliczania DFT dla b3: ", stopDFTb3 - startDFTb3, " s")
print("Czas obliczania FFT dla b3: ", stopFFTb3 - startFFTb3, " s")


#pl.plot(t1, Mb1)				#ta sama sytuacja co powyżej tyle, że do całego bloku komend dot. rysowania wykresu
#pl.title('M(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('A')
#pl.show()

pl.plot(t1, Mdecb1)
pl.title('M\'(k)')
pl.xlabel('f[Hz]')
pl.ylabel('dB')
pl.show()


#pl.plot(t2, Mb2)
#pl.title('M(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('A')
#pl.show()

pl.plot(t2, Mdecb2)
pl.title('M\'(k)')
pl.xlabel('f[Hz]')
pl.ylabel('dB')
pl.show()


#pl.plot(t3, Mb3)
#pl.title('M(k)')
#pl.xlabel('f[Hz]')
#pl.ylabel('A')
#pl.show()

pl.plot(t3, Mdecb3)
pl.title('M\'(k)')
pl.xlabel('f[Hz]')
pl.ylabel('dB')
pl.show()
