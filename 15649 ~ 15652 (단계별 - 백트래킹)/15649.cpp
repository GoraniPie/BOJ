#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int n, m;
int arr[9];
bool visited[9];

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
	}

	for (int i = 1; i <= n; i++) {

		if (visited[i] != true) {

			visited[i] = true;
			arr[a] = i;

			func(a + 1);

			visited[i] = false;
		}

	}
}