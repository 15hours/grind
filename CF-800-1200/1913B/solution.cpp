#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        std::string s; std::cin >> s;
        std::vector<int> cnt(2);
        for (char c : s) {
            cnt[(int)(c - '0')]++;
        }

        if (cnt[0] == cnt[1]) {
            std::cout << 0 << '\n';
            continue;
        }

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                if (cnt[1] > 0) {
                    cnt[1]--;
                } else {
                    std::cout << s.length() - i << '\n';
                    break;
                }
            } else {
                if (cnt[0] > 0) {
                    cnt[0]--;
                } else {
                    std::cout << s.length() - i << '\n';
                    break;
                }
            }
        }
    }
}
