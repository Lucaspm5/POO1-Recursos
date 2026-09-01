from math import log

#altere aqui caso você queira um intervalo maior [first, last + 1)
n = 5000

is_prime = [False] * 2 + [True] * n
def crivo():
	primes = [2, 3]
	next = 2
	for i in range(5, n + 1, next):
		if is_prime[i]:
			is_prime[i * i: n + 1 : 2 * i] = [False] * len(is_prime[i * i : n + 1 : 2 * i])
		next = 6 - next
def variante(x):
	return x == 2 or x == 3 or (is_prime[x] and x % 2 != 0 and x % 3 != 0)
prefix = [0] * (n + 1)
def pre_calculo():
	crivo()
	for i in range(2, n + 1):
		prefix[i] += prefix[i - 1] + (1 if variante(i) else 0)
pre_calculo()
n = int(input('Informe um número a qual deseja verificar se ele é primo ou não: '))
print('É PRIMO' if variante(n) else 'não é primo')
a, b = map(int, input('Informe o intervalo de inicio e o intervalo final respectivamente: ').split())
x = prefix[b] - prefix[a - 1]
print(x if x > 0 else 'Não existe nenhum número primo dentro desse intervalo')

"""
Outra alternativa seria:
	aprox = (b / log(b)) - (a / log(a))
	print(aprox)
"""