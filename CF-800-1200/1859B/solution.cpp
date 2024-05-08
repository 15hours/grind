#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    int minElement = 1E9;
    std::vector<int> terms;

    while (n--) {
        int m; std::cin >> m;

        std::vector<int> a(m);
        for (int i = 0; i < m; i++) {
            std::cin >> a[i];
        }

        std::sort(a.begin(), a.end());

        terms.push_back(a[1]);
        minElement = std::min(minElement, a[0]);
    }
    std::sort(terms.begin(), terms.end());

    long long beautySum = minElement;
    for (int i = 1; i < terms.size(); i++) {
        beautySum += terms[i];
    }

    std::cout << beautySum << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
