package main

import (
	"fmt"
)

func predictPartyVictory(senate string) string {
    queueR, queueD := []int{}, []int{}

    for i, ch := range senate {
        switch ch {
        case 'R':
            queueR = append(queueR, i)
        case 'D':
            queueD = append(queueD, i)
        }
    }

    addRound := len(senate)
    for len(queueR) > 0 && len(queueD) > 0 {
        r, d := queueR[0], queueD[0]

        if r < d {
            queueR = append(queueR, addRound)
        } else {
            queueD = append(queueD, addRound)
        }

        queueR = queueR[1:]
        queueD = queueD[1:]

        addRound++
    }

    if len(queueR) > 0 {
        return "Radiant"
    }
    return "Dire"
}

func main() {
    fmt.Println(predictPartyVictory("DRRDRDRDDRDR"))
    fmt.Println(predictPartyVictory("RRDDD"))
    fmt.Println(predictPartyVictory("DDRRR"))
}
