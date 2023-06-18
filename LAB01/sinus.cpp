#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>

using namespace std;

int main(void)
{
	float fs = 100; //podanie czêstotliwoœci w Hz
	float Ts = 1 / fs;
	float Tc = 1; //podanie okresu w s

	int N = ceil(Tc / Ts);

	float* s = new float[N];
	float* t = new float[N];

	float A = 1;
	float f = 1;
	float fi = 0;

	for (int n = 0; n < N; n++)
	{
		t[n] = n / fs;
		s[n] = A * sin(2 * M_PI * f * t[n] + fi);

		cout << t[n] << ";" << s[n] << ";" << endl;
	}

	delete[] s;
	delete[] t;

	return 0;
}