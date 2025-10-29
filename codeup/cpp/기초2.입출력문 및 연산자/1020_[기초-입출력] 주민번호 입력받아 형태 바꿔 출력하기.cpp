#include <iostream>
using namespace std;

int main(){;
    string s;
    cin >> s;
    
    for (int i = 0; i < s.size(); i++){
        if (s[i] != '-'){
            cout << s[i];
        }
    }
    return 0;
}

// ------------------------------------------------

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;                           
    s.erase(remove(s.begin(), s.end(), '-'), s.end());
    cout << s;
    return 0;
}
