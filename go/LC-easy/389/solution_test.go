package main

import "testing"

func testSolutionApproach(t *testing.T, solutionApproach func(string, string) byte) {
	t.Helper()

	tests := []struct {
		haystack string
		needle   string
		expected byte
	}{
		{"", "", 0},
		{"abcd", "abcdd", 'd'},
		{"", "y", 'y'},
	}

	for _, tc := range tests {
		result := solutionApproach(tc.haystack, tc.needle)
		if result != tc.expected {
			t.Errorf("For (%s, %s), expected %c, but got %c",
				tc.haystack, tc.needle, tc.expected, result)
		}
	}
}

func TestFindDifferenceUsingMap(t *testing.T) {
	testSolutionApproach(t, findTheDifferenceUsingMap)
}

func TestFindDifferenceUsingBitManipulation(t *testing.T) {
	testSolutionApproach(t, findTheDifferenceUsingBitManipulation)
}
