/*

참고한 곳 : https://wooono.tistory.com/302

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력

    첫째 줄에 N이 주어진다. (1 ≤ N < 15)
    
출력

    첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

long long result;
int n;

// 같은 행(열)에는 어차피 퀸을 배치할 수 없으니 일차원 배열로 선언( arr[2] = 4 <=> 2행 4열에 퀸이 있다.)
int arr[14];

void func(int a);
bool is_okay(int a);


int main() {

	scanf("%d", &n);

	func(0);
	printf("%d", result);

}


void func(int a) {
	// 끝까지 탐색했다면 결과값 += 1
	if (a == n) {
		result++;
		return;
	}

	for (int i = 0; i < n; i++) {
		// 행 증가시키며 배치할 수 있는 곳 탐색
		arr[a] = i;

		if (is_okay(a)) {
			// 열 증가
			func(a + 1);
		}
	}

}

bool is_okay(int a) {

	for (int i = 0; i < a; i++) {
		// 열 / 대각선에 말 있나 검사
		if ((arr[i] == arr[a]) || (a - i == (abs(arr[a] - arr[i])))) {
			return false;
		}
	}

	return true;

}