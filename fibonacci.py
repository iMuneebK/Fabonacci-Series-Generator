"""
High-Performance Fibonacci Series Suite
Author: Muhammad Muneeb Khan
"""
import time
import argparse

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fib_matrix(n):
    if n <= 0:
        return 0
    def multiply(F, M):
        x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
        y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
        z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
        w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
        F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, w

    def power(F, p):
        if p <= 1:
            return
        M = [[1, 1], [1, 0]]
        power(F, p // 2)
        multiply(F, F)
        if p % 2 != 0:
            multiply(F, M)

    F = [[1, 1], [1, 0]]
    power(F, n - 1)
    return F[0][0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fibonacci Series Generator')
    parser.add_argument('--terms', type=int, default=15, help='Number of terms to generate')
    args = parser.parse_args()

    print(f'Generating first {args.terms} Fibonacci numbers:')
    series = list(fib_iterative(args.terms))
    print(series)
    print('\nComputed 1000th Fibonacci number in O(log n):')
    t0 = time.perf_counter()
    val = fib_matrix(1000)
    dt = (time.perf_counter() - t0) * 1e6
    print(f'F(1000) digits: {len(str(val))} digits calculated in {dt:.2f} microseconds')
