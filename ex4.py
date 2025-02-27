#4️⃣ Exercise: Pascal’s Triangle (Nested Recursion)
def pascal(n, k):
    if k == 0 or k == n:
        return 1  # Base cases
    return pascal(n - 1, k - 1) + pascal(n - 1, k)  # Nested recursion

'''
Complexity Analysis:
Time Complexity: O(2^N)
Space Complexity: O(N)

✅ Correction Criteria:
    ☑ Base cases handled correctly
    ☑ Nested recursion used
    ☑ Complexity analysis provided
'''