# The Fibonacci numbers, commonly denoted F(n) form a sequence,
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
# starting from 0 and 1. That is,

def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(fib(4))
