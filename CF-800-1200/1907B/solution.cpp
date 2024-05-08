#include <deque>
#include <iostream>

template<typename T1, typename T2>
struct MyDeque{
    std::deque<std::pair<T1, T2>> elements;

    void push(const T1& first, const T2& second) {
        elements.emplace_back(first, second);
    }

    void popLast() {
        if (!elements.empty()) {
            elements.pop_back();
        }
    }

    void popFirst() {
        if (!elements.empty()) {
            elements.pop_front();
        }
    }

    bool isEmpty() {
        return elements.empty();
    }

    std::pair<T1, T2>& front() {
        return elements.front();
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        std::string s; std::cin >> s;
        MyDeque<char, int> uppercase;
        MyDeque<char, int> lowercase;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'B') {
                uppercase.popLast();
            } else if (s[i] == 'b') {
                lowercase.popLast();
            } else if ('A' <= s[i] && s[i] <= 'Z') {
                uppercase.push(s[i], i);
            } else {
                lowercase.push(s[i], i);
            }
        }

        std::string result;
        while (!uppercase.isEmpty() && !lowercase.isEmpty()) {
            if (uppercase.front().second < lowercase.front().second) {
                result += uppercase.front().first;
                uppercase.popFirst();
            } else {
                result += lowercase.front().first;
                lowercase.popFirst();
            }
        }

        while (!uppercase.isEmpty()) {
            result += uppercase.front().first;
            uppercase.popFirst();
        }
        while (!lowercase.isEmpty()) {
            result += lowercase.front().first;
            lowercase.popFirst();
        }

        std::cout << result << '\n';
    }
}
