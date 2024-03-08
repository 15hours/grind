#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> c(n);
    for (int i = 0; i < n; i++) {
        std::cin >> c[i];
    }

    long long cnt = c[0] - 1;
    for (int i = 1; i < n; i++) {
        if (c[i] > c[i - 1]) {
            cnt += c[i] - c[i - 1];
        }
    }

    std::cout << cnt << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
