# **Recursion & Memoization - Practical Lab Correction**

## **📌 Exercise 1: Fibonacci Sequence (Direct Recursion & Memoization)**
### **Problem Statement:**
Write a recursive function to compute the `n`th Fibonacci number using:
1. **Naive Recursion** (direct recursion)
2. **Memoization** to optimize it

### **Solution:**
#### **1️⃣ Naive Recursive Fibonacci (Slow)**
```python
# Exponential Time Complexity: O(2^N)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### **2️⃣ Optimized Fibonacci using Memoization (Fast)**
```python
# Linear Time Complexity: O(N)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
```

### **Test Cases & Function Calls:**
```python
print(fibonacci(10))  # Output: 55
print(fibonacci_memo(50))  # Output: 12586269025 (Computes instantly)
```

---
## **📌 Exercise 2: Factorial (Head Recursion & Tail Recursion)**
### **Problem Statement:**
Write a recursive function to compute `n!` using:
1. **Head recursion** (process after recursive call)
2. **Tail recursion** (process before recursive call)

### **Solution:**
#### **1️⃣ Head Recursion Factorial**
```python
# Time Complexity: O(N)
def factorial_head(n):
    if n == 0:
        return 1
    return n * factorial_head(n - 1)
```

#### **2️⃣ Tail Recursion Factorial (Optimized)**
```python
# Time Complexity: O(N) (Stack optimization possible)
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, n * acc)
```

### **Test Cases & Function Calls:**
```python
print(factorial_head(5))  # Output: 120
print(factorial_tail(5))  # Output: 120
```

---
## **📌 Exercise 3: Sum of Digits (Nested Recursion)**
### **Problem Statement:**
Write a recursive function to compute the sum of digits of a number.

### **Solution:**
```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
```

### **Test Cases & Function Calls:**
```python
print(sum_of_digits(12345))  # Output: 15
```

---
## **📌 Exercise 4: Tower of Hanoi (Tree Recursion)**
### **Problem Statement:**
Solve the Tower of Hanoi for `n` disks.

### **Solution:**
```python
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)
```

### **Test Cases & Function Calls:**
```python
tower_of_hanoi(3, 'A', 'B', 'C')
```

---
## **📌 Exercise 5: Indirect Recursion (Odd & Even Check)**
### **Problem Statement:**
Use **indirect recursion** to determine if a number is even or odd.

### **Solution:**
```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
```

### **Test Cases & Function Calls:**
```python
print(is_even(10))  # Output: True
print(is_odd(11))   # Output: True
```

---
## **📌 Exercise 6: Minimum Coins Problem (Dynamic Programming with Memoization)**
### **Problem Statement:**
Find the minimum number of coins required to make `N` using a given set of denominations.

### **Solution:**
```python
def min_coins(N, coins, memo={}):
    if N in memo:
        return memo[N]
    if N == 0:
        return 0
    min_count = float('inf')
    for coin in coins:
        if N >= coin:
            min_count = min(min_count, 1 + min_coins(N - coin, coins, memo))
    memo[N] = min_count
    return min_count
```

### **Test Cases & Function Calls:**
```python
coins = [1, 5, 10, 25]
print(min_coins(30, coins))  # Output: 2 (25 + 5)
```

---
## **🎯 Summary**
| **Exercise** | **Recursion Type** | **Time Complexity** |
|-------------|----------------|------------------|
| Fibonacci | Direct & Memoization | O(2^N) → O(N) |
| Factorial | Head & Tail | O(N) |
| Sum of Digits | Nested Recursion | O(log N) |
| Tower of Hanoi | Tree Recursion | O(2^N) |
| Odd/Even Check | Indirect Recursion | O(N) |
| Min Coins Problem | Dynamic with Memoization | O(N * C) |

🧠 **Memoization speeds up recursion dramatically by reducing redundant computations.** 🚀

**Happy Coding!** 🎯🔥