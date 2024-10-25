package main

// 19. Longest Subarray of 1's After Deleting One Element https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
// Given a binary array nums, you should delete one element from it.
// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


// 1 0 1 1 1 0 1 1

func solve(nums []int) {
    var l, r, cntZeroes, result int

    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            cntZeroes++
        }

        if cntZeroes > 1 {
            if nums[l] == 0 {
                cntZeroes--
            }
            l++
        }

        r++
        result = max(result, r - l - 1)
    }

}
