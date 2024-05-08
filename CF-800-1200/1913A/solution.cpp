#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        std::string s; std::cin >> s;
        int sLen = s.length();
        bool found = false;
        for (int i = 1; i < sLen; i++) {
            if (i > sLen / 2) {
                break;
            }
            if (s[i] != '0' && std::stoi(s.substr(0, i)) < std::stoi(s.substr(i, sLen))) {
                std::cout << s.substr(0, i) << " " << s.substr(i, sLen) << "\n";
                found = true;
                break;
            }
        }
        if (!found) {
            std::cout << -1 << '\n';
        }
    }
}
