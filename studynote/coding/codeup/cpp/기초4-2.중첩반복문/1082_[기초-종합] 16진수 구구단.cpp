#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int n;
    cin >> hex >> n;

    for (int i = 1; i <= 15; i++){
        cout << uppercase << hex 
        << n << '*' << i << '=' << n * i << '\n';
    }

}
