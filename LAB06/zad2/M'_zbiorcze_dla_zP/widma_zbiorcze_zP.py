from math import sin, cos, pi, sqrt, log10
import matplotlib.pyplot as plt



fs = 300000 #podanie częstotliwości w kHz
Ts = 1 / fs
Tc = 0.002 #podanie okresu w s

N = round(Tc / Ts)

t = []
m = []
zP1 = []
zP2 = []
zP3 = []
XRezP1 = []
XImzP1 = []
XRezP2 = []
XImzP2 = []
XRezP3 = []
XImzP3 = []
MzP1 = []
MzP2 = []
MzP3 = []
MdBzP1 = []
MdBzP2 = []
MdBzP3 = []
B3dB = []
B6dB = []
B12dB = []

fm = 1000
fn = 10000
kP1 = 0.5
kP2 = 0.5 * pi
kP3 = 20 * pi


for i in range(0, N):

	t.append(i / fs)
	m.append(sin(2 * pi * fm * t[i]))
	zP1.append(cos(2 * pi * fn * t[i] + kP1 * m[i]))
	zP2.append(cos(2 * pi * fn * t[i] + kP2 * m[i]))
	zP3.append(cos(2 * pi * fn * t[i] + kP3 * m[i]))

for i in range(0, N):

	XRezP1_suma = 0
	XImzP1_suma = 0
	XRezP2_suma = 0
	XImzP2_suma = 0
	XRezP3_suma = 0
	XImzP3_suma = 0

	for j in range(0, N):
		XRezP1_suma += zP1[j] * cos((-2 * pi * i * j)/N)
		XImzP1_suma += zP1[j] * sin((-2 * pi * i * j)/N)
		XRezP2_suma += zP2[j] * cos((-2 * pi * i * j)/N)
		XImzP2_suma += zP2[j] * sin((-2 * pi * i * j)/N)
		XRezP3_suma += zP3[j] * cos((-2 * pi * i * j)/N)
		XImzP3_suma += zP3[j] * sin((-2 * pi * i * j)/N)

	XRezP1.append(XRezP1_suma)
	XImzP1.append(XImzP1_suma)
	MzP1.append(sqrt((XRezP1[i])**2 + (XImzP1[i])**2))
	MdBzP1.append(10 * log10(MzP1[i]))

	XRezP2.append(XRezP2_suma)
	XImzP2.append(XImzP2_suma)
	MzP2.append(sqrt((XRezP2[i])**2 + (XImzP2[i])**2))
	MdBzP2.append(10 * log10(MzP2[i]))

	XRezP3.append(XRezP3_suma)
	XImzP3.append(XImzP3_suma)
	MzP3.append(sqrt((XRezP3[i])**2 + (XImzP3[i])**2))
	MdBzP3.append(10 * log10(MzP3[i]))

	B3dB.append(3)
	B6dB.append(6)
	B12dB.append(12)


plt.subplot(3, 1, 1)
plt.plot(t, MdBzP1)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kP = 0.5')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 2)
plt.plot(t, MdBzP2)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kP = pi/2')
plt.xlabel('f[Hz]')
plt.ylabel('dB')

plt.subplot(3, 1, 3)
plt.plot(t, MdBzP3)
plt.plot(t, B3dB, 'k')
plt.plot(t, B6dB, 'y')
plt.plot(t, B12dB, 'r')
plt.title('M\'(t) dla kP = 20*pi')
plt.xlabel('f[Hz]')
plt.ylabel('dB')
plt.show()
