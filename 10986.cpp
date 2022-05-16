/*

데이터의 저장과 연산을 int로 했었더니 예제 입력과 같은 작은 수에서는 정상적으로 출력되었지만 큰 수에 대해서는

오답이 나왔었다. 메모리 제한이 널널하니 대부분을 long long 데이터타입으로 바꿔서 해결됐다.

############################################################################################

수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

입력

    첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

    둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력

    첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.


*/



#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>

int main() {

	int N, M;
	scanf("%d %d", &N, &M);

	std::vector<long long> remain_counter(M, 0);
	std::vector<long long> input(N);
	std::vector<long long> remain_sum(N);

	for (int i = 0; i < N; i++) {

		scanf("%d", &input[i]);

		long long remainder_ = input[i] % M;

		if (i == 0) {
			remain_sum[0] = remainder_;
		}
		else {
			remain_sum[i] = (remainder_ + remain_sum[i - 1]) % M;
		}

		remain_counter[remain_sum[i]]++;

	}

	long long result = remain_counter[0];

	for (int i = 0; i < M; i++) {

		if (remain_counter[i] > 1) {
			result += remain_counter[i] * (remain_counter[i] - 1) / 2;
		}

	}

	printf("%lld", result);

}