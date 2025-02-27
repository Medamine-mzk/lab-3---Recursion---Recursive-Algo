#1️⃣ Exercise: The Recursive Cashier (Direct Recursion) + Optimization (Memoization)
def minCoinsMemo(N, coins, memo={}):
    if N in memo:
        return memo[N]
    if N == 0:
        return 0
    min_count = float('inf')
    for coin in coins:
        if N >= coin:
            min_count = min(min_count, 1 + minCoinsMemo(N - coin, coins, memo))
    memo[N] = min_count
    return min_count

'''
Time Complexity (Optimized): O(N)
Space Complexity: O(N)

✅ Correction Criteria:
    ☑ Base case handling (N = 0)
    ☑ Correct recursive structure
    ☑ Correct use of min()
    ☑ Memoization for efficiency
'''