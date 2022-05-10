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