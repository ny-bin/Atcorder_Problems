#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(void)
{
    int n;
    cin >> n ;
    int ans = 100;
    
    for(int i =0;i<n;i++)
    {
        int a;
        cin >> a;
        if(a % 2 != 0)
        {
            ans = 0;
            break;
        }
        int count = 0;
        while(true)
        {
            if(a % 2 == 0)
            {
                count++;
                a = a / 2;
            }
            else
            {
                if(ans > count )
                {
                    ans = count;
                }
                count = 0;
                break;
            }
        }
    }

    cout << ans << endl;


}