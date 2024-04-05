#include <iostream>

void solve() {
    int n; std::cin >> n;
    int m[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cin >> m[i][j];
        }
    }

    int result[n];
    for (int i = 0; i < n; i++) {
        result[i] = (1 << 30) - 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }

            result[i] &= m[i][j];
            result[j] &= m[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }

            if ((result[i] | result[j]) != m[i][j]) {
                std::cout << "No" << '\n';
                return;
            }
        }
    }

    std::cout << "Yes" << '\n';
    for (int i = 0; i < n; i++) {
        std::cout << result[i] << " ";
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
