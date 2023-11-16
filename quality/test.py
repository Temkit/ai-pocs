def generate_primes(max_value):
    if max_value < 2:
        return []

    # Initialize a list to track prime status of numbers
    is_prime = [True] * max_value
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Implement the Sieve of Eratosthenes
    for number in range(2, int(max_value ** 0.5) + 1):
        if is_prime[number]:
            # Mark multiples of the number as non-prime
            for multiple in range(number*number, max_value, number):
                is_prime[multiple] = False

    # Generate the list of primes
    primes = [number for number, prime in enumerate(is_prime) if prime]
    return primes

# Generate and print the list of prime numbers less than 30
prime_numbers = generate_primes(30)
print(prime_numbers)