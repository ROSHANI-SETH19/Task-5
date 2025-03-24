def fibonacci(n):
    # Handle the base cases directly
    if n <= 1:
        return n
    
    # Create a memoization array to store Fibonacci numbers up to n
    fib = [0] * (n + 1)
    fib[0] = 0  # Fibonacci(0)
    fib[1] = 1  # Fibonacci(1)
    
    # Compute Fibonacci numbers from 2 to n using bottom-up dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage
n = 10  # You can change n to compute a different Fibonacci number
print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
