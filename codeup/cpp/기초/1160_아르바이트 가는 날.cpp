#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    switch(n) {
        case 1: case 3: case 5: case 7: cout << "oh my god"; break;
        case 2: case 4: case 6: cout << "enjoy"; break;
    }
    return 0;
}