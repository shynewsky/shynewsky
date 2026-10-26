#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int s = 0;
    for (int i = a; i <= b; i++) {
        if (i % 3 == 0) s += i;
    }
    cout << s;
    return 0;
}