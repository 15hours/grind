// 3. Сжать монотонные подпоследовательности с разницей 1, например [1,2,4,6,7] в последовательности вида min-max т.е. ‘’1-2,4,6-7’’

package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func compressMinMax(seq []int) string {
	lenSeq := len(seq)
	if lenSeq == 0 {
		return ""
	}

    // Quick Sort 
    // Time: avg O(n logn); worst O(n^2)
    // Space: O(n)

    sort.Slice(seq, func(i, j int) bool {
        return seq[i] < seq[j]
    })

	result := []string{}

	l, r := 0, 0
	for i := 1; i < lenSeq; i++ {
		if seq[i]-seq[i-1] > 1 {
			if l == r {
				result = append(result, strconv.Itoa(seq[l]))
			} else {
				result = append(result, strconv.Itoa(seq[l])+"-"+strconv.Itoa(seq[r]))
			}
			l, r = i, i
		} else {
			r++
		}
	}

	if l == r {
		result = append(result, strconv.Itoa(seq[l]))
	} else {
		result = append(result, strconv.Itoa(seq[l])+"-"+strconv.Itoa(seq[r]))
	}

	return strings.Join(result, ",")
}

func main() {
	test0 := []int{1, 3, 4, 6, 7}
	fmt.Println(compressMinMax(test0)) // "1,3-4,6-7"

	test1 := []int{1, 2, 3, 4, 5, 7}
	fmt.Println(compressMinMax(test1)) // "1-4,5-7"

	test2 := []int{1, 2, 4, 6, 7}
	fmt.Println(compressMinMax(test2)) // "1-2,4,6-7"

	test3 := []int{1}
	fmt.Println(compressMinMax(test3)) // "1"

	test4 := []int{}
	fmt.Println(compressMinMax(test4)) // ""

	test5 := []int{1, 3, 4, 6, 7}
	fmt.Println(compressMinMax(test5)) // "1,3-4,6-7"

	test6 := []int{6,1,2,3,7,0}
	fmt.Println(compressMinMax(test6)) // "0-3,6-7"
}
