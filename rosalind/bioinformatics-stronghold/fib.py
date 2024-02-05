# Rabbits and Recurrence Relations
# Dynamic Programming

# f_curr = f_prev + (k * f_prev)
def fibonnaci(n, k):
    # Initialization of F1 and F2
    f_curr = 1
    f_prev = 1
    # Iteration from F3
    for i in range(3, n+1):
        # Apply the Fibonacci recurrence relation 
        f_next = f_curr + (k * f_prev)
        # Update for the next iteration
        f_prev, f_curr = f_curr, f_next
    return f_curr

with open("data/rosalind_fib.txt") as f:
    n, k = map(int, f.readline().split())

result = fibonnaci(n, k)
print(result)