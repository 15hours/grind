package main

import (
	"reflect"
	"testing"
)

func testSolutionApproach(t *testing.T, solutionApproach func(nums []int) []int) {
	t.Helper()

	tests := []struct {
		nums     []int
		expected []int
	}{
		{[]int{0, 1, 0, 3, 12}, []int{1, 3, 12, 0, 0}},
		{[]int{0}, []int{0}},
		{[]int{0, 0, 1, 2, 3}, []int{1, 2, 3, 0, 0}},
	}

	for _, tc := range tests {
		result := solutionApproach(tc.nums)
		if !reflect.DeepEqual(result, tc.expected) {
			t.Errorf("For nums=%v, expected %v, but got %v", tc.nums, tc.expected, result)
		}
	}
}

func TestMoveZeroesUsingBFApproach(t *testing.T) {
	testSolutionApproach(t, BFApproach)
}

func TestMoveZeroesUsingSnowballApproach(t *testing.T) {
	testSolutionApproach(t, snowballApproach)
}

func TestMoveZeroesUsingModifiedSnowballApproach(t *testing.T) {
	testSolutionApproach(t, modifiedSnowballApproach)
}

func TestMoveZeroesUsingTwoPointersApproach(t *testing.T) {
	testSolutionApproach(t, twoPointersApproach)
}
