#include <iostream>
using namespace std;

int main() {
    string s;
    cin >> s;
    
    for(int i = 0; i < s.size(); i++){
        cout << '[' << s[i];
        
        for(int j = i+1; j < s.size(); j++){
            cout << "0";
        }
        cout << ']' << endl;
    }

    return 0;
}
