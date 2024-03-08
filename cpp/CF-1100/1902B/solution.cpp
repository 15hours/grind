#include <algorithm>
#include <iostream>

void solve() {
    long long n, P, L, T; std::cin >> n >> P >> L >> T;

    int tt = (n + 6) / 7;
    
    int l = 0, r = n;
    while (r - l > 1) {
        int k = (l + r) / 2;
        long long p = k * L + T * std::min(tt, 2 * k);
        if (p > P) {
            r = k;
        } else if (p < P) {
            l = k;
        } else {
            std::cout << n - k << '\n';
            return;
        }
    }
    std::cout << n - r << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int tc; std::cin >> tc;
    while (tc--) {
        solve();
    }
}
