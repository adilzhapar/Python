#include <iostream>
#include <stack>
#include <cmath>
using namespace std;

char hashback(int n, int index){
    return (n / pow(2, index)) + 97;
}

int main(){

    freopen("input.txt", "r", stdin);
    int n;
    cin >> n;
    stack<int> st;
    string ans = "";
    
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        int temp = x;
        if (!st.empty()){
            temp -= st.top();
        }
        st.push(x);
        ans += hashback(temp, i);
    }
    cout << ans;

    return 0;
} 