package main

import "fmt"

// 13. Даны две строки: T и S, надо найти первое вхождение S в T БЕЗ учёта порядка символов. Пример  T=reebok S=bee, ответ i=1 (eeb содержит те же символы что и bee).

func solve(t, s string) int {
    currTCnt := [26]int{}
    sCnt := [26]int{}

    sLen := len(s)
    tLen := len(t)

    for i := 0; i < sLen; i++ {
        sCnt[s[i] - 'a']++
        currTCnt[t[i] - 'a']++
    }

    if currTCnt == sCnt {
        return 0
    }

    for r := 1; r < tLen - sLen + 1; r++ {
        currTCnt[t[r+sLen - 1] - 'a']++
        currTCnt[t[r - 1] - 'a']--

        if currTCnt == sCnt {
            return r
        }
    }

    return -1
}

func main() {
    fmt.Println(solve("reebok", "bee"))
}
