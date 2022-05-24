
#include "pch.h"
#include <iostream>
#include <time.h>
using namespace std;

long long asd(int N) {
	time_t start = clock();
	long long answer = 0;

	bool* check = (bool*)malloc(sizeof(bool)*N);

	for (int i = 2; i <= sqrt(N); i++) {
		if (check[i] == false)
			continue;
		for (int j = 2*i; j <= N; j += i) {
			check[j] = false;
		}
	}

	for (int i = 2; i <= N; i++) {
		if (check[i] != false) {
			answer += i;
		}
	}

	cout << answer << endl;
	cout << clock() - start;


	return answer;
}

int main() {
	int a;
	cin >> a;

	asd(a);

	return 0;
}

// Maid Bie SunYong
