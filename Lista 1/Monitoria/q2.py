class Fatorial:
    @staticmethod
    def recursivo(n: int, acc: int) -> int:
        return acc if n == 0 or n == 1 else Fatorial().recursivo(n - 1, n * acc)
    @staticmethod
    def iterativo(n: int) -> int:
        acc = 1
        for num in range(1, n + 1):
            acc *= num
        return acc
    
if __name__ == "__main__":
    num = int(input('Informe um numero: '))

    print('Recursivo: ', Fatorial().recursivo(num, 1))
    print('Iterativo: ', Fatorial().iterativo(num))