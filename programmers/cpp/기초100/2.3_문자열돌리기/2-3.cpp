#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    
    // 코드입력
    for (char c : str)
        cout << c << endl;

    return 0;
}
