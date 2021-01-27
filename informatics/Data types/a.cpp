#include <iostream>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    if(b <= a){
        cout << a;
    }else{
        cout << 1 + (b - a);
    }
    return 0;
}