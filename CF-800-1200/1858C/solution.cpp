#include <iostream>

void solve() {
    int n; std::cin >> n;

    for (int i = 1; i <= n; i += 2) {
        for (int j = i; j <= n; j *= 2) {
            std::cout << j << " ";
        }
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
