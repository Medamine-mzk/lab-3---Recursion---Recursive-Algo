# **Practical Lab: Recursion and Complexity Analysis**

## **🎯 Objective:**
- Understand and implement different types of recursion.
- Analyze the complexity of recursive functions.
- Design optimal recursive solutions.

---
## **1️⃣ Exercise: The Recursive Cashier (Direct Recursion)**
### **Problem Statement:**
A cashier needs to give change using the fewest number of coins. Given an amount `N` and a set of coin denominations `{1, 5, 10, 25, 50, 100}`, write a recursive function to compute the minimum number of coins needed.

### **Tasks:**
- Write a recursive function `minCoins(N, coins)` that finds the minimum number of coins.
- Analyze its complexity and explain why recursion may not be the best approach.
- Optimize it using memoization.

### **Expected Output:**
```python
minCoins(47, [1, 5, 10, 25])  # Output: 5 (25 + 10 + 10 + 1 + 1)
```

---
## **2️⃣ Exercise: Virus Spread (Head Recursion)**
### **Problem Statement:**
A computer virus spreads exponentially every hour. If a system starts with `P` infected computers, and each infected computer infects two new computers every hour, how many infected computers will there be after `N` hours?

### **Tasks:**
- Write a head-recursive function `virusSpread(N, P)`.
- Determine the time complexity.
- Modify the recursion to an iterative approach and compare efficiency.

### **Expected Output:**
```python
virusSpread(3, 1)  # Output: 15 (1 → 3 → 7 → 15)
```

---
## **3️⃣ Exercise: The Tail-Recursive Factorial (Tail Recursion)**
### **Problem Statement:**
Factorial calculation is commonly done using direct recursion, but it can be optimized using tail recursion to avoid stack overflow.

### **Tasks:**
- Implement a tail-recursive factorial function.
- Compare it with a non-tail-recursive version.
- Analyze the complexity and discuss why tail recursion is more memory-efficient.

### **Expected Output:**
```python
factorial(5)  # Output: 120
```

---
## **4️⃣ Exercise: Pascal’s Triangle (Nested Recursion)**
### **Problem Statement:**
Pascal’s Triangle is defined as:

\[ C(n, k) = C(n-1, k-1) + C(n-1, k) \]

with base cases:

\[ C(n, 0) = C(n, n) = 1 \]

### **Tasks:**
- Write a nested recursive function `pascal(n, k)` to compute Pascal’s Triangle.
- Analyze the complexity and suggest an iterative approach.
- Print Pascal’s Triangle up to `n = 5`.

### **Expected Output:**
```plaintext
1  
1 1  
1 2 1  
1 3 3 1  
1 4 6 4 1  
```

---
## **5️⃣ Exercise: File System Depth (Tree Recursion)**
### **Problem Statement:**
A computer file system can be represented as a tree. Each folder contains files or subfolders. Given a nested directory structure, compute the maximum depth of the file system.

### **Example:**
```python
file_system = {
    "home": {
        "user": {
            "documents": {
                "project": {
                    "file1.txt": None,
                    "file2.txt": None
                }
            }
        },
        "downloads": {
            "movie.mp4": None
        }
    }
}
```

### **Tasks:**
- Write a tree-recursive function `maxDepth(fs)` to compute the depth.
- Analyze the complexity and compare with an iterative BFS approach.

### **Expected Output:**
```python
maxDepth(file_system)  # Output: 4
```

---
## **6️⃣ Exercise: Two-Way Communication (Indirect Recursion)**
### **Problem Statement:**
A phone call alternates between caller and receiver until the conversation ends. The caller speaks first, then the receiver replies, then the caller again, and so on. If the caller starts with `n` sentences, and each reply is `n-1` until `n=0`, simulate the conversation using indirect recursion.

### **Tasks:**
- Write two mutually recursive functions `caller(n)` and `receiver(n)`.
- Print a conversation simulation where each side speaks alternately.

### **Expected Output:**
```python
caller(3)
# Output:
# Caller: I will speak 3 times.
# Receiver: I will reply 2 times.
# Caller: I will speak 1 time.
# Receiver: I will reply 0 times.
```

---
## **✨ Bonus Challenge: The Towers of Hanoi (Optimization & Complexity)**
### **Problem Statement:**
The classic Towers of Hanoi involves moving `N` disks from `A → C`, using `B` as an auxiliary. The goal is to minimize the number of moves.

### **Tasks:**
- Write a recursive solution for `hanoi(N, A, B, C)`.
- Prove that the minimum number of moves is \(O(2^N - 1)\).
- Implement a memoized version and analyze its impact.

### **Expected Output:**
```python
hanoi(3, 'A', 'B', 'C')
# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
```

---
## **📌 Student Deliverables:**
- Implement all exercises in Python.
- Analyze the complexity of each algorithm.
- Optimize solutions where possible (memoization, iteration).
- Write a short report explaining:
  - The recursion type used.
  - The base case and recursive case.
  - Time complexity analysis.
  - Alternative iterative solutions (if applicable).

---
## **🔎 Key Takeaways:**
✅ Recursion is powerful but must be optimized to avoid inefficiency.  
✅ Tail recursion improves space complexity.  
✅ Tree recursion can model hierarchical structures like file systems.  
✅ Memoization significantly improves performance.  
✅ Indirect recursion models real-world interactions like phone calls.  

---
## **🔥 Motivation Strategy:**
💡 Gamify the lab: Give points for correct implementations & optimizations.  
💡 Relate to real-world examples: Virus spread, file systems, transactions.  
💡 Show optimization tricks: Memoization, tail recursion, iterative methods.  
💡 Give a challenge: Implement an alternative approach for each problem.  

🎯 **Happy Coding!** 🚀