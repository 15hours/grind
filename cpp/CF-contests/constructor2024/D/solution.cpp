#include <iostream>
#include <vector>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, m; std::cin >> n >> m;
        long long s[n], d[m];
        for (int i = 0; i < n; i++) {
            std::cin >> s[i];
        }
        for (int i = 0; i < m; i++) {
            std::cin >> d[i];
        }

        int k = 0;
        std::vector<long long> v;
        for (int i = n - 1; i > 0; i--) {
            while (d[m - 1] > s[i]) {
                m--;
            }
            if (m < 1) {
                break;
            }
            if (d[m - 1] <= s[i] && d[m - 1] > s[i - 1]) {
                v.push_back(m);
                k++;
            } else {
                break;
            }
            if (k >= n) {
                break;
            }
        }
        while (d[m - 1] > s[0]) {
            m--;
        }
        if (k < n && m > 0 && d[m - 1] <= s[0]) {
            v.push_back(m);
            k++;
        }

        if (k < n) {
            std::cout << -1;
        } else {
            std::cout << k << '\n';
            for (int i = 0; i < k; i++) {
                std::cout << v[i] << " ";
            }
        }
        std::cout << '\n';
    }
}
