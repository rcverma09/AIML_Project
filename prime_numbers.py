def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    """Find all prime numbers between start and end"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    print("Prime Numbers between 1 and 100:")
    print("=" * 40)
    
    primes = find_primes(1, 100)
    
    print(f"\nTotal primes found: {len(primes)}")
    print("\nPrime numbers:")
    print(primes)
    
    print("\nFormatted output:")
    for i, prime in enumerate(primes, 1):
        print(f"{i}. {prime}")

if __name__ == "__main__":
    main()
