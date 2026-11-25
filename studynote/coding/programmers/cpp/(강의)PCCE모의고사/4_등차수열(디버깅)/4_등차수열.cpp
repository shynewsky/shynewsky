#include <iostream>

using namespace std;

int main(void) {
    int start, step, end;
    cin >> start >> step >> end;
    
    //for(int i = start; i < end; i++){
    for(int i = start; i >= end; i -= step){

        cout << i << endl;
    }
    
    return 0;
}
