package main

import (
	"testing"
)

func TestDifferentStringLength(t *testing.T) {
	result := isAnagram("a", "ab")
	expected := false

	if result != expected {
		t.Errorf("Expected %t, but got %t", expected, result)
	}
}

func TestEmptyStrings(t *testing.T) {
	result := isAnagram("", "")
	expected := false

	if result != expected {
		t.Errorf("Expected %t, but got %t", expected, result)
	}
}

func TestCorrectAnagram(t *testing.T) {
	result := isAnagram("anagram", "nagaram")
	expected := true

	if result != expected {
		t.Errorf("Expected %t, but got %t", expected, result)
	}
}

func TestIncorrectAnagram(t *testing.T) {
	result := isAnagram("rat", "car")
	expected := false

	if result != expected {
		t.Errorf("Expected %t, but got %t", expected, result)
	}
}
