#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>

using namespace std;

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

		bool is_sorted = true;
		for (int i = 0; i < m ; i++) {
			if (i < m - 1 && arr[i] > arr[i + 1]) {
				is_sorted = false;
				break;
			}
		}

		if (is_sorted) {
			for (int i = 0; i < m; i++) {
				printf("%d ", arr[i]);
			}
			printf("\n");
		}

	}

	for (int i = 1; i <= n; i++) {

		if (!visited[i]) {

			visited[i] = true;
			arr[a] = i;

			func(a + 1);

			visited[i] = false;
		}

	}
}