#include <iostream>

using namespace std;

int main(void) {
    int start;
    int before;
    int after;
    cin >> start >> before >> after;

    int money = start;
    int month = 1;

    while (money < 70) {
        money += before; // before 는 개월수가 아니라 금액이다. 문제를 잘 읽어라
        month++;
    }
    while (money < 100) {
        money += after; // after 는 개월수가 아니라 금액이다. 문제를 잘 읽어라
        month++;
    }
    cout << month << endl;
    return 0;
}

