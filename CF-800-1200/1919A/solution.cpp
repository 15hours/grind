#include <iostream>


int main() {
    int t; std::cin >> t;

    while (t--) {
        int a, b; std::cin >> a >> b;
        if (abs(a - b) % 2 == 0) {
            std::cout << "Bob" << std::endl;
        } else {
            std::cout << "Alice" << std::endl;
        }
    }
}

