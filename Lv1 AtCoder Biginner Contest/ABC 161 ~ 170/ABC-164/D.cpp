#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    int start,len,count;
    cin >> S;
    start = 0;
    len = 4;
    count = 0;
    if ((int)(S.length()) >= 4){
        while (true){
            for (int i; i < (int)(S.length()) -4 -start; i++){
                if (atoi(S.substr(start,len))%2019==0){
                    count++;
                }
                end++;
            }
            start++;
            end = start + 4;
            if (start == (int)(S.length()) -3){
                break;
            }
        }
    }
    cout << count << '\n';
    return 0;
}