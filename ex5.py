#5️⃣ Exercise: File System Depth (Tree Recursion)
def maxDepth(fs):
    if not isinstance(fs, dict):  
        return 0  # Base case: A file has depth 0
    return 1 + max((maxDepth(sub) for sub in fs.values()), default=0)

'''
Complexity Analysis:
Time Complexity: O(N) (Visits each folder once)
Space Complexity: O(D) (Recursion depth D)

✅ Correction Criteria:
    ☑ Handles base case (files)
    ☑ Uses tree recursion
    ☑ Computes correct maximum depth
'''