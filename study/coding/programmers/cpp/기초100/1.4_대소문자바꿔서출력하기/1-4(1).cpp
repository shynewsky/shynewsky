#include <iostream>
#include <string>

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
- char 타입은 아스키코드 뜻하며, 숫자와 알파벳을 저장한다
-  문자배열의 원소 개수만큼 반복/순회하며, 원소를 char c에 나눠담는다
- for(int i = 0; i < str.size(); i++) 와 같다

- 아스키코드 A(65)~Z(90), a(97)~z(122)로 대소문자는 32만큼 차이가 난다
- 경계가 되는 Z를 기준으로, 같거나 작으면 대문자고, 초과하면 소문자이다
- 대문자는 +32 하여 소문자로 만들고, 소문자는 -32 하여 대문자로 만든다
*/

