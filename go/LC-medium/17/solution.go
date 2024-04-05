package main

// time O(4^n), where n=len(digits), and 4=max(letters[digit])
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	letters := map[byte][]string{
		'2': {"a", "b", "c"},
		'3': {"d", "e", "f"},
		'4': {"g", "h", "i"},
		'5': {"j", "k", "l"},
		'6': {"m", "n", "o"},
		'7': {"p", "q", "r", "s"},
		'8': {"t", "u", "v"},
		'9': {"w", "x", "y", "z"},
	}

	var combinations []string
	for _, v := range letters[digits[0]] {
		combinations = append(combinations, v)
	}

	for i := 1; i < len(digits); i++ {
		var tmpCombinations []string

		for _, v := range letters[digits[i]] {
			for j := range combinations {
				tmpCombinations = append(tmpCombinations, combinations[j]+v)
			}
		}

		combinations = tmpCombinations
	}

	return combinations
}

func letterCombinationsBacktracking(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	letters := map[byte][]string{
		'2': {"a", "b", "c"},
		'3': {"d", "e", "f"},
		'4': {"g", "h", "i"},
		'5': {"j", "k", "l"},
		'6': {"m", "n", "o"},
		'7': {"p", "q", "r", "s"},
		'8': {"t", "u", "v"},
		'9': {"w", "x", "y", "z"},
	}

    var combinations []string

    var backtrack func(comb string, nextDigits string)
    backtrack = func(comb string, nextDigits string) {
        if nextDigits == "" {
            combinations = append(combinations, comb)
            return
        }

        for _, letter := range letters[nextDigits[0]] {
            backtrack(comb + string(letter), nextDigits[1:])
        }
    }

    backtrack("", digits)
    return combinations
}
