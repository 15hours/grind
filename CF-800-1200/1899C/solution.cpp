#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    int maxSum = a[0];
    int prefixSum = a[0];
    for (int i = 1; i < n; i++) {
        if ((a[i] - a[i - 1]) % 2 == 0) {
            prefixSum = a[i];
        } else {
            prefixSum = std::max(prefixSum, 0) + a[i];
        }
        maxSum = std::max(maxSum, prefixSum);
    }

    std::cout << maxSum << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
