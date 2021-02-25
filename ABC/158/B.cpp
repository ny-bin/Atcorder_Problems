#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(void)
{
    long n;
    long a;
    long b;
    cin >> n >> a >> b;

    long ans = n / (a+b);
    ans = ans * a;
    long rem = n % (a+b);
    long minans = min(rem,a);
    cout << ans + minans << endl;
}