package main

type Pair struct {
	Var    string
	Factor float64
}

// time O(q*n)
// space O(n)
func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	adjMap := make(map[string][]Pair)

	for i, eq := range equations {
		a, b := eq[0], eq[1]
		adjMap[a] = append(adjMap[a], Pair{b, values[i]})
		adjMap[b] = append(adjMap[b], Pair{a, 1 / values[i]})
	}

    var traverse func(node Pair, target string, visited map[string]bool) float64
    traverse = func(node Pair, target string, visited map[string]bool) float64 {
        if visited[node.Var] {
            return 0.0
        }
        visited[node.Var] = true

        if node.Var == target {
            return node.Factor
        }

        for _, nextNode := range adjMap[node.Var] {
            ans := node.Factor * traverse(nextNode, target, visited)
            if ans != 0.0 {
                return ans
            }
        }

        return 0.0
    }

    result := []float64{}
    for _, query := range queries {
        a, b := query[0], query[1]
        if _, ok := adjMap[a]; !ok {
            result = append(result, -1.0)
            continue
        }
        if _, ok := adjMap[b]; !ok {
            result = append(result, -1.0)
            continue
        }

        visited := make(map[string]bool)
        ans := traverse(Pair{a, 1}, b, visited)
        if ans == 0.0 {
            ans = -1.0
        }
        result = append(result, ans)
    }

    return result
}
