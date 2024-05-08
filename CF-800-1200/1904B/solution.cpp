#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<std::pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i].first;
        a[i].second = i;
    }
    std::sort(a.begin(), a.end());

    std::vector<long long> sums(n);
    sums[0] = a[0].first;
    for (int i = 1; i < n; i++) {
        sums[i] = sums[i - 1] + a[i].first;
    }

    std::vector<int> cntScore(n);
    cntScore[n - 1] = n - 1;
    for (int i = n - 2; i >= 0; i--) {
        if (sums[i] >= a[i + 1].first) {
            cntScore[i] = cntScore[i + 1];
        } else {
            cntScore[i] = i;
        }
    }
 
    std::vector<int> res(n);
    for (int i = 0; i < n; i++) {
        res[a[i].second] = cntScore[i];
    }
    for (int i = 0; i < n; i++) {
        std::cout << res[i] << " ";
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
