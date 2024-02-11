#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        int a[26] = {0};

        std::string s; std::cin >> s;
        for (char ch : s) {
            a[ch - 'A']++;
        }

        int counter = 0;
        for (int i = 0; i < 26; i++) {
            if (a[i] >= i + 1) {
                counter++;
            }
        }

        std::cout << counter << '\n';
    }
}
