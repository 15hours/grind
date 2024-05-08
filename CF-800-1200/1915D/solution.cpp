#include <iostream>

bool isVowel(char x) {
    return x == 'a' || x == 'e';
}

int main() {
    int t; std::cin >> t;

    while (t--) {
        long n; std::cin >> n;
        std::string s; std::cin >> s;
        std::string result;
        result += s[0];

        for (int i = 1; i < s.length() - 1; i++) {
            if (!isVowel(s[i]) && isVowel(s[i+1])) {
                result += '.';
                result += s[i];
            } else if (!isVowel(s[i]) && !isVowel(s[i+1])) {
                result += s[i];
            } else {
                result += s[i];
            }
        }

        result += s[s.length() - 1];
        std::cout << result << '\n';
    }
}
