#include <iostream>

void solve() {
    int n, k; std::cin >> n >> k;
    int c[n];

    for (int i = 0; i < n; i++) {
        std::cin >> c[i];
    }

    int startCount = k;
    int l = 0;
    int startColor = c[l];

    int endCount = k;
    int r = n - 1;
    int endColor = c[r];

    while (l < n) {
        if (c[l] == startColor) {
            startCount--;
        }
        if (startCount == 0) {
            break;
        }

        l++;
    }

    while (r >= 0) {
        if (c[r] == endColor) {
            endCount--;
        }
        if (endCount == 0) {
            break;
        }

        r--;
    }

    if (l >= n || r < 0 || (startColor != endColor && l > r)) {
        std::cout << "No" << '\n';
    } else {
        std::cout << "Yes" << '\n';
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
