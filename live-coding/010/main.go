// 10. Поступает строка. Нужно понять, можно ли удалить символ так, чтобы строка стала палиндромом. На вход любые виды строк. Надо за O(N)

package main

import "fmt"

func solve(s string) bool {
    l, r := 0, len(s)-1

    for l < r {
        if s[l] != s[r] {
            return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1)
        }
        l++
        r--
    }

    return true
}

func isPalindrome(s string, l int, r int) bool {
    for l < r {
        if s[l] != s[r] {
            return false
        }
        l++
        r--
    }

    return true
}

func main() {
    fmt.Println(solve("qwerewq")) //true
    fmt.Println(solve("assa")) // true
    fmt.Println(solve("jkl")) // false
    fmt.Println(solve("worrxow")) // true
    fmt.Println(solve("worrow")) // true
}
