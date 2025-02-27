#3️⃣ Exercise: The Tail-Recursive Factorial (Tail Recursion)
def factorial(n, acc=1):  
    if n == 0:
        return acc
    return factorial(n - 1, acc * n)  # Tail-recursive call

'''
Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1) (Optimized due to tail recursion)

✅ Correction Criteria:
    ☑ Correct base case (n = 0)
    ☑ Uses tail recursion (accumulator parameter)
    ☑ Compares with non-tail version
'''