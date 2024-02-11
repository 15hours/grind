package main

func isVowel(c rune) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}

func maxVowelsBFApproach(s string, k int) int {
	n := len(s)
	result := 0
	for i := 0; i < n-k+1; i++ {
		counter := 0
		for j := i; j < i+k; j++ {
			if isVowel(rune(s[j])) {
				counter++
			}
		}
		if counter > result {
			result = counter
		}
	}

	return result
}

func maxVowels(s string, k int) int {
	n := len(s)
	counter := 0
	for i := 0; i < k; i++ {
		if isVowel(rune(s[i])) {
			counter++
		}
	}

	result := counter
	for i := k; i < n; i++ {
		if isVowel(rune(s[i])) {
			counter++
		}
		if isVowel(rune(s[i-k])) {
			counter--
		}
		if counter > result {
			result = counter
		}
	}

	return result
}
