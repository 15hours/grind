#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, k; std::cin >> n >> k;
        int a[n];
        for (int i = 0; i < n; i++) {
            if (i < k) {
                a[i] = i + 1;
            } else {
                a[i] = n - i + k;
            }
            if (i) std::cout << " ";
            std::cout << a[i];
        }
        std::cout << '\n';
    }
}
