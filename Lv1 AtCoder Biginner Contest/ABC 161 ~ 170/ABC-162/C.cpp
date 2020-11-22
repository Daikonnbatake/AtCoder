#include <iostream>
using namespace std;

int gcd(int x, int y) { return (x % y)? gcd(y, x % y): y; }
int lcm(int x, int y) { return x / gcd(x, y) * y; }

int main(){
    int K;
    int count = 0;
    cin >> K;
    for(int a = 1; a < K+1; a++){
        for(int b = 1; b < K+1; b++){
            for(int c = 1; c < K+1; c++){
                if(a==1 || b==1 || c==1){
                    count += 1;
                    continue;
                }else{
                    count += gcd(a,gcd(b,c));
                }
            }
        }
    }
    cout << count << '\n';
    return 0;
}