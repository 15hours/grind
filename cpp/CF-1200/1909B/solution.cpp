#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    long long k = 1;
    while (true) {
        for (int i = 1; i < n; i++) {
            if (a[i] % k != a[0] % k) {
                std::cout << k << '\n';
                return;
            }
        }
        k *= 2;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
