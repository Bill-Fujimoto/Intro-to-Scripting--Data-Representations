"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
##    print(answer)
    for divisor in range(2, bound):
        # Remove appropriate multiples of divisor from answer
        for num in answer:
            if num==divisor:
                continue
            else:
                if num%divisor==0:
                    answer.remove(num)
    return answer

##print(compute_primes(200))
print(len(compute_primes(200)))
##print(compute_primes(2000))
print(len(compute_primes(2000)))