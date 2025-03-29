# Task 11: Fibonacci Sequence
# Instructions:
# Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence. The function should:
# Accept a positive integer n as input.
# Return a list of the first n Fibonacci numbers.
# The Fibonacci sequence is defined as:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) for n >= 2
# Test Cases:
# assert fibonacci(1) == [0]
# assert fibonacci(2) == [0, 1]
# assert fibonacci(5) == [0, 1, 1, 2, 3]
# assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def fibonacci(n):
    if n >= 2 :
        
        list = [0, 1]
    
        for i in range(2, n):
            list.append(list[i- 1] + list[i- 2])
        return list

print(fibonacci(7))
        