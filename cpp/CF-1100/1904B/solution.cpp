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

    std::vector<int> cntScore(n);
    long long leftSum = 0;
    for (int i = 0; i < n; i++) {
        long long rightSum = 0;
        int cnt = 0;
        for (int j = i + 1; j < n; j++) {
            if (a[i].first + leftSum + rightSum >= a[j].first) {
                rightSum += a[j].first;
                cnt++;
            } else {
                break;
            }
        }
        leftSum += a[i].first;
        cntScore[i] = i + cnt;
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
