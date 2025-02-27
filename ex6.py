#6️⃣ Exercise: Two-Way Communication (Indirect Recursion)
def caller(n):
    if n == 0:
        return
    print(f"Caller: I will speak {n} times.")
    receiver(n - 1)

def receiver(n):
    if n == 0:
        return
    print(f"Receiver: I will reply {n} times.")
    caller(n - 1)

'''
✅ Correction Criteria:
    ☑ Uses mutually recursive functions
    ☑ Prints correct alternating dialogue
    ☑ Stops when n = 0

'''