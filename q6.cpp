#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <bitset>
#include <cmath>

using namespace std;
typedef unsigned long long ll;

ll modulo = 998244353;
ll ans_modulo = 0;

ll exponentiation_modulo(ll base, ll power)
{

    ll res = 1;
    base = base % modulo;
    string bin_power = bitset<64>(power).to_string();
    reverse(bin_power.begin(), bin_power.end());

    for (char i : bin_power)
    {
        if (i == '1')
        {
            res = (res * base) % modulo;
        }
        base = ((base % modulo) * (base % modulo)) % modulo;
    }

    return res;
}

// void subsets_sum(vector<ll> &S, ll n, ll power)
// {
//     ll max = 1 << n;
//     for (ll i = 0; i < max; i++)
//     {
//         ll idx = 0;
//         ll j = i;
//         ll subset_sum = 0;
//         while (j > 0)
//         {
//             if (j & 1)
//             {
//                 subset_sum += S[idx];
//             }
//             idx++;
//             j = j >> 1;
//         }
//         ans_modulo = (ans_modulo + exponentiation_modulo(subset_sum, power)) % modulo;
//     }
// }

void subsetsSum(std::vector<ll>& nums, ll power) {
    ll n = nums.size();

    for (ll i = 0; i < pow(2, n); i++) {
        ll sum = 0;
        for (ll j = 0; j < n; j++) {
            // 如果j位上的标记为1，那么就把对应的数字加到sum中
            if ((i & (1 << j)) != 0) {
                sum += nums[j];
            }
        }
        // ans_modulo = (ans_modulo + exponentiation_modulo(sum, power)) % modulo;
        cout << sum << endl;
    }
}

int main(void)
{

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    ll n, power;
    cin >> n >> power;

    vector<ll> arr(n);
    for (ll i = 0; i < n; i++)
    {
        ll temp;
        cin >> temp;
        arr[i] = temp % modulo;
    }

    subsetsSum(arr, power);
    cout << ans_modulo << endl;

    return 0;
}
