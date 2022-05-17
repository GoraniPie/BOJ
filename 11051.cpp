/*
https://www.acmicpc.net/problem/11051
이항계수 3 문제에서 메모리 초과로 실패했던 접근을 이항계수 2 문제에 이식했음. 
*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>

int combination(int n, int r, std::vector<std::vector<int>> &arr);

int main() {
	
	int N, K;
	scanf("%d %d", &N, &K);

	std::vector<std::vector<int>> arr(N, std::vector<int>(N, -1));
	arr[0][0] = 1;
	printf("%d", combination(N, K, arr) % 10007);

}

int combination(int n, int r, std::vector<std::vector<int>> &arr) {
	if (r > n) {
		return 0;
	}
	
	if (r == n || r == 0) {
		return 1;
	}
	
	if (arr[n - 1][r - 1] == -1 && arr[n - 1][r] == -1) {
		arr[n - 1][r - 1] = combination(n - 1, r - 1, arr);
		arr[n - 1][r] = combination(n - 1, r, arr);
		int tmp = arr[n - 1][r - 1] + arr[n - 1][r];
		if (tmp > 10007) {
			return tmp - 10007;
		}
		return tmp;
	}
	else if (arr[n - 1][r - 1] == -1 && arr[n - 1][r] != -1) {
		arr[n - 1][r - 1] = combination(n - 1, r - 1, arr);
		int tmp = arr[n - 1][r - 1] + arr[n - 1][r];
		if (tmp > 10007) {
			return tmp - 10007;
		}
		return tmp;
	}
	else if (arr[n - 1][r - 1] != -1 && arr[n - 1][r] == -1) {
		arr[n - 1][r] = combination(n - 1, r, arr);
		int tmp = arr[n - 1][r - 1] + arr[n - 1][r];
		if (tmp > 10007) {
			return tmp - 10007;
		}
		return tmp;
	}
	else {
		int tmp = arr[n - 1][r - 1] + arr[n - 1][r];
		if (tmp > 10007) {
			return tmp - 10007;
		}
		return tmp;
	}
	
}