#include <iostream>

void sovle(){
    std::string s; std::cin >> s;
    int n = s.size();
    for (int i = n - 1; i > 0; i--) {
        if ('1' <= s[i] && s[i] <= '9') {
            std::cout << s.substr(0, i) << '\n';
            break;
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        sovle();
    }
}
