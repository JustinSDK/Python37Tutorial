from typing import List
from functools import reduce

def to_digits(num: int) -> List[int]:
    return [] if num == 0 else ([num % 10] + to_digits(num // 10))

def is_narcissistic(number: int) -> bool:
    digits = to_digits(number)
    return reduce(lambda sum, d: sum + d ** len(digits),
               digits, 0) == number

def narcissistic(n: int) -> List[int]:
    return [i for i in range(1, 10 ** (n if n < 40 else 39))
            if is_narcissistic(i)]

print(narcissistic(3))