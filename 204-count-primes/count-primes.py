class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Create a boolean array "prime[0..n]" and initialize
        # all entries as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                # Update all multiples of i to False
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        
        # Count the primes
        return sum(primes)

        