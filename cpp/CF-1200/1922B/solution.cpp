#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
        a[i] = pow(2, a[i]);
    }

    std::sort(a.begin(), a.end());

    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (a[i] + a[j] <= a[k]) {
                    break;
                }
                count++;
            }
        }
    }

    std::cout << count << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
