from math import sin, cos, pi, sqrt, log10
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zA1 = []
zA2 = []
zA3 = []
XRezA1 = []
XImzA1 = []
XRezA2 = []
XImzA2 = []
XRezA3 = []
XImzA3 = []
MzA1 = []
MzA2 = []
MzA3 = []
MdBzA1 = []
MdBzA2 = []
MdBzA3 = []
B3dB = []
B6dB = []
B12dB = []

fm = 1000
fn = 10000
kA1 = 0.5
kA2 = 7
kA3 = 120


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zA1.append((kA1 * m[i] + 1) * cos(2 * pi * fn * t[i]))
	zA2.append((kA2 * m[i] + 1) * cos(2 * pi * fn * t[i]))
	zA3.append((kA3 * m[i] + 1) * cos(2 * pi * fn * t[i]))

for i in range(0, N):

	XRezA1_suma = 0
	XImzA1_suma = 0
	XRezA2_suma = 0
	XImzA2_suma = 0
	XRezA3_suma = 0
	XImzA3_suma = 0

	for j in range(0, N):
		XRezA1_suma += zA1[j] * cos((-2 * pi * i * j)/N)
		XImzA1_suma += zA1[j] * sin((-2 * pi * i * j)/N)
		XRezA2_suma += zA2[j] * cos((-2 * pi * i * j)/N)
		XImzA2_suma += zA2[j] * sin((-2 * pi * i * j)/N)
		XRezA3_suma += zA3[j] * cos((-2 * pi * i * j)/N)
		XImzA3_suma += zA3[j] * sin((-2 * pi * i * j)/N)

	XRezA1.append(XRezA1_suma)
	XImzA1.append(XImzA1_suma)
	MzA1.append(sqrt((XRezA1[i])**2 + (XImzA1[i])**2))
	MdBzA1.append(10 * log10(MzA1[i]))

	XRezA2.append(XRezA2_suma)
	XImzA2.append(XImzA2_suma)
	MzA2.append(sqrt((XRezA2[i])**2 + (XImzA2[i])**2))
	MdBzA2.append(10 * log10(MzA2[i]))

	XRezA3.append(XRezA3_suma)
	XImzA3.append(XImzA3_suma)
	MzA3.append(sqrt((XRezA3[i])**2 + (XImzA3[i])**2))
	MdBzA3.append(10 * log10(MzA3[i]))

	B3dB.append(3)
	B6dB.append(6)
	B12dB.append(12)


plt.subplot(3, 1, 1)
plt.plot(t, MdBzA1)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kA = 0.5')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 2)
plt.plot(t, MdBzA2)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kA = 7')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 3)
plt.plot(t, MdBzA3)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kA = 120')
plt.xlabel('f[Hz]')
plt.ylabel('dB')
plt.show()
