package main

import (
	"testing"
)

func TestEmptyStrings(t *testing.T) {
    result := mergeAlternately("", "")
    expected := ""

    if result != expected {
        t.Errorf("Expected %s, but got %s", expected, result)
    }
}

func TestFirstEmptyString(t *testing.T) {
    result := mergeAlternately("", "hello")
    expected := "hello"

    if result != expected {
        t.Errorf("Expected %s, but got %s", expected, result)
    }
}

func TestSecondEmptyString(t *testing.T) {
    result := mergeAlternately("hello", "")
    expected := "hello"

    if result != expected {
        t.Errorf("Expected %s, but got %s", expected, result)
    }
}

func TestDifferentLengths(t *testing.T) {
    result := mergeAlternately("ac", "bde")
    expected := "abcde"

    if result != expected {
        t.Errorf("Expected %s, but got %s", expected, result)
    }
}

func TestEqualLengths(t *testing.T) {
    result := mergeAlternately("ace", "bdf")
    expected := "abcdef"

    if result != expected {
        t.Errorf("Expected %s, but got %s", expected, result)
    }
}
