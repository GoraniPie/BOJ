#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int n, m;
int arr[8];

void func(int a);

int main() {

	scanf("%d %d", &n, &m);

	func(0);

}

void func(int a) {

	if (a == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 1; i <= n; i++) {

		arr[a] = i;
		func(a + 1);

	}
}