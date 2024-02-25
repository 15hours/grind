#include <iostream>
#include <vector>

void solve() {
    int n; std::cin >> n;

    std::vector<int> adjList(n + 1, 0);
    n--;
    while (n--) {
        int u, v; std::cin >> u >> v;
        adjList[u]++;
        adjList[v]++;

    }

    int cnt = 0;
    for (auto& x : adjList) {
        if (x == 1) {
            cnt++;
        }
    }

    std::cout << (cnt + 1) / 2 << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
