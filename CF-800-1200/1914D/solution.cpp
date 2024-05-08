#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

bool compare(const std::pair<int,int>& a, const std::pair<int, int>& b) {
    return a.first > b.first;
}

void solve() {
    int n; std::cin >> n;
    std::vector<std::pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i].first;
        a[i].second = i;
    }
    std::sort(a.begin(), a.end(), compare);

    std::vector<std::pair<int, int>> b(n);
    for (int i = 0; i < n; i++) {
        std::cin >> b[i].first;
        b[i].second = i;
    }
    std::sort(b.begin(), b.end(), compare);

    std::vector<std::pair<int, int>> c(n);
    for (int i = 0; i < n; i++) {
        std::cin >> c[i].first;
        c[i].second = i;
    }
    std::sort(c.begin(), c.end(), compare);

    long long result = 0;
    for (int i = 0; i < std::min(3, n); i++) {
        for (int j = 0; j < std::min(3, n); j++) {
            if (b[j].second == a[i].second) {
                continue;
            }
            for (int k = 0; k < std::min(3, n); k++) {
                if (c[k].second == b[j].second || c[k].second == a[i].second) {
                    continue;
                }

                long long tmpSum = a[i].first + b[j].first + c[k].first;
                result = std::max(result, tmpSum);
            }
        }
    }

    std::cout << result << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
