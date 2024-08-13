from typing import List

def find_divisors(n: int)->List[int]:
    if n <= 0:
        return[]
    divisors = [i for i in range(1, n + 1)if n % i == 0]
    return divisors

print(find_divisors(20))