#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    long long n; std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::vector<long long> sums(n + 1);
    for (int i = 0; i < n; i++) {
        sums[i + 1] = sums[i] + a[i];
    }

    long long maxDiff = 0;
    for (int k = 1; k < n; k++) {
        if (n % k != 0) {
            continue;
        }

        long long maxSum = 0;
        long long minSum = 1e9;
        for (int i = 0; i < n; i += k) {
            long long v = sums[i + k] - sums[i];
            maxSum = std::max(maxSum, v);
            minSum = std::min(minSum, v);
        }
        maxDiff = std::max(maxDiff, maxSum - minSum);
    }

    std::cout << maxDiff << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
