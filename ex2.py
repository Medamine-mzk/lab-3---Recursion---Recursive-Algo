#2️⃣ Exercise: Virus Spread (Head Recursion)
def virusSpread(N, P):
    if N == 0:
        return P  # Base case: No more spread
    return 2 * virusSpread(N - 1, P) + 1  # Recursive case: Each infected person infects 2 more

'''
Complexity Analysis:
Time Complexity: O(2^N) (Exponential)
Space Complexity: O(N) (Recursion depth)
'''