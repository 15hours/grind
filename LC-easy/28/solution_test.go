package main

import "testing"

func testSolutionApproach(t *testing.T, solutionApproach func(string, string) int) {
	t.Helper()

	tests := []struct {
		haystack string
		needle   string
		expected int
	}{
		{"", "", -1},
		{"someome", "me", 2},
		{"whatever", "hello", -1},
	}

	for _, tc := range tests {
		result := solutionApproach(tc.haystack, tc.needle)
		if result != tc.expected {
			t.Errorf("For (%s, %s), expected %d, but got %d",
				tc.haystack, tc.needle, tc.expected, result)
		}
	}
}

func TestStrStrUsingBF(t *testing.T) {
	testSolutionApproach(t, strStrUsingBF)
}

func TestStrStrUsingSlice(t *testing.T) {
	testSolutionApproach(t, strStrUsingSlice)
}

func TestStrStrUsingIndex(t *testing.T) {
	testSolutionApproach(t, strStrUsingIndex)
}
