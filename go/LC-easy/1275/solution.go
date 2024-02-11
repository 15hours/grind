package main

import "fmt"

const gridSize = 3

func currentStandings(gameGrid [][]uint8) string {
    for i := 0; i < gridSize; i++ {
        if gameGrid[i][0] == gameGrid[i][1] && gameGrid[i][0] == gameGrid[i][2] {
            if gameGrid[i][0] == 'X' {
                return "A"
            } else if gameGrid[i][0] == '0' {
                return "B"
            }
        } else if gameGrid[0][i] == gameGrid[1][i] && gameGrid[0][i] == gameGrid[2][i] {
            if gameGrid[0][i] == 'X' {
                return "A"
            } else if gameGrid[0][i] == '0' {
                return "B"
            }
        }
    }

    if gameGrid[0][0] == gameGrid[1][1] && gameGrid[1][1] == gameGrid[2][2] {
        if gameGrid[0][0] == 'X' {
            return "A"
        } else if gameGrid[0][0] == '0' {
            return "B"
        }
    } else if gameGrid[0][2] == gameGrid[1][1] && gameGrid[1][1] == gameGrid[2][0] {
        if gameGrid[0][2] == 'X' {
            return "A"
        } else if gameGrid[0][2] == '0' {
            return "B"
        }
    }

    for i := 0; i < gridSize; i++ {
        if gameGrid[i][0] == '-' || gameGrid[i][1] == '-' || gameGrid[i][2] == '-' {
            return "Pending"
        }
    }

    return "Draw"
}

func tictactoe(moves [][]int) string {
	gameGrid := [][]uint8{
		{'-', '-', '-'},
		{'-', '-', '-'},
		{'-', '-', '-'},
	}

    for i, move := range moves {
		if i%2 == 0 {
			gameGrid[move[0]][move[1]] = 'X'
		} else {
			gameGrid[move[0]][move[1]] = '0'
		}
	}

	return currentStandings(gameGrid)
}

func main() {
	moves1 := [][]int{
		{0, 0},
		{2, 0},
		{1, 1},
		{2, 1},
		{2, 2},
	}
	fmt.Println(tictactoe(moves1))

	moves2 := [][]int{
		{0, 0},
		{1, 1},
		{0, 1},
		{0, 2},
		{1, 0},
		{2, 0},
	}
	fmt.Println(tictactoe(moves2))

	moves3 := [][]int{
		{0, 0},
		{1, 1},
		{2, 0},
		{1, 0},
		{1, 2},
		{2, 1},
		{0, 1},
		{0, 2},
		{2, 2},
	}
	fmt.Println(tictactoe(moves3))
}
