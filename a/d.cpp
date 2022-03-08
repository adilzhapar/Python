#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int c = sqrt(a*a + b*b);
    int p = a + b + c;
    cout << c  << " " << p;
    return 0;
}