#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    if (a > b){
        int c = a;
        a = b;
        b = c;
    }
    for (int i = a; i <= b; i++){
        cout << i << ' ';
    }
    return 0;
}