/*

참고한 곳 :
https://sihyungyou.github.io/baekjoon-17298/



크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력

	첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력

	총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

*/


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stack>

int main() {

	int N;
	scanf("%d", &N);

	int* arr = (int*)malloc(sizeof(int) * N);
	int* ans = (int*)malloc(sizeof(int) * N);
	std::fill_n(ans, N, -1);
	std::stack<int> stack_;

	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < N; i++) {
		while (!stack_.empty() && arr[stack_.top()] < arr[i]) {
			ans[stack_.top()] = arr[i];
			stack_.pop();
		}
		stack_.push(i);
	}

	free(arr);

	for (int i = 0; i < N; i++) {
		printf("%d ", ans[i]);
	}

	free(ans);

}
