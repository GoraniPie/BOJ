/*

문제

70세 박종수 할아버지는 매일 매일 약 반알을 먹는다. 손녀 선영이는 종수 할아버지에게 약이 N개 담긴 병을 선물로 주었다.

첫째 날에 종수는 병에서 약 하나를 꺼낸다. 그 다음, 그 약을 반으로 쪼개서 한 조각은 먹고, 다른 조각은 다시 병에 넣는다.

다음 날부터 종수는 병에서 약을 하나 꺼낸다. (약은 한 조각 전체 일 수도 있고, 쪼갠 반 조각 일 수도 있다) 반 조각이라면 그 약을 먹고, 아니라면 반을 쪼개서 한 조각을 먹고, 다른 조각은 다시 병에 넣는다.

종수는 손녀에게 한 조각을 꺼낸 날에는 W를, 반 조각을 꺼낸 날에는 H 보낸다. 손녀는 할아버지에게 받은 문자를 종이에 기록해 놓는다. 총 2N일이 지나면 길이가 2N인 문자열이 만들어지게 된다. 이때, 가능한 서로 다른 문자열의 개수는 총 몇 개일까?

입력

    입력은 최대 1000개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄이며, 병에 들어있는 약의 개수 N ≤ 30 가 주어진다.

    입력의 마지막 줄에는 0이 하나 주어진다.

출력

    각 테스트 케이스에 대해서 가능한 문자열의 개수를 출력한다.

*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>

long long funcfunc(short num1, short num2);

long long arr[31][31];

int main() {
    
    for (;;) {
        
        short a;
        scanf("%hd", &a);

        if (a == 0) {
            break;
        }

        printf("%lld\n", funcfunc(a, 0));
        
        for (short i = 0; i < 31; i++) {
            std::fill_n(arr[i], 31, 0);
        }

        for (short i = 1; i < 31; i++) {
            arr[0][i] = 1;
        }
    }
    

}

long long funcfunc(short num1, short num2) {

    if (num1 == 0 && num2 >= 0) {
        return 1;
    }
    else if (num1 > 0 && num2 == 0) {

        if (arr[num1 - 1][1] == 0) {
            arr[num1 - 1][1] = funcfunc(num1 - 1, 1);
            arr[num1][num2] = arr[num1 - 1][1];
            return arr[num1 - 1][1];
        }
        else {
            arr[num1][num2] = arr[num1 - 1][1];
            return arr[num1][num2];
        }
    }
    else {
        if (arr[num1 - 1][num2 + 1] != 0 && arr[num1][num2 - 1] == 0) {
            arr[num1][num2 - 1] = funcfunc(num1, num2 - 1);
            arr[num1][num2] = arr[num1 - 1][num2 + 1] + arr[num1][num2 - 1];
            return arr[num1][num2];
        }
        else if (arr[num1 - 1][num2 + 1] == 0 && arr[num1][num2 - 1] != 0) {
            arr[num1 - 1][num2 + 1] = funcfunc(num1 - 1, num2 + 1);
            arr[num1][num2] = arr[num1 - 1][num2 + 1] + arr[num1][num2 - 1];
            return arr[num1][num2];
        }
        else if (arr[num1 - 1][num2 + 1] != 0 && arr[num1][num2 - 1] != 0) {
            arr[num1][num2] = arr[num1 - 1][num2 + 1] + arr[num1][num2 - 1];
            return arr[num1][num2];
        }
        else {
            arr[num1 - 1][num2 + 1] = funcfunc(num1 - 1, num2 + 1);
            arr[num1][num2 - 1] = funcfunc(num1, num2 - 1);
            arr[num1][num2] = arr[num1 - 1][num2 + 1] + arr[num1][num2 - 1];
            return arr[num1][num2];
        }

    }

}