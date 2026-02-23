import sys
from functools import lru_cache

# Increase recursion depth for large n
sys.setrecursionlimit(2000)

# --- FACTORIAL SECTION ---

@lru_cache(maxsize=None)
def factorial_memo(n):
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_memo(n - 1)


# --- FIBONACCI SECTION ---

@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 0:
        return "Undefined for negative numbers"
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# --- REUSABLE INPUT HELPER ---

def get_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Please enter a valid integer.")

# --- EXECUTION ---

if __name__ == "__main__":
    n_fact = get_valid_input("Enter a number for Factorial: ")
    print(f"Factorial of {n_fact}: {factorial_memo(n_fact)}")

    n_fib = get_valid_input("Enter a number for Fibonacci: ")
    print(f"Fibonacci of {n_fib}: {fib_memo(n_fib)}")
