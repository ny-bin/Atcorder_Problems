#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main(void)
{
    int a, b, m;
    int j;
    cin >> a >> b >> m;
    vector<int> inputA(a);
    vector<int> inputB(b);

    int ans;

    for (int i = 0; i < a; i++)
    {
        cin >> j;
        inputA[i] = j;
    }
    for (int i = 0; i < b; i++)
    {
        cin >> j;
        inputB[i] = j;
    }
    int amin = *min_element(inputA.begin(), inputA.end());
    int bmin = *min_element(inputB.begin(), inputB.end());
    ans = amin + bmin;

    for (int i = 0; i < m; i++)
    {

        /* code */
        int x, y, c;
        cin >> x >> y >> c;
        int testans = inputA[x - 1] + inputB[y - 1] - c;
        if (testans < ans)
        {
            ans = testans;
        }
    }
    cout << ans << endl;
}

// #include <bits/stdc++.h>
// using namespace std;
// int main()
// {
//     int A, B, M;
//     cin >> A >> B >> M;
//     vector<int> a(A);
//     vector<int> b(B);
//     for (int i = 0; i < A; i++)
//         cin >> a[i];
//     for (int i = 0; i < B; i++)
//         cin >> b[i];
//     int minA = *min_element(a.begin(), a.end());
//     int minB = *min_element(b.begin(), b.end());
//     int ans = minA + minB;
//     for (int i = 0; i < M; i++)
//     {
//         int x, y, c;
//         cin >> x >> y >> c;
//         x--;
//         y--;
//         ans = min(ans, a[x] + b[y] - c);
//     }
//     cout << ans << endl;
//     return 0;
// }