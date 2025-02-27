#🔥 Bonus Challenge: The Towers of Hanoi (Optimization & Complexity)
def hanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return
    hanoi(n - 1, A, C, B)  # Move top n-1 disks to auxiliary peg
    print(f"Move disk {n} from {A} to {C}")  # Move nth disk to destination
    hanoi(n - 1, B, A, C)  # Move n-1 disks from auxiliary peg to destination

'''
Complexity Analysis:
Time Complexity: O(2^N) 
Space Complexity: O(N) (Recursion depth)

✅ Correction Criteria:
    ☑ Recursive structure follows the Hanoi algorithm
    ☑ Correct sequence of moves
    ☑ Complexity analysis included
'''