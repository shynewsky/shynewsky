#include <iostream>
#include <string>
#include <algorithm>
// isupper(), islower(), toupper(), tolower() 를 사용하려면 포함해야 함

using namespace std;

int main(void) {
    string str;
    cin >> str;
    
    // 코드입력 (1) - 반복문 이용
    for (char c : str)
        cout << (c <= 'Z' ? char(c+32) : char(c-32));

    return 0;
}

/*
- isupper() : 대문자인지 확인하는 C++ 함수
- islower() : 소문자인지 확인하는 C++ 함수
- toupper() : 대문자로 바꾸는 C++ 함수
- tolower() : 소문자로 바꾸는 C++ 함수
*/

