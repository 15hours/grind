#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        char c = 'A' ^ 'B' ^ 'C' ^ '?';
        std::string s;
        for (int i = 0; i < 3; i++) {
            std::cin >> s;
            for (char ch : s) {
                c ^= ch;
            }
        }
        std::cout << c << '\n';
    }
}
