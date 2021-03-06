#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(void)
{
    int64_t h;
    int64_t ans;
    cin >> h;
    int count = 0;
    while (h > 1)
    {
        h = h / 2;
        count++;
    }
    ans = pow(2, count + 1) - 1;
    cout << ans << endl;
}