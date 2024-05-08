#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, m; std::cin >> n >> m;
        int b[m];

        for (int i = 0; i < m; i++) {
            std::cin >> b[i];
        }

        for (int a = n; a > 0; a--) {
            if (m <= 0 || a != b[m - 1]) {
                std::cout << a << " ";
            } else {
                m--;
            }
        }
        std::cout << '\n';
    }
}
