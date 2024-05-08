package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

type Folder struct {
	Dir     string   `json:"dir"`
	Files   []string `json:"files"`
	Folders []Folder `json:"folders"`
	Viruses int
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n int
	fmt.Fscan(in, &n)

	in.ReadString('\n')

	lines := make([]string, n)
	for i := 0; i < n; i++ {
		line, err := in.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading input:", err)
			return
		}

		lines[i] = line
	}

	jsonData := strings.Join(lines, "\n")
	var folder Folder
	if err := json.Unmarshal([]byte(jsonData), &folder); err != nil {
		fmt.Println("Error:", err)
		return
	}

	var traverse func(node Folder, infected bool) int
	traverse = func(node Folder, infected bool) int {
		if !infected {
			for _, file := range node.Files {
				if strings.HasSuffix(file, ".hack") {
					infected = true
					break
				}
			}
		}

		if infected {
			node.Viruses += len(node.Files)
		}

		for _, nextNode := range node.Folders {
			node.Viruses += traverse(nextNode, infected)
		}

		return node.Viruses
	}

	fmt.Fprintln(out, traverse(folder, false))
}

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	for i := 0; i < t; i++ {
		solve(in, out)
	}
}
