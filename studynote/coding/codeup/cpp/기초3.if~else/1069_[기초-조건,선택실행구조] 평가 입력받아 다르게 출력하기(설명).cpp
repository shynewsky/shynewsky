#include <iostream>
using namespace std;

int main(){
    char c;
    cin >> c;
    switch(c){
        case 'A' : cout << "best!!!" << "\n"; break;
        case 'B' : cout << "good!!" << "\n"; break;
        case 'C' : cout << "run!" << "\n"; break;
        case 'D' : cout << "slowly~" << "\n"; break;
        default : cout << "what?" << "\n"; break;
    }
    return 0;
}