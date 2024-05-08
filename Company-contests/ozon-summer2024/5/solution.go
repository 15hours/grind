package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func solve(in *bufio.Reader) string {
	var n int
	fmt.Fscan(in, &n)

	in.ReadString('\n')

	lines := make([]string, n)
	for i := 0; i < n; i++ {
		line, err := in.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading input:", err)
			return ""
		}

		lines[i] = line
	}

	jsonData := strings.Join(lines, "\n")
	var jsonObj interface{}
	if err := json.Unmarshal([]byte(jsonData), &jsonObj); err != nil {
		fmt.Println("Error:", err)
		return ""
	}

	var traverse func(obj interface{}) interface{}
	traverse = func(obj interface{}) interface{} {
		switch v := obj.(type) {
		case map[string]interface{}:
			newObj := make(map[string]interface{})
			for key, val := range v {
				if updatedVal := traverse(val); updatedVal != nil {
					newObj[key] = updatedVal
				}
			}
			if len(newObj) == 0 {
				return nil
			}
			return newObj
		case []interface{}:
			newArr := make([]interface{}, 0)
			for _, elem := range v {
				if updatedElem := traverse(elem); updatedElem != nil {
					newArr = append(newArr, updatedElem)
				}
			}
			if len(newArr) == 0 {
				return nil
			}
			return newArr
		default:
			return v
		}
	}

	updatedObj := traverse(jsonObj)
	updatedJSON, err := json.Marshal(updatedObj)
	if err != nil {
		fmt.Println("Error encoding JSON:", err)
		return ""
	}

	return string(updatedJSON)
}

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	lines := make([]string, t)
	for i := 0; i < t; i++ {
		result := solve(in)
		lines[i] = result
	}

	combinedJSON := "[" + strings.Join(lines, ",") + "]"
	fmt.Fprintln(out, combinedJSON)
}
