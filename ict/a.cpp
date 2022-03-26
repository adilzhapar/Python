#include <iostream>
#include <cmath>

using namespace std;

int Hash(string s){
    int n = 0;
    for(int i=0; i<s.size(); i++){
        n += ((int(s[i]) - 97) * pow(2, i));
    }
    return n;
}


int main(){
    string s;
    getline(cin, s);
    cout << s.size() << endl;
    for(int i=0; i<s.size(); i++){
        cout << Hash(s.substr(0,i+1)) << " ";
    }

    return 0;
}