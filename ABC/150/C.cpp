#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(void)
{
    int n;
    int j;
    cin >> n;

    vector<int> vecP(n);
    vector<int> vecQ(n);

    vector<int> vecJ(n);
    for (int i = 0; i < n; i++)
        vecJ[i] = i + 1;

    for (int i = 0; i < n; i++)
        cin >> vecP[i];
    for (int i = 0; i < n; i++)
        cin >> vecQ[i];

    map<vector<int>, int> mp;

    do
    {
        mp[vecJ] = mp.size();
    } while (next_permutation(vecJ.begin(), vecJ.end()));

    int ans = abs(mp[vecP] - mp[vecQ]);
    cout << ans << endl;

}