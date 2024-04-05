#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> cnt(n + 1);
    for (int i = 0; i < n; i++) {
        int x; std::cin >> x;
        cnt[x]++;
    }

    long long counter = 0;
    int dp = 0;
    for (int i = 0; i < n + 1; i++) {
        if (cnt[i] == 0) {
            continue;
        }
        counter += 1LL * cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) / 6;
        counter += 1LL * cnt[i] * (cnt[i] - 1) * dp / 2;
        dp += cnt[i];
    }

    std::cout << counter << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
