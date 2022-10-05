# DP - bottom up approach
coin_list = [1, 3, 4, 5]

def coin_change(coins: list, amount:int):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i-coin])

    if dp[amount] == amount +1:
        return -1
    else:
        return dp[amount]

print(coin_change(coin_list, 10))
