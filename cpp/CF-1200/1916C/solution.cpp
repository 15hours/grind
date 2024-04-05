#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::cout << a[0] << ' ';
    long long sums = a[0];
    int cntOdd = a[0] % 2;
    for (int i = 1; i < n; i++) {
        cntOdd += a[i] % 2;
        sums += a[i];
        long long ans = 0;

        if (cntOdd % 3 == 0 || cntOdd % 3 == 2) {
            ans = sums - (cntOdd / 3);
        } else {
            ans = sums - (cntOdd + 2) / 3;
        }
        std::cout << ans << ' ';
    }

    std::cout << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
