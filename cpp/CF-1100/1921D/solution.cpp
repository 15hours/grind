#include <algorithm>
#include <cstdlib>
#include <iostream>

void solve() {
    int n, m;
    std::cin >> n >> m;

    int a[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a, a + n);

    int b[m];
    for (int i = 0; i < m; i++) {
        std::cin >> b[i];
    }
    std::sort(b, b + m);

    long long maxDiff = 0;
    int lA = 0, rA = n - 1;
    int lB = 0, rB = m - 1;
    while (lA <= rA) {
        int llDiff = std::abs(a[lA] - b[lB]);
        int lrDiff = std::abs(a[lA] - b[rB]);
        int rlDiff = std::abs(a[rA] - b[lB]);
        int rrDiff = std::abs(a[rA] - b[rB]);

        if (llDiff >= std::max(lrDiff, std::max(rlDiff, rrDiff))) {
            lA++;
            lB++;
            maxDiff += llDiff;
        } else if (lrDiff >= std::max(llDiff, std::max(rlDiff, rrDiff))) {
            lA++;
            rB--;
            maxDiff += lrDiff;
        } else if (rlDiff >= std::max(llDiff, std::max(lrDiff, rrDiff))) {
            rA--;
            lB++;
            maxDiff += rlDiff;
        } else {
            rA--;
            rB--;
            maxDiff += rrDiff;
        }
    }

    std::cout << maxDiff << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
}
