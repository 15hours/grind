#include <algorithm>
#include <iostream>

bool compare(int a, int b) {
    return a < b;
}

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        int s[n];
        for (int i = 0; i < n; i++) {
            std::cin >> s[i];
        }

        int d[n];
        for (int i = 0; i < n; i++) {
            d[i] = (i + 1) * (n - i);
        }

        int nn = sizeof(s) / sizeof(s[0]);
        std::sort(s, s + nn, compare);
        std::sort(d, d + nn, compare);
        int takenDamage = 0;
        for (int i = 0; i < n; i++) {
            takenDamage += s[i] * d[n - i - 1];
        }

        std::cout << takenDamage << '\n';
    }
}
