#include <iostream>

void solve() {
    int n, k; std::cin >> n >> k;

    int a[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int b[n];
    for (int i = 0; i < n; i++) {
        std::cin >> b[i];
    }

    int answer = 0;
    int firstTryExp = 0;
    int curMaxGrindExp = 0;
    if (n > k) {
        n = k;
    }
    for (int i = 0; i < n; i++) {
        firstTryExp += a[i];
        curMaxGrindExp = std::max(curMaxGrindExp, b[i]);

        int curTotalMaxExp = firstTryExp + curMaxGrindExp * (k - i - 1);
        if (curTotalMaxExp > answer) {
            answer = curTotalMaxExp;
        }
    }

    std::cout << answer << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
