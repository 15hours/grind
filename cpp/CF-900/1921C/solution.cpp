#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        long long n, f, a, b; std::cin >> n >> f >> a >> b;
        long long m[n + 1];
        m[0] = 0;
        for (int i = 0; i < n; i++) {
            std::cin >> m[i + 1];
            f -= std::min(b, (m[i + 1] - m[i])*a);
        }

        if (f <= 0) {
            std::cout << "No" << '\n';
        } else {
            std::cout << "Yes" << '\n';
        }
    }
}
