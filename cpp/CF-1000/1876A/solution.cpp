#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

void solve() {
    long long n, p; std::cin >> n >> p;

    std::vector<int> a;
    for (int i = 0; i < n; i++) {
        int aa; std::cin >> aa;
        a.push_back(aa);
    }

    std::vector<int> b;
    for (int i = 0; i < n; i++) {
        int bb; std::cin >> bb;
        b.push_back(bb);
    }

    std::vector<size_t> indices(a.size());
    std::iota(indices.begin(), indices.end(), 0);

    std::sort(indices.begin(), indices.end(), [&](size_t i, size_t j) {
        return b[i] < b[j];
    });

    std::vector<int> sorted_a;
    std::vector<int> sorted_b;

    for (size_t i : indices) {
        sorted_a.push_back(a[i]);
        sorted_b.push_back(b[i]);
    }

    long long totalSum = p;
    long long cnt = n - 1;

    for (int i = 0; i < n; i++) {
        if (sorted_b[i] < p) {
            if (sorted_a[i] <= cnt) {
                totalSum += sorted_b[i] * sorted_a[i];
                cnt -= sorted_a[i];
            } else {
                totalSum += sorted_b[i] * cnt;
                break;
            }
        } else {
            totalSum += p * cnt;
            break;
        }
    }

    std::cout << totalSum << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
