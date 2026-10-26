#include <iostream>
using namespace std;

int main(){
    char a, b;
    cin >> a >> b;
    if (a > b){
        char c = a;
        a = b;
        b = c;
    }
    for (char i = a; i <= b; i++){
        cout << i << ' ';
    }
    return 0;
}