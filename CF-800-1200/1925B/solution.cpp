#include <algorithm>
#include <iostream>

void solve() {
    int x, n; std::cin >> x >> n;
    
    long long maxGcd = 0;
    for (long long divisor = 1; divisor*divisor <= x; divisor++) {
        if (x % divisor != 0) {
            continue;
        }

        if (divisor * n <= x) {
            maxGcd = std::max(maxGcd, divisor);
        }
        if (divisor >= n) {
            maxGcd = std::max(maxGcd, x / divisor);
            break;
        }
    }

    std::cout << maxGcd << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
