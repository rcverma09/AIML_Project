import pandas as pd
import numpy as np

def fibonacci_series(n):
    """Generate Fibonacci series up to n terms"""
    fib_series = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series

def main():
    print("Fibonacci Series (up to 20 terms):")
    fib = fibonacci_series(20)
    print(fib)
    
    print("\nFormatted Fibonacci Series:")
    for i, num in enumerate(fib, 1):
        print(f"Term {i}: {num}")

if __name__ == "__main__":
    main()