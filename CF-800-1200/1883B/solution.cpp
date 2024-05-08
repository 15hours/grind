#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, k; std::cin >> n >> k;
        int a[26] = {0};

        for (int i = 0; i < n; i++) {
            char ch; std::cin >> ch;
            a[ch - 'a']++;
        }

        int oddCount = 0;
        for (auto& x : a) {
            oddCount += x % 2;
        }

        if (oddCount - 1 > k) {
            std::cout << "No" << '\n';
        } else {
            std::cout << "Yes" << '\n';
        }
    }
}
