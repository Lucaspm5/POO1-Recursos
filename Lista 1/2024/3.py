def memoization():
    #Mudar esse intervalo para testar valores mais altos
    dp = [1 for x in range(1, (1 << 10 + 1))]
    for k in range(1, len(dp)): dp[k] = dp[k - 1] * k
    return dp
dp = memoization()
print("""Informe a quantidade de elementos (n), 
      e a quantidade de elementos pro arranjo (p) e pra combinação (r), respectivamente:
      """)
n, p, r = map(int, input().split())
a, c = dp[n] // dp[n - p], dp[n] // (dp[r] * dp[n - r])
print('Arranjo: {}, Combinação : {}'.format(a, c))

