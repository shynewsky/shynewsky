#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int i = 0;
    int s = 0;
    while (s < n){
        i++;
        s += i;
    }
    cout << i;

    return 0;
}