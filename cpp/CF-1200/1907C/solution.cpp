#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<int> a(26);
    std::string s; std::cin >> s;
    for (char c : s) {
        a[c - 'a']++;
    }

    int mx = *std::max_element(a.begin(), a.end());
    if (2 * mx >= n) {
        std::cout << 2 * mx - n << '\n';
    } else {
        std::cout << n % 2 << '\n';
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
