#include <algorithm>
#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a.begin(), a.end());
    a.erase(std::unique(a.begin(), a.end()), a.end());
    
    int start = 0;
    int total = 0;
    int counter = 1;
    for (int i = 1; i < a.size(); i++) {
        while (a[i] - a[start] >= n) {
            counter--;
            start++;
        }
        counter++;
        total = std::max(total, counter);
    }

    total = std::max(total, counter);
    std::cout << total << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
