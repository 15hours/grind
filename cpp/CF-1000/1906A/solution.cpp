#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    char mat[3][3];
    for (int i = 0; i < 3; i++) {
        std::string l; std::cin >> l;
        for (int j = 0; j < 3; j++) {
            mat[i][j] = l[j];
        }
    }

    std::vector<std::string> words;
    for (int r1 = 0; r1 < 3; r1++) {
        for (int c1 = 0; c1 < 3; c1++) {
            for (int r2 = 0; r2 < 3; r2++) {
                for (int c2 = 0; c2 < 3; c2++) {
                    if (r1 == r2 && c1 == c2) {
                        continue;
                    }
                    if (std::abs(r1 - r2) > 1 || std::abs(c1 - c2) > 1) {
                        continue;
                    }
                    for (int r3 = 0; r3 < 3; r3++) {
                        for (int c3 = 0; c3 < 3; c3++) {
                            if (r1 == r3 && c1 == c3 || r2 == r3 && c2 == c3) {
                                continue;
                            }
                            if (std::abs(r2 - r3) > 1 || std::abs(c2 - c3) > 1) {
                                continue;
                            }
                            std::string word;
                            word += mat[r1][c1];
                            word += mat[r2][c2];
                            word += mat[r3][c3];
                            words.push_back(word);
                        }
                    }
                }
            }
        }
    }

    std::string answer = words[0];
    for (const std::string& s : words) {
        if (s < answer) {
            answer = s;
        }
    }

    std::cout << answer <<'\n';
}
