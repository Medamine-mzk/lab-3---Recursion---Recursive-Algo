#2️⃣ Exercise: Virus Spread (Head Recursion) + Iterative Optimization:
def virusSpreadIter(N, P):
    total = P
    for _ in range(N):
        total = 2 * total + 1
    return total

'''
✅ Correction Criteria:
    ☑ Correct base case (N = 0)
    ☑ Correct head recursion structure
    ☑ Identifies inefficiency (exponential complexity)
    ☑ Suggests iteration for optimization
'''
