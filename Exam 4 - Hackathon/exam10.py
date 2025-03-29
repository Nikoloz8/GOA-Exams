# Task 10: Check if a Number is Prime
# Instructions:
# Write a function is_prime(n) that takes an integer n and returns True if it is a prime number, otherwise False. The function should:
# Accept an integer as input.
# Return True if n is prime, False otherwise.
# Test Cases:
# assert is_prime(2) == True 
# assert is_prime(3) == True 
# assert is_prime(4) == False 
# assert is_prime(11) == True 
# assert is_prime(15) == False

def is_prime(n):
    count = 0
    for i in range(n + 1):
        if i > 0:        
            if n % i == 0:
                count += 1
    if count == 2:
        return True
    return False

print(is_prime(15))
    
    