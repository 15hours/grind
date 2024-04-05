package main

func maxProfitBottomUpApproach(prices []int, fee int) int {
	n := len(prices)
	if n == 1 {
		return 0
	}

	buy := make([]int, n)
	buy[0] = -prices[0]
	sell := make([]int, n)

	for i := 1; i < n; i++ {
		buy[i] = max(buy[i-1], sell[i-1]-prices[i])
		sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
	}

	return sell[n-1]
}

func maxProfitTopDownApproach(prices []int, fee int) int {
	n := len(prices)
	if n == 1 {
		return 0
	}

	buy := make([]int, n)
	sell := make([]int, n)
    for i := 0; i < n; i++ {
        buy[i] = -1e9
        sell[i] = -1e9
    }
    buy[0] = -prices[0]

	var traverse func(stock, turn int) int
	traverse = func(stock, turn int) int {
		if stock < 0 {
			return 0
		}
		if turn == 0 && buy[stock] != -1e9 {
			return buy[stock]
		} 
        if turn == 1 && sell[stock] != -1e9 {
			return sell[stock]
		}

		if turn == 0 {
			buy[stock] = max(traverse(stock-1, 0), traverse(stock-1, 1)-prices[stock])
			return buy[stock]
		} else {
			sell[stock] = max(traverse(stock-1, 1), traverse(stock-1, 0)+prices[stock]-fee)
			return sell[stock]
		}

	}

	return traverse(n-1, 1)
}
