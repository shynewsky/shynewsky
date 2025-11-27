#include <iostream>

using namespace std;

int main(void) {
    int year, answer;
    string age_type;
    cin >> year >> age_type;

    if (age_type == "Korea") {
        answer = 2030 -year+1; // 문제에서 '2030년 기준'이라고 한 것을 잘 읽어라
    }
    else if (age_type == "Year") {
        answer = 2030 - year; // 문제에서 '2030년 기준'이라고 한 것을 잘 읽어라
    }

    cout << answer << endl;
    return 0;
}

