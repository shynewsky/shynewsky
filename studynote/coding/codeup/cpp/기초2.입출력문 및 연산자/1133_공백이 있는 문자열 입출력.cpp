#include <iostream>
#include <string>
using namespace std;

int main(){
    string s;
    // cin >> s;  // 단어 하나만 들어온다
    getline(cin, s); // 문장을 통째로 받아온다
    cout << s; // 단어 하나만 출력된다
    return 0;
}