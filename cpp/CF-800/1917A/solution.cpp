#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        int a[n];

        int k = -1;
        int negCount = 0;
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];

            if (a[i] == 0) {
                k = 0;
            }

            if (a[i] < 0) {
                negCount++;
            }
        }

        if (k == 0 || negCount % 2 == 1) {
            std::cout << 0 << std::endl;
        } else {
            std::cout << 1 << std::endl;
            std::cout << n << " " << 0 << std::endl;
        }
    }
}
