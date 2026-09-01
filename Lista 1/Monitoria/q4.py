from typing import List

class Primo:
    @staticmethod
    def eh_primo(n: int) -> bool:
        if n == 2: return True
        if n <= 1 or n % 2 == 0: return False
        for num in range(3, int(n ** 0.5) + 1, 2):
            if n % num == 0: return False
        return True
    @staticmethod
    def intervalo(a: int, b: int) -> List[int]:
        return [num for num in range(a, b + 1) if Primo.eh_primo(num)]

if __name__ == "__main__":
    n = int(input('Informe um numero: '))
    print('Primo' if Primo.eh_primo(n) else 'Nao eh primo')
    a, b = map(int, input('informe o limite inferior e superior: ').split())
    primes = Primo.intervalo(a, b)
    if len(primes) == 0:
        print('Não existe nenhum número primo dentro desse intervalo')
    else:
        for num in primes:
            print(num)