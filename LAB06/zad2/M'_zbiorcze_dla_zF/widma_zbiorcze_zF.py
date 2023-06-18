from math import sin, cos, pi, sqrt, log10
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zF1 = []
zF2 = []
zF3 = []
XRezF1 = []
XImzF1 = []
XRezF2 = []
XImzF2 = []
XRezF3 = []
XImzF3 = []
MzF1 = []
MzF2 = []
MzF3 = []
MdBzF1 = []
MdBzF2 = []
MdBzF3 = []
B3dB = []
B6dB = []
B12dB = []

fm = 1000
fn = 10000
kF1 = 0.5
kF2 = 0.5 * pi
kF3 = 20 * pi


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zF1.append(cos(2 * pi * fn * t[i] + (kF1/fm) * m[i]))
	zF2.append(cos(2 * pi * fn * t[i] + (kF2/fm) * m[i]))
	zF3.append(cos(2 * pi * fn * t[i] + (kF3/fm) * m[i]))

for i in range(0, N):

	XRezF1_suma = 0
	XImzF1_suma = 0
	XRezF2_suma = 0
	XImzF2_suma = 0
	XRezF3_suma = 0
	XImzF3_suma = 0

	for j in range(0, N):
		XRezF1_suma += zF1[j] * cos((-2 * pi * i * j)/N)
		XImzF1_suma += zF1[j] * sin((-2 * pi * i * j)/N)
		XRezF2_suma += zF2[j] * cos((-2 * pi * i * j)/N)
		XImzF2_suma += zF2[j] * sin((-2 * pi * i * j)/N)
		XRezF3_suma += zF3[j] * cos((-2 * pi * i * j)/N)
		XImzF3_suma += zF3[j] * sin((-2 * pi * i * j)/N)

	XRezF1.append(XRezF1_suma)
	XImzF1.append(XImzF1_suma)
	MzF1.append(sqrt((XRezF1[i])**2 + (XImzF1[i])**2))
	MdBzF1.append(10 * log10(MzF1[i]))

	XRezF2.append(XRezF2_suma)
	XImzF2.append(XImzF2_suma)
	MzF2.append(sqrt((XRezF2[i])**2 + (XImzF2[i])**2))
	MdBzF2.append(10 * log10(MzF2[i]))

	XRezF3.append(XRezF3_suma)
	XImzF3.append(XImzF3_suma)
	MzF3.append(sqrt((XRezF3[i])**2 + (XImzF3[i])**2))
	MdBzF3.append(10 * log10(MzF3[i]))

	B3dB.append(3)
	B6dB.append(6)
	B12dB.append(12)


plt.subplot(3, 1, 1)
plt.plot(t, MdBzF1)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kF = 0.5')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 2)
plt.plot(t, MdBzF2)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kF = pi/2')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 3)
plt.plot(t, MdBzF3)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kF = 20*pi')
plt.xlabel('f[Hz]')
plt.ylabel('dB')
plt.show()
