#1️⃣ Exercise: The Recursive Cashier (Direct Recursion)
def minCoins(N, coins):
    if N == 0:
        return 0  # Base case: No coins needed for zero amount
    min_count = float('inf')  # Initialize with a large value
    for coin in coins:
        if N >= coin:
            min_count = min(min_count, 1 + minCoins(N - coin, coins))
    return min_count

'''
Complexity Analysis:
Time Complexity: O(2^N) (Exponential, since each call branches into multiple recursive calls)
Space Complexity: O(N) (Recursion depth in the worst case)
'''