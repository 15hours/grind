package main

import (
	"testing"
)

func testSolutionApproach(t *testing.T, solutionApproach func(string) bool) {
	t.Helper()
	tests := []struct {
		s        string
		expected bool
	}{
		{"", false},
		{"abcde", false},
		{"aa", true},
		{"subsubsub", true},
		{"hellohellowhello", false},
		{"aabaaba", false},
	}

	for _, tc := range tests {
		result := solutionApproach(tc.s)
		if result != tc.expected {
			t.Errorf("For %s expected %t, but got %t", tc.s, tc.expected, result)
		}
	}
}

func TestRepeatedSubstringPattern(t *testing.T) {
	testSolutionApproach(t, repeatedSubstringPattern)
}
