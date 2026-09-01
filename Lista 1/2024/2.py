def iterativo(n):
    partial = 1
    for i in range(1, n + 1): partial *= i
    return partial
def recursivo(n, accumulate):
    return accumulate if n == 0 or n == 1 else recursivo(n - 1, accumulate * n)
n = int(input())
a, b = iterativo(n), recursivo(n, 1)
print('iterativo: {}, recursivo: {}'.format(a, b))
    