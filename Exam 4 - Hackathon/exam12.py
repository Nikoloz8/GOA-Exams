# Task 12: Find All Prime Numbers up to N
# Instructions:
# Write a function find_primes(n) that returns a list of all prime numbers less than or equal to n. The function should:
# Accept a positive integer n.
# Return a list of prime numbers up to n.
# Test Cases:
# assert find_primes(10) == [2, 3, 5, 7]
# assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
# assert find_primes(1) == []
# assert find_primes(2) == [2]

def find_primes(n):
    list = []
    def is_prime(n):
        count = 0
        for i in range(n + 1):
            if i > 0:        
                if n % i == 0:
                    count += 1
        if count == 2:
            return True
        return False
    for i in range(n + 1):
        if is_prime(i):
            list.append(i)
    return list            

print(find_primes(20))

