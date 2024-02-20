#include <iostream>

void solve() {
    std::string a, b;
    std::cin >> a;
    std::cin >> b;

    int n = a.size();

    for (int i = 1; i < n; i++) {
        if (a[i] == '1' && a[i - 1] == '0') {
            if (b[i] == '1' && b[i - 1] == '0') {
                std::cout << "Yes\n";
                return;
            }
        }
    }

    std::cout << "No\n";
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
