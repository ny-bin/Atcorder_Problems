#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int n;
    cin >> n;
    int d, x;
    cin >> d >> x;

    for (int i = 0; i < n; i++)
    {

        /* code */
        int a;
        int c = 1;
        cin >> a;
        while (c <= d)
        {
            /* code */
            x++;
            c += a;
        }
    }
    cout << x << endl;
}