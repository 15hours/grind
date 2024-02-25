#include <iostream>
#include <string>

void solve() {
    int n; std::cin >> n;
    std::string s; std::cin >> s;

    int cnt = n;
    char lastChar = s[n - 1];
    for (int i = 0; i < n; i++) {
        char curChar = s[i];
        bool skip = false;
        for (int j = i + 2; j < n; j++) {
            if (curChar != s[j - 1]) {
                cnt++;
            } else {
                skip = true;
                break;
            }
        }
        if (!skip && curChar != lastChar) {
            cnt++;
        }
    }

    std::cout << cnt << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
